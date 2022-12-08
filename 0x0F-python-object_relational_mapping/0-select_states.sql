-- Create a database
CREATE DATABASE IF NOT EXISTS hbtn_0e_0_usa;
USE hbtn_0e_0_usa;
CREATE TABLE IF NOT EXISTS States (
    id INT NOT NULL AUTO_INCREMENT,
    name VARCHAR(2560) NOT NULL,
    PRIMARY KEY (id)
);
INSERT INTO States (name)
VALUES ("California"), ("Arizona"), ("Texas"), ("New York"), ("Nevada");