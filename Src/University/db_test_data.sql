INSERT OR IGNORE INTO users (username, role) VALUES 
('Алиса', 'user'), 
('Ваня', 'user'), 
('admin', 'admin');

INSERT INTO questions (text, category) VALUES
('Столица Франции?', 'География'),
('Сколько будет 25+76?', 'Математика'),
('Сколько планет в солнечной системе?', 'Астрономия'),
('Кто написал "Войну и мир"?', 'Литература'),
('Какой газ составляет 78% атмосферы Земли?', 'Наука'),
('Столица Японии?', 'География'),
('2^10 = ?', 'Математика'),
('Сколько континентов на Земле?', 'География'),
('Первый президент США?', 'История'),
('Скорость света в вакууме (км/с)?', 'Физика');

INSERT INTO answers (question_id, text, is_correct) VALUES
(1, 'Париж', 1), (1, 'Сыктывкар', 0), (1, 'Рим', 0), (1, 'Прага', 0),
(2, '176', 0), (2, '101', 1), (2, '98', 0), (2, '201', 0),
(3, '9', 0), (3, '11', 0), (3, '288', 0), (3, '8', 1),
(4, 'Лев Толстой', 1), (4, 'Достоевский', 0), (4, 'Пушкин', 0), (4, 'Гоголь', 0),
(5, 'Азот', 1), (5, 'Кислород', 0), (5, 'Углекислый газ', 0), (5, 'Гелий', 0),
(6, 'Токио', 1), (6, 'Киото', 0), (6, 'Осака', 0), (6, 'Хиросима', 0),
(7, '1024', 1), (7, '1000', 0), (7, '512', 0), (7, '2048', 0),
(8, '7', 1), (8, '5', 0), (8, '6', 0), (8, '8', 0),
(9, 'Джордж Вашингтон', 1), (9, 'Авраам Линкольн', 0), (9, 'Томас Джефферсон', 0), (9, 'Барак Обама', 0),
(10, '300000', 1), (10, '150000', 0), (10, '500000', 0), (10, '100000', 0);

INSERT INTO results (user_id, score) VALUES
((SELECT id FROM users WHERE username='Алиса'), 3),
((SELECT id FROM users WHERE username='Ваня'), 1),
((SELECT id FROM users WHERE username='Алиса'), 2),
((SELECT id FROM users WHERE username='Ваня'), 4),
((SELECT id FROM users WHERE username='Алиса'), 5);

-- НОВОЕ: Заполнение тегов
INSERT OR IGNORE INTO tags (name) VALUES 
('География'), ('Математика'), ('Астрономия'), ('Литература'), ('Наука'), ('История'), ('Физика');

-- Привязка тегов к вопросам (многие-ко-многим)
INSERT OR IGNORE INTO question_tags (question_id, tag_id) VALUES 
(1, (SELECT id FROM tags WHERE name='География')),  -- Вопрос 1: География
(2, (SELECT id FROM tags WHERE name='Математика')), -- Вопрос 2: Математика
(3, (SELECT id FROM tags WHERE name='Астрономия')), -- И т.д.
(4, (SELECT id FROM tags WHERE name='Литература')),
(5, (SELECT id FROM tags WHERE name='Наука')),
(6, (SELECT id FROM tags WHERE name='География')),
(7, (SELECT id FROM tags WHERE name='Математика')),
(8, (SELECT id FROM tags WHERE name='География')),
(9, (SELECT id FROM tags WHERE name='История')),
(10, (SELECT id FROM tags WHERE name='Физика'));
