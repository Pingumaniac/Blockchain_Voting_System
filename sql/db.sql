-- Alex, please finalize how will you design the database.
-- Guess it will be different from the ER diagram that I have designed. 
-- I will be waiting for your response.
-- I have written all sample queries based on the ER diagram.

CREATE TABLE IF NOT EXISTS sys.Users (
    userID VARCHAR(256) NOT NULL,
    userName VARCHAR(256) NOT NULL,
    password VARCHAR(256) NOT NULL,
    fullName VARCHAR(1000) NOT NULL,
    email VARCHAR(1000) NOT NULL,
    publicKey VARCHAR(256) NOT NULL,
    privateKey VARCHAR(256),
    PRIMARY KEY (userID)
);

CREATE TABLE IF NOT EXISTS sys.Elections (
    electionID VARCHAR(256) NOT NULL,
    prompt MEDIUMTEXT NOT NULL,
    privateKey VARCHAR(256),
    endDate DATE NOT NULL,
    userID VARCHAR(256) NOT NULL,
    yesVotes INT,
    noVotes INT,
    PRIMARY KEY (electionID),
    FOREIGN KEY (userID) REFERENCES Users(userID) ON DELETE NO ACTION
);

CREATE TABLE IF NOT EXISTS sys.Votes (
    userID VARCHAR(256) NOT NULL,
    electionID VARCHAR(256) NOT NULL,
    voteData BOOLEAN,
    privateKey VARCHAR(256),
    PRIMARY KEY (userID, electionID),
    FOREIGN KEY (userID) REFERENCES Users(userID) ON DELETE NO ACTION,
    FOREIGN KEY (electionID) REFERENCES Elections(electionID) ON DELETE NO ACTION
);
