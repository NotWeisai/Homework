import os
import json
import csv
import xml.etree.ElementTree as ET
import yaml
import sqlite3

DB_PATH = "quiz.db"
OUT_DIR = "out"

# ----------------------------
# Подключение к базе данных
# ----------------------------
def get_conn():
    """
    Создаёт соединение с SQLite-базой.
    row_factory делает так, чтобы строки можно было читать как словарь.
    PRAGMA foreign_keys включает поддержку внешних ключей.
    """
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    conn.execute("PRAGMA foreign_keys = ON;")
    return conn


# ----------------------------
# Извлечение основной таблицы + связанных
# ----------------------------
def fetch_table_with_related(table: str, related: dict):
    """
    Загружает данные из основной таблицы и связанных таблиц.

    table — имя основной таблицы: например, "questions".
    related — словарь, указывающий связи:
        {
            "answers": ("answers", "question_id")
        }

    То есть:
        "answers" — имя поля в результирующей структуре,
        "answers" — имя таблицы,
        "question_id" — столбец, ссылающийся на основную таблицу.
    """
    with get_conn() as conn:
        main_rows = conn.execute(f"SELECT * FROM {table}").fetchall()
        result = []

        for row in main_rows:
            row_dict = dict(row)

            # Загружаем данные всех связанных таблиц
            for field, (rel_table, rel_key) in related.items():
                rel_rows = conn.execute(
                    f"SELECT * FROM {rel_table} WHERE {rel_key}=?",
                    (row["id"],)
                ).fetchall()
                row_dict[field] = [dict(r) for r in rel_rows]

            result.append(row_dict)

        return result


# ----------------------------
# Экспорт в JSON
# ----------------------------
def export_json(data, path):
    """Сохраняет структуру данных в формате JSON."""
    with open(path, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=4)


# ----------------------------
# Экспорт в CSV
# ----------------------------
def export_csv(data, path):
    """
    Сохраняет таблицу в CSV.
    Вложенные данные JSON переводятся в строку,
    так как CSV не поддерживает вложенные структуры.
    """
    if not data:
        return

    flat = []
    for row in data:
        clean = {}
        for key, val in row.items():
            if isinstance(val, list):
                clean[key] = json.dumps(val, ensure_ascii=False)
            else:
                clean[key] = val
        flat.append(clean)

    with open(path, "w", encoding="utf-8", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=flat[0].keys())
        writer.writeheader()
        writer.writerows(flat)


# ----------------------------
# Экспорт в XML
# ----------------------------
def export_xml(data, path):
    """
    Сохраняет данные в формате XML,
    корректно добавляя вложенные элементы.
    """
    root = ET.Element("items")

    for row in data:
        item = ET.SubElement(root, "item")

        for key, val in row.items():
            # Если поле — список словарей (например, answers)
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


# ----------------------------
# Экспорт в YAML
# ----------------------------
def export_yaml(data, path):
    """Сохраняет структуру данных в YAML."""
    with open(path, "w", encoding="utf-8") as f:
        yaml.dump(data, f, allow_unicode=True)


# ----------------------------
# Главная функция
# ----------------------------
def main():
    """
    Основной процесс:
    1. Создать папку out
    2. Выгрузить данные из таблицы questions + связанные answers
    3. Сохранить их в JSON, CSV, XML, YAML
    """

    os.makedirs(OUT_DIR, exist_ok=True)

    data = fetch_table_with_related(
        table="users",
        related={"results": ("results", "user_id")}
    )

    export_json(data, os.path.join(OUT_DIR, "data.json"))
    export_csv(data, os.path.join(OUT_DIR, "data.csv"))
    export_xml(data, os.path.join(OUT_DIR, "data.xml"))
    export_yaml(data, os.path.join(OUT_DIR, "data.yaml"))

    print("Готово! Файлы созданы в папке out.")


if __name__ == "__main__":
    main()