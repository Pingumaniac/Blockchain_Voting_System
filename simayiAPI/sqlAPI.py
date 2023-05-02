import pymysql
import json # used for json.dumps() for REST API

class DB():
    def __init__(self):
        self.conn = pymysql.connect(
                    host =  'database-1.cj5a1jigdz45.us-east-2.rds.amazonaws.com',
                    port = 3306,
                    user = 'GloriousPingu',
                    password = 'TheGloriousPinguEmpire',
                    database = 'sys',
                    )
        self.cursor = self.conn.cursor()
        
    def connectDB(self):
        if self.conn.open != True:
            self.conn = pymysql.connect(
                host =  'database-1.cj5a1jigdz45.us-east-2.rds.amazonaws.com',
                port = 3306,
                user = 'GloriousPingu',
                password = 'TheGloriousPinguEmpire',
                database = 'sys',
                )
            self.cursor = self.conn.cursor()
    
    def disconnectDB(self):
        self.conn.close()
    
    def getUserNameExistence(self, userName):
        query1 = 'SELECT COUNT(userName) FROM Users where userName = (%s)'
        self.cursor.execute(query1, (userName, ))
        accountExistence = self.cursor.fetchone()
        return accountExistence

    def getUserNameAndPassword(self, userName):
        query1 = 'SELECT userName, password FROM Users WHERE userName = (%s)'
        self.cursor.execute(query1, (userName, ))
        userDataTable = self.cursor.fetchone()
        return userDataTable
    
    def addUser(self, userID, userName, password, fullName, email, publicKey, privateKey):
        query1 = 'INSERT INTO Users VALUES (%s, %s, %s, %s, %s, %s, %s)'
        self.cursor.execute(query1, (userID, userName, password, fullName, email, publicKey, privateKey)) 
        self.conn.commit()
    
    def getUserData(self, userName):
        query1 = 'SELECT * FROM Users WHERE userName = (%s)'
        self.cursor.execute(query1, (userName, ))
        userDataTable = self.cursor.fetchone()
        return userDataTable

    def getUserID(self, userName):
        query1 = 'SELECT userID FROM Users WHERE userName = (%s)'
        self.cursor.execute(query1, (userName, ))
        userID = self.cursor.fetchone()
        return userID

    def getUserFullName(self, userName):
        query1 = 'SELECT fullName FROM Users WHERE userName = (%s)'
        self.cursor.execute(query1, (userName, ))
        fullName = self.cursor.fetchone()
        return fullName

    def getUserEmail(self, userName):
        query1 = 'SELECT email FROM Users WHERE userName = (%s)'
        self.cursor.execute(query1, (userName, ))
        email = self.cursor.fetchone()
        return email

    def getUserPublicKey(self, userName):
        query1 = 'SELECT publicKey FROM Users WHERE userName = (%s)'
        self.cursor.execute(query1, (userName, ))
        publicKey = self.cursor.fetchone()
        return publicKey

    def getUserPrivateKey(self, userName):
        query1 = 'SELECT privateKey FROM Users WHERE userName = (%s)'
        self.cursor.execute(query1, (userName, ))
        privateKey = self.cursor.fetchone()
        return privateKey
    
    def deleteUser(self, userName):
        query1 = 'DELETE FROM Users WHERE userName = (%s)'
        self.cursor.execute(query1, (userName))
        self.conn.commit()
    
    def addElection(self, electionTitle, electionPrompt, electionPK, electionEndDate, electionUserName):
        query1 = 'INSERT INTO Elections VALUES (%s, %s, %s, %s, %s, %s, %s)'
        self.cursor.execute(query1, (electionTitle, electionPrompt, electionPK, electionEndDate, electionUserName, 0, 0))
        self.conn.commit()
    
    def getMyElection(self, userID):
        query1 = 'SELECT * FROM Elections WHERE userID = (%s)'
        self.cursor.execute(query1, (userID, ))
        myElectionTable = self.cursor.fetchall()
        return myElectionTable
    
    def getCurrentElection(self, endDateInput):
        query1 = 'SELECT * FROM Elections WHERE endDate >= (%s)'
        self.cursor.execute(query1, (endDateInput))
        myElectionTable = self.cursor.fetchall()
        return myElectionTable

    def getPastElection(self, endDateInput):
        query1 = 'SELECT * FROM Elections WHERE endDate < (%s)'
        self.cursor.execute(query1, (endDateInput))
        myElectionTable = self.cursor.fetchall()
        return myElectionTable
