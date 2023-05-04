# Name of the app: Simayi
CS 6381 Distributed Systems Principles Final Project - An implementation of a web-based blockchain voting system.

## About Members and Roles

#### Young-jae Moon
* M.Sc. in computer science and Engineering Graduate Fellowship recipient at Vanderbilt University (January 2023 - December 2024).
* Email: youngjae.moon@Vanderbilt.Edu

#### Alex Richardson
* M.Sc./Ph.D. in computer science and Engineering Graduate Fellowship recipient at Vanderbilt University.
* Email: william.a.richardson@vanderbilt.edu

#### Azhar Hasan
* M.Sc./Ph.D. in computer science and Engineering Graduate Fellowship recipient at Vanderbilt University.
* Email: azhar.hasan@vanderbilt.edu

## Advisor

#### Professor Aniruddha Gokhale
* Professor of Computer Science at Vanderbilt University

## Project Goals

We will implement a web-based blockchain voting system that 
1. allows for people to create arbitrary elections and answer them
2. while storing the information in several redundant nodes as per a standard blockchain with each block in the chain either a created election or a user casting vote
3. with several backend nodes maintaining chains separately
4. heavily based on the original bitcoin paper for simplicity.

## Key Performance Indicators (KPI)

1. Blockchain chain agreement
2. Performance
3. Decentralisation
4. Load balancing
5. Validation of System Reliability with Malicious Nodes
6. Transparency
7. Consensus

## Tools and technologies

### Programming languages and Database Management System (DBMS) used

1. JavaScript (ECMAScript 2023)
2. MySQL (MySQL Community Edition 8.0.33)
3. Python (3.11.2)
4. PHP

### Frameworks used

1. Bootstrap front-end framework (v5.3)
2. Flask framework (v2.2.3)

### Python libraries and 3rd party packages used

1. cryptography (40.0.2)
2. Flask-Bootstrap (v3.3.7.1)
3. Gunicorn (v20.1.0)
4. pysqlite3 (v0.5.0)

## How to build this software

### 1. Install the following python packages using pip in the terminal:

```
pip3 install cryptography
pip3 install flask 
pip3 install Flask-Bootstrap
pip3 install gunicorn
pip3 install pysqlite3
```

### 2. Deployment method

#### We will use Netlify to deploy the Flask. Note that:
 1. Git must be installed since Netlify uses Git. Please install Git from this website unless you have already installed: https://git-scm.com/downloads
 2. Python must be installed to use Flask. Please install Python 3.11.2 from this website unless you have already installed: https://www.python.org/downloads/

## How to test this software

* If you have decided to run the software in your local terminal, please move to the right folder and then enter the following:
```
python3 app.py
```
The following (perhaps the port number can differ from this) will appear. 
```
 * Serving Flask app 'app' (lazy loading)
 * Environment: production
   WARNING: This is a development server. Do not use it in a production deployment.
   Use a production WSGI server instead.
 * Debug mode: on
 * Running on http://127.0.0.1:5000/ (Press CTRL+C to quit)
 * Restarting with stat
 * Debugger is active!
 * Debugger PIN: 749-499-479
```
* Now, you can test various functionalities and non-functional requirements. 
* Here is the URL for viewing and reporting a list of bugs: https://github.com/Pingumaniac/Blockchain_Voting_System/issues

## Bug tracking

* All users can view and report a bug in "GitHub Issues" of our repository. 
