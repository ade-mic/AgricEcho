-- prepares a MySQL server for the project

CREATE DATABASE IF NOT EXISTS agricecho_dev_db;
CREATE USER IF NOT EXISTS 'agriecho_dev'@'localhost' IDENTIFIED BY 'agriecho_dev_pwd';
GRANT ALL PRIVILEGES ON `agriecho_dev_db`.* TO 'agriecho_dev'@'localhost';
GRANT SELECT ON `performance_schema`.* TO 'agriecho_dev'@'localhost';
FLUSH PRIVILEGES;
