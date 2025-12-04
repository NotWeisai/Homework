#!/usr/bin/env python3
import sys
from models import User, Question, Answer, Result, get_conn
from repository import get_random_questions, get_user_results, get_all_users, get_all_questions, get_question_with_answers
import random
from table_export import export_table  # Для экспорта

def login():
    """Простой логин по username (пароль не добавлен для простоты; можно доработать)."""
    print("\n=== Логин ===")
    username = input("Введите username: ").strip()
    user = User.get_by_username(username)
    if not user:
        print("Пользователь не найден. Создать нового? (y/n): ")
        if input().lower() == 'y':
            role = input("Роль (user/admin): ").strip() or 'user'
            user = User.create(username, role)
            print(f"Создан {user.username} с ролью {user.role}")
        else:
            return None
    print(f"Добро пожаловать, {user.username}! Роль: {user.role}")
    return user

def user_menu(user):
    """Меню для обычного пользователя."""
    while True:
        print("\n=== Меню пользователя ===")
        print("1. Играть в викторину")
        print("2. Просмотреть свои результаты")
        print("3. Выход")
        choice = input("Выбор: ").strip()
        if choice == '1':
            play_quiz(user)
        elif choice == '2':
            view_results(user)
        elif choice == '3':
            break
        else:
            print("Неверный выбор.")

def export_selected_table():
    """Админ выбирает таблицу для экспорта."""
    tables = {
        '1': ('users', {"results": ("results", "user_id")}),  # С результатами
        '2': ('questions', {"answers": ("answers", "question_id")}),  # С ответами
        '3': ('answers', None),  # Чисто ответы
        '4': ('results', {"user": ("users", "id")}),  # С именами юзеров
        '5': ('tags', None),  # Теги
        '6': ('question_tags', {"questions": ("questions", "question_id"), "tags": ("tags", "tag_id")})  # Связи с вопросами/тегами
    }
    print("\n=== Выбери таблицу для экспорта ===")
    for key, (name, rel) in tables.items():
        print(f"{key}. {name}")
    print("0. Назад")
    choice = input("Выбор: ").strip()
    if choice == '0':
        return
    if choice in tables:
        table_name, related = tables[choice]
        export_table(table_name, related)
    else:
        print("Неверный выбор. Попробуй снова.")

def admin_menu(user):
    """Меню для администратора."""
    while True:
        print("\n=== Меню администратора ===")
        print("1. Добавить вопрос")
        print("2. Просмотреть/обновить/удалить вопросы")
        print("3. Добавить пользователя")
        print("4. Просмотреть/удалить пользователей")
        print("5. Экспорт выбранной таблицы")  # НОВОЕ!
        print("6. Выход")  # Сдвинь
        choice = input("Выбор: ").strip()
        if choice == '1':
            add_question()
        elif choice == '2':
            manage_questions()
        elif choice == '3':
            add_user()
        elif choice == '4':
            manage_users()
        elif choice == '5':
            export_selected_table()  # НОВОЕ!
        elif choice == '6':
            break
        else:
            print("Неверный выбор.")

def play_quiz(user):
    """Игра: 5 случайных вопросов, подсчет очков."""
    questions = get_random_questions(5)
    if not questions:
        print("Нет вопросов! Обратитесь к админу.")
        return
    score = 0
    print("\n=== Викторина (5 вопросов) ===")
    for q in questions:
        print(f"\n{q['text']} (Категория: {q['category']})")
        for i, ans in enumerate(q['answers'], 1):
            print(f"{i}. {ans['text']}")
        try:
            choice = int(input("Ваш ответ (номер): ")) - 1
            if 0 <= choice < len(q['answers']) and q['answers'][choice]['is_correct']:
                print("Правильно!")
                score += 1
            else:
                print(f"Неправильно. Правильный: {next(a['text'] for a in q['answers'] if a['is_correct'])}")
        except ValueError:
            print("Неверный ввод. Пропуск.")
    Result.create(user.id, score)
    print(f"\nИгра окончена! Ваш счет: {score}/5")

