from typing import List, Dict, Any
import random
from University.models import get_conn

def get_user_results(username: str) -> List[Dict[str, Any]]:
    """Все результаты конкретного пользователя (по имени)."""
    with get_conn() as conn:
        sql = "SELECT r.id, r.score, r.played_at FROM results r JOIN users u ON u.id = r.user_id WHERE u.username = ? ORDER BY r.played_at DESC"
        rows = conn.execute(sql, (username,)).fetchall()
        return [dict(row) for row in rows]

def get_question_with_answers(question_id: int) -> Dict[str, Any]:
    """Вопрос + его ответы."""
    with get_conn() as conn:
        q = conn.execute("SELECT * FROM questions WHERE id=?", (question_id,)).fetchone()
        if not q:
            return {}
        ans = conn.execute("SELECT id, text, is_correct FROM answers WHERE question_id=?", (question_id,)).fetchall()
        return {"id": q["id"], "text": q["text"], "category": q["category"], "answers": [dict(a) for a in ans]}

def get_questions_by_tag(tag_name: str) -> List[Dict[str, Any]]:
    """Все вопросы, помеченные заданным тегом."""
    with get_conn() as conn:
        sql = "SELECT q.id, q.text, q.category FROM questions q JOIN question_tags qt ON qt.question_id = q.id JOIN tags t ON t.id = qt.tag_id WHERE t.name = ? ORDER BY q.id"
        rows = conn.execute(sql, (tag_name,)).fetchall()
        return [dict(r) for r in rows]

def get_random_questions(limit: int = 5) -> List[Dict[str, Any]]:
    """Случайный набор вопросов для игры (с ответами, перемешанными)."""
    with get_conn() as conn:
        qs = conn.execute("SELECT * FROM questions ORDER BY RANDOM() LIMIT ?", (limit,)).fetchall()
        result = []
        for q in qs:
            ans = conn.execute("SELECT id, text, is_correct FROM answers WHERE question_id=?", (q["id"],)).fetchall()
            shuffled_ans = list(ans)
            random.shuffle(shuffled_ans)
            result.append({
                "id": q["id"], "text": q["text"], "category": q["category"],
                "answers": [dict(a) for a in shuffled_ans]
            })
        return result

def get_all_users() -> List[Dict[str, Any]]:
    """Все пользователи."""
    with get_conn() as conn:
        sql = "SELECT id, username, role, created_at FROM users ORDER BY username"
        rows = conn.execute(sql).fetchall()
        return [dict(row) for row in rows]

def get_all_questions() -> List[Dict[str, Any]]:
    """Все вопросы с ответами."""
    with get_conn() as conn:
        qs = conn.execute("SELECT * FROM questions ORDER BY id").fetchall()
        result = []
        for q in qs:
            ans = conn.execute("SELECT id, text, is_correct FROM answers WHERE question_id=?", (q["id"],)).fetchall()
            result.append({
                "id": q["id"], "text": q["text"], "category": q["category"],
                "answers": [dict(a) for a in ans]
            })
        return result
