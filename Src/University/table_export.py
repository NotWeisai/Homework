import os
import json
import csv
import xml.etree.ElementTree as ET
import yaml  # pip install pyyaml if needed
import sqlite3

DB_PATH = "quiz.db"
OUT_DIR = "out"

def get_conn():
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    conn.execute("PRAGMA foreign_keys = ON;")
    return conn

def fetch_table_with_related(table: str, related: dict = None):
    """Извлечение таблицы + связанных."""
    if related is None:
        related = {}
    with get_conn() as conn:
        main_rows = conn.execute(f"SELECT * FROM {table} ORDER BY id").fetchall()
        result = []
        for row in main_rows:
            row_dict = dict(row)
            for field, (rel_table, rel_key) in related.items():
                rel_rows = conn.execute(f"SELECT * FROM {rel_table} WHERE {rel_key}=?", (row["id"],)).fetchall()
                row_dict[field] = [dict(r) for r in rel_rows]
            result.append(row_dict)
        return result

def export_json(data, path):
    with open(path, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=4)

def export_csv(data, path):
    if not data:
        return
    flat = []
    for row in data:
        clean = {k: json.dumps(v, ensure_ascii=False) if isinstance(v, list) else v for k, v in row.items()}
        flat.append(clean)
    with open(path, "w", encoding="utf-8", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=flat[0].keys())
        writer.writeheader()
        writer.writerows(flat)

def export_xml(data, path):
    root = ET.Element("items")
    for row in data:
        item = ET.SubElement(root, "item")
        for key, val in row.items():
            if isinstance(val, list):
                parent = ET.SubElement(item, key)
                for block in val:
                    sub_el = ET.SubElement(parent, "entry")
                    for k, v in block.items():
                        sub_c = ET.SubElement(sub_el, k)
                        sub_c.text = str(v)
            else:
                child = ET.SubElement(item, key)
                child.text = str(val)
    tree = ET.ElementTree(root)
    tree.write(path, encoding="utf-8", xml_declaration=True)

def export_yaml(data, path):
    with open(path, "w", encoding="utf-8") as f:
        yaml.dump(data, f, allow_unicode=True, default_flow_style=False, indent=2)

def main():
    os.makedirs(OUT_DIR, exist_ok=True)
    
    # Экспорт users + results
    users_data = fetch_table_with_related("users", {"results": ("results", "user_id")})
    export_json(users_data, os.path.join(OUT_DIR, "users.json"))
    export_csv(users_data, os.path.join(OUT_DIR, "users.csv"))
    export_xml(users_data, os.path.join(OUT_DIR, "users.xml"))
    export_yaml(users_data, os.path.join(OUT_DIR, "users.yaml"))
    
    # Экспорт questions + answers
    questions_data = fetch_table_with_related("questions", {"answers": ("answers", "question_id")})
    export_json(questions_data, os.path.join(OUT_DIR, "questions.json"))
    export_csv(questions_data, os.path.join(OUT_DIR, "questions.csv"))
    export_xml(questions_data, os.path.join(OUT_DIR, "questions.xml"))
    export_yaml(questions_data, os.path.join(OUT_DIR, "questions.yaml"))
    
    print("Готово! Файлы созданы в папке out.")

if __name__ == "__main__":
    main()
