-- prepares a MySQL server for the project

CREATE DATABASE IF NOT EXISTS agricecho_test_db;
CREATE USER IF NOT EXISTS 'agricecho_test'@'localhost' IDENTIFIED BY 'agricecho_test_pwd';
GRANT ALL PRIVILEGES ON `agricecho_test_db`.* TO 'agricecho_test'@'localhost';
GRANT SELECT ON `performance_schema`.* TO 'agricecho_test'@'localhost';
FLUSH PRIVILEGES;
