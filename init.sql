DROP DATABASE Wadachi;
DROP USER 'gruper'@'localhost';

CREATE USER 'gruper'@'localhost' IDENTIFIED BY 'Spring_e6';
CREATE DATABASE Wadachi;
USE Wadachi
GRANT ALL PRIVILEGES ON Wadachi.* TO 'gruper'@'localhost';

--　usersテーブルの作成
CREATE TABLE users (
    user_id VARCHAR(255) PRIMARY KEY, NOT NULL,
    user_name VARCHAR(255) UNIQUE, NOT NULL,
    email VARCHAR(255) UNIQUE, NOT NULL,
    password VARCHAR(255) NOT NULL,
    goal TEXT,
    start_date DATE, NOT NULL
);

--　channelsテーブルの作成
CREATE TABLE channels (
    ch_id SERIAL PRIMARY KEY,
    user_id VARCHAR(255) REFERENCES users(user_id),
    ch_name VARCHAR(255) UNIQUE NOT NULL,
    summary VARCHAR(255),
    main_category VARCHAR(255),
    sub_category VARCHAR(255),
    created_date TIMESTAMP not null default current_timestamp
);

--　messagesテーブルの作成
CREATE TABLE messages (
    message_id SERIAL PRIMARY KEY,
    user_id VARCHAR(255) REFERENCES users(user_id),
    ch_id INT REFERENCES channel(ch_id) ON DELETE CASCADE,
    message TEXT,
    created_date TIMESTAMP not null default current_timestamp,
    reaction INT
);

--　postsテーブルの作成
CREATE TABLE posts (
    post_id SERIAL PRIMARY KEY,
    user_id VARCHAR(255) REFERENCES users(user_id),
    title VARCHAR(255) NOT NULL,
    post TEXT,
    created_date TIMESTAMP not null default current_timestamp,
    study_time INT
);
