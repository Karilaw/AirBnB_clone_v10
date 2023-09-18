 -- This script sets up a MySQL database named hbnb_test_db
-- It assigns a password to the user and grants necessary privileges
-- The script also grants SELECT privilege on the performance_schema


-- create Database
CREATE DATABASE IF NOT EXISTS hbnb_test_db;

-- Create or Use the User and Set Password
CREATE USER IF NOT EXISTS 'hbnb_test'@'localhost' IDENTIFIED BY 'hbnb_test_pwd';

--Grant Privileges
GRANT ALL PRIVILEGES ON hbnb_test_db.* TO 'hbnb_test'@'localhost';

-- Grant SELECT Privilege on the performance_schema Database
GRANT SELECT ON performance_schema.* TO 'hbnb_test'@'localhost';

FLUSH PRIVILEGES;