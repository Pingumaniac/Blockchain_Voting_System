# Blockchain_Voting_System
CS 6381 Distributed Systems Principles Final Project

## About Members and Roles

#### Young-jae Moon
* M.Sc. in computer science and Engineering Graduate Fellowship recipient at Vanderbilt University (January 2023 - December 2024).
* Email: youngjae.moon@Vanderbilt.Edu

#### Alex Richardson
* M.Sc./Ph.D. in computer science and Engineering Graduate Fellowship recipient at Vanderbilt University.
* Email:

#### Azhar Hasan
* M.Sc./Ph.D. in computer science and Engineering Graduate Fellowship recipient at Vanderbilt University.
* Email:

## Advisor

#### Professor Aniruddha Gokhale
* Professor of Computer Science at Vanderbilt University

## Tools and technologies

### Programming languages and Database Management System (DBMS) used

1. JavaScript (ECMAScript 2023)
2. MySQL (MySQL Community Edition 8.0.27)
3. Python (3.11.2)

### Frameworks used

1. Bootstrap front-end framework (v5.3)
2. Flask framework (v2.2.3)

### Python libraries and 3rd party packages used

1. Flask-Bootstrap (v3.3.7.1)
2. Gunicorn (v20.1.0)
3. PyMySQL (v1.0.3)
4. WerkZeug (v2.2.3)

## Instructions for checking out the latest stable version

* TBU

## How to build this software

### 1. Please make sure you have downloaded MySQL (v8.0.27).

* Here is the URL for downloading the MySQL installer for Windows: https://dev.mysql.com/downloads/installer/
* Here is the URL that shows the instructions to install MySQL on macOS: https://dev.mysql.com/doc/mysql-osx-excerpt/5.7/en/osx-installation.html 

### 2. Install the following python packages using pip in the terminal:

```
pip3 install flask 
pip3 install Flask-Bootstrap
pip3 install gunicorn
pip3 install PyMySQL
pip3 install Werkzeug
```

### 3. Deployment method

#### We will use Heroku to deploy the Flask. Note that:
 1. Git must be installed since Heroku uses Git. Please install Git from this website unless you have already installed: https://git-scm.com/downloads
 2. Python must be installed to use Flask. Please install Python 3.11.2 from this website unless you have already installed: https://www.python.org/downloads/

#### To install Heroku,
 1. Open the Heroku website. Here is the link for the Heroku website: https://www.heroku.com/
 2. Sign up a Heroku account.
 3. Install Heroku command-line interface (CLI) in your Terminal by following the instructions from this website: https://devcenter.heroku.com/articles/heroku-cli
 
 #### To use Heroku for deploying our application,
1. Make sure you have already installed Flask and Gunicorn. Check "How to build software" section to refer the installation processes for each of them.
2. Refer "Instructions for checking out the latest stable version" to download all the files needed to build this software.
3. Open the terminal and move to the folder directory which contains all the files for this project.
4. Login to your Heroku account in the terminal.
  ```
 heroku login
 ```
5. Use Procfile, requirements.txt and runtime.txt given in the file.
6. Go to Heroku website again and create an application (name: mastersql).
7. Clone the repository using Git.  
 ```
 heroku git:clone -a Blockchain_Voting_System
 ```
8. Now a folder named 'simayi' has been created. Inside this folder put all the files needed to deploy this project. 
9. Next, move to this folder in the terminal.
 ```
 cd Blockchain_Voting_System
 ```
10. Then, input the following in the terminal:
 ```
 heroku git:remote -a "Simayi"
 git add .
 git commit -am "type whatever you wanna say here"
 git push heroku HEAD:master
```
11. If the following steps run successfully, the website URL will be printed in the console. 
```
https://simayi.herokuapp.com/
```

## How to test this software

* TBU
* Now, you can test various functionalities and non-functional requirements. 

## Bug tracking

* All users can view and report a bug in "GitHub Issues" of our repository. 
