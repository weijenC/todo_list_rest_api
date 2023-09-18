-- Create the "cognixus" database if it doesn't exist
CREATE DATABASE IF NOT EXISTS cognixus;

-- Switch to the "cognixus" database
USE cognixus;

-- Create the "todolist" table with specified columns and constraints
CREATE TABLE IF NOT EXISTS todolist (
    id INT AUTO_INCREMENT PRIMARY KEY,
    item VARCHAR(255) NOT NULL,
    status TINYINT(1) DEFAULT 0 NOT NULL,
    owner VARCHAR(255) NOT NULL,
    created TIMESTAMP DEFAULT CURRENT_TIMESTAMP NOT NULL,
    modified TIMESTAMP DEFAULT CURRENT_TIMESTAMP NOT NULL
);
