-- Script to prepare MySQL server for AirBnB_v2
-- Creates:
--	* new user 'hbnb_dev' in localhost
--	* new database 'hbnb_dev_db'
-- Assigns: hbnb_dev with:
-- 	* All privileges on the database 'hbnb_dev_db'
--	* SELECT privilege on the database 'performance_schema'
-- Query 1
CREATE DATABASE IF NOT EXISTS hbnb_dev_db;
-- Query 2
CREATE USER IF NOT EXISTS 'hbnb_dev'@'localhost' IDENTIFIED BY 'hbnb_dev_pwd';
-- Query 3
GRANT ALL PRIVILEGES ON hbnb_dev_db.* TO 'hbnb_dev'@'localhost';
-- Query 4
GRANT SELECT ON performance_schema.* TO 'hbnb_dev'@'localhost';
