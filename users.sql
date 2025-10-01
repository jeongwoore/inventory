CREATE DATABASE IF NOT EXISTS burger DEFAULT CHARACTER SET utf8mb4;

USE burger;

CREATE TABLE IF NOT EXISTS users (
  id INT PRIMARY KEY AUTO_INCREMENT,
  username VARCHAR(50) UNIQUE NOT NULL,
  password VARCHAR(100) NOT NULL
);

INSERT INTO users (username, password) 
VALUES ('admin', 'admin123'), ('seo', 'tjwjddn'), ('root', '1234')
ON DUPLICATE KEY UPDATE password=VALUES(password);