def view_results(user):
    """Просмотр результатов пользователя."""
    results = get_user_results(user.username)
    if not results:
        print("Нет результатов.")
        return
    print("\n=== Ваши результаты ===")
    for r in results:
        print(f"ID: {r['id']}, Очки: {r['score']}, Дата: {r['played_at']}")

def add_question():
    """Добавление вопроса + 4 ответов (1 правильный)."""
    text = input("Текст вопроса: ").strip()
    category = input("Основная категория (опционально): ").strip() or None  # Оставляем для совместимости
    q = Question.create(text, category)
    print(f"Вопрос создан (ID: {q.id})")
    
    # Добавляем ответы (как было)
    for i in range(4):
        ans_text = input(f"Ответ {i+1}: ").strip()
        is_correct = input("Правильный? (y/n): ").strip().lower() == 'y'
        Answer.add(q.id, ans_text, 1 if is_correct else 0)
    
    # НОВОЕ: Несколько тегов
    print("Добавьте теги (через запятую, напр. География,Легкий): ")
    tag_input = input().strip()
    if tag_input:
        tags = [t.strip() for t in tag_input.split(',')]
        Question.attach_tags(q.id, tags)
        print(f"Теги добавлены: {', '.join(tags)}")
    
    print("Ответы и теги готовы!")

def manage_questions():
    """Просмотр, обновление, удаление вопросов."""
    qs = get_all_questions()
    if not qs:
        print("Нет вопросов.")
        return
    print("\n=== Вопросы ===")
    for q in qs:
        # В цикле for q in qs:
        tags = Question.get_tags(q['id'])
        print(f"ID: {q['id']}, {q['text']} (Категория: {q['category']}, Теги: {', '.join(tags)})")
        for a in q['answers']:
            mark = " (правильный)" if a['is_correct'] else ""
            print(f"  - {a['text']}{mark}")
    qid = int(input("ID вопроса для обновления/удаления (0 - назад): ") or 0)
    if qid == 0:
        return
    if input("Удалить? (y/n): ").lower() == 'y':
        Question.delete(qid)
        reset_autoincrement()  # Добавь эту строку
        print("Удалено и счётчик сброшен.")
    else:
        text = input("Новый текст (Enter - оставить): ").strip() or None
        category = input("Новая категория (Enter - оставить): ").strip() or None
        Question.update(qid, text, category)
        print("Обновлено.")

def reset_autoincrement(table: str = 'questions'):
    """Сброс autoincrement после удаления — следующий ID = MAX+1."""
    with get_conn() as conn:
        conn.execute(f"UPDATE sqlite_sequence SET seq = COALESCE((SELECT MAX(id) FROM {table}), 0) WHERE name = '{table}';")
        conn.commit()
        print(f"Счётчик {table} сброшен на {conn.execute('SELECT seq FROM sqlite_sequence WHERE name=?', (table,)).fetchone()[0] + 1}.")

def add_user():
    """Добавление пользователя."""
    username = input("Username: ").strip()
    role = input("Роль (user/admin): ").strip() or 'user'
    User.create(username, role)
    print("Пользователь добавлен.")

def manage_users():
    """Просмотр и удаление пользователей."""
    users = get_all_users()
    print("\n=== Пользователи ===")
    for u in users:
        print(f"ID: {u['id']}, {u['username']} ({u['role']})")
    uid = int(input("ID для удаления (0 - назад): ") or 0)
    if uid == 0:
        return
    if input("Удалить? (y/n): ").lower() == 'y':
        User.delete(uid)
        print("Удалено.")

def main():
    print("=== Викторина: Добро пожаловать! ===")
    user = login()
    if not user:
        return
    if user.role == 'admin':
        admin_menu(user)
    else:
        user_menu(user)
    print("До свидания!")

if __name__ == "__main__":
    main()
