-- Project: echo input
-- What it does: stores a name and age then selects them back out
-- Run: sqlite3 echo.db < main.sql
-- Note: SQL has no interactive input — data is provided via INSERT

CREATE TABLE IF NOT EXISTS user_input (
    name TEXT,
    age  TEXT
);

INSERT INTO user_input (name, age) VALUES ('London', '22');

SELECT
    'You entered:' AS message;

SELECT
    '  Name: ' || name AS output
FROM user_input;

SELECT
    '  Age:  ' || age AS output
FROM user_input;
