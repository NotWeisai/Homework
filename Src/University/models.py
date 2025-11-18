from dataclasses import dataclass
from typing import Optional, List
import sqlite3

DB_PATH = "quiz.db"

def get_conn():
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    conn.execute("PRAGMA foreign_keys = ON;")
    return conn

# ======= MODELS =======

@dataclass
class User:
    id: Optional[int]
    username: str
    created_at: Optional[str] = None

    @staticmethod
    def create(username: str) -> "User":
        with get_conn() as conn:
            cur = conn.execute(
                "INSERT INTO users (username) VALUES (?)",
                (username,))
            uid = cur.lastrowid
            row = conn.execute("SELECT * FROM users WHERE id=?", (uid,)).fetchone()
            return User(id=row["id"], username=row["username"], created_at=row["created_at"])

    @staticmethod
    def get_by_username(username: str) -> Optional["User"]:
        with get_conn() as conn:
            row = conn.execute("SELECT * FROM users WHERE username=?", (username,)).fetchone()
            return User(id=row["id"], username=row["username"], created_at=row["created_at"]) if row else None


@dataclass
class Question:
    id: Optional[int]
    text: str
    category: Optional[str] = None
    created_at: Optional[str] = None

    @staticmethod
    def create(text: str, category: Optional[str]=None) -> "Question":
        with get_conn() as conn:
            cur = conn.execute(
                "INSERT INTO questions (text, category) VALUES (?, ?)",
                (text, category))
            qid = cur.lastrowid
            row = conn.execute("SELECT * FROM questions WHERE id=?", (qid,)).fetchone()
            return Question(id=row["id"], text=row["text"], category=row["category"], created_at=row["created_at"])

    @staticmethod
    def update(qid: int, text: Optional[str]=None, category: Optional[str]=None) -> None:
        with get_conn() as conn:
            if text is not None and category is not None:
                conn.execute("UPDATE questions SET text=?, category=? WHERE id=?", (text, category, qid))
            elif text is not None:
                conn.execute("UPDATE questions SET text=? WHERE id=?", (text, qid))
            elif category is not None:
                conn.execute("UPDATE questions SET category=? WHERE id=?", (category, qid))

    @staticmethod
    def delete(qid: int) -> None:
        with get_conn() as conn:
            conn.execute("DELETE FROM questions WHERE id=?", (qid,))


@dataclass
class Answer:
    id: Optional[int]
    question_id: int
    text: str
    is_correct: int  # 0/1

    @staticmethod
    def add(question_id: int, text: str, is_correct: int) -> "Answer":
        with get_conn() as conn:
            cur = conn.execute(
                "INSERT INTO answers (question_id, text, is_correct) VALUES (?, ?, ?)",
                (question_id, text, is_correct))
            aid = cur.lastrowid
            row = conn.execute("SELECT * FROM answers WHERE id=?", (aid,)).fetchone()
            return Answer(id=row["id"], question_id=row["question_id"], text=row["text"], is_correct=row["is_correct"])

    @staticmethod
    def delete_by_question(question_id: int) -> None:
        with get_conn() as conn:
            conn.execute("DELETE FROM answers WHERE question_id=?", (question_id,))


@dataclass
class Result:
    id: Optional[int]
    user_id: int
    score: int
    played_at: Optional[str] = None

    @staticmethod
    def create(user_id: int, score: int) -> "Result":
        with get_conn() as conn:
            cur = conn.execute(
                "INSERT INTO results (user_id, score) VALUES (?, ?)",
                (user_id, score))
            rid = cur.lastrowid
            row = conn.execute("SELECT * FROM results WHERE id=?", (rid,)).fetchone()
            return Result(id=row["id"], user_id=row["user_id"], score=row["score"], played_at=row["played_at"])


@dataclass
class Tag:
    id: Optional[int]
    name: str

    @staticmethod
    def get_or_create(name: str) -> "Tag":
        with get_conn() as conn:
            row = conn.execute("SELECT * FROM tags WHERE name=?", (name,)).fetchone()
            if row:
                return Tag(id=row["id"], name=row["name"])
            cur = conn.execute("INSERT INTO tags (name) VALUES (?)", (name,))
            tid = cur.lastrowid
            row = conn.execute("SELECT * FROM tags WHERE id=?", (tid,)).fetchone()
            return Tag(id=row["id"], name=row["name"])

    @staticmethod
    def attach_to_question(question_id: int, tag_name: str) -> None:
        tag = Tag.get_or_create(tag_name)
        with get_conn() as conn:
            conn.execute(
                "INSERT OR IGNORE INTO question_tags (question_id, tag_id) VALUES (?, ?)",
                (question_id, tag.id))