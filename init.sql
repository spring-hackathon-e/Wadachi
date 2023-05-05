DROP DATABASE Wadachi;
DROP USER 'gruper'@'localhost';

CREATE USER 'gruper'@'localhost' IDENTIFIED BY 'Spring_e6';
CREATE DATABASE Wadachi;
USE Wadachi;
GRANT ALL PRIVILEGES ON Wadachi.* TO 'gruper'@'localhost';

CREATE TABLE users (
    user_id VARCHAR(255) PRIMARY KEY NOT NULL,
    user_name VARCHAR(255) UNIQUE NOT NULL,
    email VARCHAR(255) UNIQUE NOT NULL,
    password VARCHAR(250) NOT NULL

);

CREATE TABLE channels (
    ch_id SERIAL PRIMARY KEY,
    user_id VARCHAR(255) REFERENCES users(user_id),
    ch_name VARCHAR(255) UNIQUE NOT NULL,
    summary VARCHAR(255),
    main_category VARCHAR(255),
    sub_category VARCHAR(255),
    created_date TIMESTAMP NOT NULL default current_timestamp
);

CREATE TABLE messages (
    message_id SERIAL PRIMARY KEY,
    user_id VARCHAR(255) REFERENCES users(user_id),
    ch_id INT REFERENCES channel(ch_id) ON DELETE CASCADE,
    message TEXT,
    created_date TIMESTAMP NOT NULL default current_timestamp,
    reaction INT
);

CREATE TABLE posts (
    post_id SERIAL PRIMARY KEY,
    user_id VARCHAR(255) REFERENCES users(user_id),
    title VARCHAR(255) NOT NULL,
    post TEXT,
    created_date TIMESTAMP NOT NULL default current_timestamp,
    study_time INT
);


INSERT INTO users(user_id, user_name, email, password)VALUES('970af84c-dd40-47ff-af23-282b72b7cca8','test','test@gmail.com','37268335dd6931045bdcdf92623ff819a64244b53d0e746d438797349d4da578');
# INSERT INTO channels(id, uid, name, abstract)VALUES(1, '970af84c-dd40-47ff-af23-282b72b7cca8','botti','テストさんの孤独な部屋です');
# INSERT INTO messages(id, uid, cid, message)VALUES(1, '970af84c-dd40-47ff-af23-282b72b7cca8', '1', '誰かかまってください、、');
