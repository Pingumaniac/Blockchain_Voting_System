-- Add more table as needed. I have added a sample query for creating a table for Users here.
-- Alex, please finalize how will you design the database.
-- Guess it will be different from the ER diagram that I have designed.

CREATE TABLE IF NOT EXISTS sys.Users (
    userID VARCHAR(256) NOT NULL,
    userName VARCHAR(256) NOT NULL,
    password VARCHAR(256) NOT NULL,
    fullName VARCHAR(1000) NOT NULL,
    email VARCHAR(1000) NOT NULL,
    publicKey VARCHAR(1000) NOT NULL,
    privateKey VARCHAR(1000) NOT NULL,
    PRIMARY KEY (userID)
);
