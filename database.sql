CREATE DATABASE IF NOT EXISTS `users_db`;
USE `users_db`;

CREATE TABLE IF NOT EXISTS `users` (
	`id` INT UNIQUE NOT NULL AUTO_INCREMENT PRIMARY KEY,
    `name` VARCHAR(50) NOT NULL,
    `password` VARCHAR(24) NOT NULL,
    `score` INT DEFAULT 0
);


CREATE TABLE IF NOT EXISTS `score` (
	`score_id` INT UNIQUE NOT NULL AUTO_INCREMENT PRIMARY KEY,
    `user_id` INT NOT NULL,
    `score` INT NOT NULL,
	FOREIGN KEY (user_id) REFERENCES users(id)
);

