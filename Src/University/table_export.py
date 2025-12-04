import os
import json
import csv
import xml.etree.ElementTree as ET
import yaml
import sqlite3

DB_PATH = "quiz.db"
OUT_DIR = "out"

def get_conn():
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    conn.execute("PRAGMA foreign_keys = ON;")
    return conn

def fetch_table_with_related(table: str, related: dict = None):
    if related is None:
        related = {}
    with get_conn() as conn:
        try:
            main_rows = conn.execute(f"SELECT * FROM {table} ORDER BY rowid ASC").fetchall()
        except sqlite3.OperationalError:
            print(f"Таблица {table} не существует.")
            return []
        result = []
        for row in main_rows:
            row_dict = dict(row)
            for field, rel_info in related.items():
                if isinstance(rel_info, tuple) and len(rel_info) >= 2:
                    rel_table, rel_col = rel_info[0], rel_info[1]
                    main_col = rel_info[2] if len(rel_info) > 2 else "id"
                else:
                    continue  # Invalid
                if main_col not in row:
                    row_dict[field] = []
                    continue
                value = row[main_col]
                rel_rows = conn.execute(f"SELECT * FROM {rel_table} WHERE {rel_col}=?", (value,)).fetchall()
                row_dict[field] = [dict(r) for r in rel_rows]
            result.append(row_dict)
        return result

def export_json(data, path):
    with open(path, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=4)

def export_csv(data, path):
    if not data:
        return
    flat = [{k: json.dumps(v, ensure_ascii=False) if isinstance(v, list) else v for k, v in row.items()} for row in data]
    if flat:
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
                    sub = ET.SubElement(parent, "entry")
                    for k, v in block.items():
                        child = ET.SubElement(sub, k)
                        child.text = str(v)
            else:
                child = ET.SubElement(item, key)
                child.text = str(val)
    ET.ElementTree(root).write(path, encoding="utf-8", xml_declaration=True)

def export_yaml(data, path):
    with open(path, "w", encoding="utf-8") as f:
        yaml.dump(data, f, allow_unicode=True, default_flow_style=False, indent=2)

def export_table(table: str, related: dict = None):
    data = fetch_table_with_related(table, related)
    if not data:
        print(f"Таблица {table} пуста.")
        return
    os.makedirs(OUT_DIR, exist_ok=True)
    base = table
    export_json(data, os.path.join(OUT_DIR, f"{base}.json"))
    export_csv(data, os.path.join(OUT_DIR, f"{base}.csv"))
    export_xml(data, os.path.join(OUT_DIR, f"{base}.xml"))
    export_yaml(data, os.path.join(OUT_DIR, f"{base}.yaml"))
    print(f"Экспорт {table} ({len(data)} записей) в out/.")

