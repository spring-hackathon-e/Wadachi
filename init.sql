
DROP DATABASE chatapp;
DROP USER 'testuser'@'localhost';

CREATE USER 'testuser'@'localhost' IDENTIFIED BY 'testuser';
CREATE DATABASE chatapp;
USE chatapp
GRANT ALL PRIVILEGES ON chatapp.* TO 'testuser'@'localhost';

--usersテーブルの作成
CREATE TABLE users (
     user_id VARCHAR(255) PRIMARY KEY, NOT NULL,
     user_name VARCHAR(255) UNIQUE, NOT NULL,
     email VARCHAR(255) UNIQUE, NOT NULL,
     password VARCHAR(50) NOT NULL,
     goal TEXT,
     start_date DATE, NOT NULL
);

--channelsテーブルの作成
CREATE TABLE channels (
    ch_id SERIAL PRIMARY KEY,
    user_id VARCHAR(255) REFERENCES users(user_id),
    ch_name VARCHAR(255) UNIQUE, NOT NULL,
    summary VARCHAR(255),
    main_category VARCHAR(255),
    sub_category VARCHAR(255),
    created_date TIMESTAMP not null default current_timestamp
);

--messagesテーブルの作成
CREATE TABLE messages (
    message_id SERIAL PRIMARY KEY,
    user_id VARCHAR(255) REFERENCES users(user_id),
    ch_id INT REFERENCES channel(ch_id) ON DELETE CASCADE,
    message TEXT,
    created_date TIMESTAMP not null default current_timestamp,
    reaction INT
);

--postsテーブルの作成
CREATE TABLE posts (
    post_id SERIAL PRIMARY KEY,
    user_id VARCHAR(255) REFERENCES users(user_id),
    title VARCHAR(255) NOT NULL,
    post TEXT,
    created_date TIMESTAMP not null default current_timestamp,
    study_time INT
);

--VALUE以降が不明だったので一旦コメント化しています。
--INSERT INTO users(user_id, user_name, email, password, goal, start_date)VALUES('970af84c-dd40-47ff-af23-282b72b7cca8','テスト','test@gmail.com','37268335dd6931045bdcdf92623ff819a64244b53d0e746d438797349d4da578');--
--INSERT INTO channels(ch_id, user_id, ch_name, summary, main_category, sub_category, created_date)VALUES(1, '970af84c-dd40-47ff-af23-282b72b7cca8','ぼっち部屋','テストさんの孤独な部屋です');
--INSERT INTO messages(message_id, user_id, ch_id, message, created_date, reaction)VALUES(1, '970af84c-dd40-47ff-af23-282b72b7cca8', '1', '誰かかまってください、、')
--INSERT INTO posts(post_id, user_id, title, post, created_date, study_time)VALUES(1, '970af84c-dd40-47ff-af23-282b72b7cca8', '1', '誰かかまってください、、')
