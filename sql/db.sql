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
    PRIMARY KEY (electionID),
    FOREIGN KEY (userID) REFERENCES Users(userID) ON DELETE NO ACTION
);

CREATE TABLE IF NOT EXISTS sys.Parties (
    partyID VARCHAR(256) NOT NULL,
    partyName MEDIUMTEXT NOT NULL,
    PRIMARY KEY (partyID)
);

CREATE TABLE IF NOT EXISTS sys.Candidates (
    candidateID VARCHAR(256) NOT NULL,
    fullName VARCHAR(1000) NOT NULL,
    age INTEGER,
    gender BOOLEAN NOT NULL,
    pictureURL MEDIUMTEXT NOT NULL,
    partyID VARCHAR(256) NOT NULL,
    PRIMARY KEY (candidateID),
    FOREIGN KEY (partyID) REFERENCES Parties(partyID) ON DELETE NO ACTION
);

CREATE TABLE IF NOT EXISTS sys.Votes (
    voteID VARCHAR(256) NOT NULL,
    electionID VARCHAR(256) NOT NULL,
    candidateID VARCHAR(256) NOT NULL,
    PRIMARY KEY (voteID),
    FOREIGN KEY (electionID) REFERENCES Elections(electionID) ON DELETE NO ACTION,
    FOREIGN KEY (candidateID) REFERENCES Candidates(candidateID) ON DELETE NO ACTION
);

CREATE TABLE IF NOT EXISTS sys.CandidatesVotersPairings (
    candidateID VARCHAR(256) NOT NULL,
    voterID VARCHAR(256) NOT NULL,
    PRIMARY KEY (candidateID, voterID),
    FOREIGN KEY (candidateID) REFERENCES Candidates(candidateID) ON DELETE NO ACTION,
    FOREIGN KEY (voterID) REFERENCES Users(userID) ON DELETE NO ACTION
);
