import sqlite3, pathlib
conn = sqlite3.connect("quiz.db")
conn.execute("PRAGMA foreign_keys = ON;")
with open("src/University/db_init.sql", "r", encoding="utf-8") as f:
    conn.executescript(f.read())
with open("src/University/db_test_data.sql", "r", encoding="utf-8") as f:
    conn.executescript(f.read())
conn.commit()
conn.close()
print("База данных создана и заполнена тестовыми данными.")