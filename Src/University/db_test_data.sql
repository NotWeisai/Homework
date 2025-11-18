INSERT OR IGNORE INTO users (username) VALUES ('Алиса'), ('Ваня');

INSERT INTO questions (text, category) VALUES
('Столица Франции?', 'География'),
('Сколько будет 25+76?', 'Математика'),
('Сколько планет в солнечной системе?', 'Астрономия');

INSERT INTO answers (question_id, text, is_correct) VALUES
(1, 'Париж', 1), (1, 'Сыктывкар', 0), (1, 'Рим', 0), (1, 'Прага', 0),
(2, '176', 0), (2, '101', 1), (2, '98', 0), (2, '201', 0),
(3, '9', 0), (3, '11', 0), (3, '288', 0), (3, '8', 1);

INSERT INTO results (user_id, score) VALUES
((SELECT id FROM users WHERE username='Алиса'), 3),
((SELECT id FROM users WHERE username='Ваня'), 1);