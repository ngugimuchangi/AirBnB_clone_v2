-- Script to prepare MySQL server for AirBnB_v2

-- Creeate database 'hbnb_dev_db'
CREATE DATABASE IF NOT EXISTS hbnb_dev_db;
-- Create user 'hbnb_dev'
CREATE USER IF NOT EXISTS 'hbnb_dev'@'localhost' IDENTIFIED BY 'hbnb_dev_pwd';
-- Grant all privileges to 'hbnb_dev' on 'hbnb_dev_db' database
GRANT ALL PRIVILEGES ON hbnb_dev_db.* TO 'hbnb_dev'@'localhost';
-- Grant select privileges to 'hbnb_deve' on 'performance schema' database
GRANT SELECT ON performance_schema.* TO 'hbnb_dev'@'localhost';
