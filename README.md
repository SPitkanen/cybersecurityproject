# Introduction
This is the project for University of Helsinki MOOC course Cyber Security Base 2024. The project contains the five most common OWASP flaws on five separate branches.

## Installation guide
To install the project:
1. Navigate to your preferred directory and run the command:
   ```console
   git clone git@github.com:SPitkanen/cybersecurityproject.git
   ```
2. Go to the project  by using:
   ```console
   cd cybersecurityproject
   ```
3. Create virtual env:

   macOs/Linux:
   ```console
   python3 -m venv venv
   ```
   Windows:
   ```console
   py -m venv env
   ```
5. Activate virtual env:
   
   macOs/Linux:
   ```console
   source venv/bin/activate
   ```
   Windows:
   ```console
   .\env\Scripts\activate
   ```
6. Install project specific packages:
   ```console
   pip install -r requirements.txt
   ```
   or
   ```console
   python3 -m pip install -r requirements.txt
   ```
7. Create images folder:
   ```console
   mkdir images
   ```
8. Apply migrations:
   ```console
   python3 manage.py makemigrations
   ```
   and then
   ```console
   python3 manage.py migrate
   ```
9. Create superuser:
   ```console
   python3 manage.py createsuperuser
   ```
10. Run server with:
  ```console
   python3 manage.py runserver
   ```
  or for HTTPS server:
  ```console
   python3 manage.py runsslserver
   ```
10. Go to [admin page](http://localhost:8000/admin) or [https admin page](https://localhost:8000/admin) to create normal users. Create two users and head to [login page](http://localhost:8000/login) or [https](https://localhost:8000/login) to log in. Create couple of images for each user to test the app.
11. To see all branches use
  ```console
   git branch
   ```
  or
  ```console
   git branch -a
   ```
  use 
  ```console
   git checkout <branchName>
   ```
  to work on the branch. The branches are named after the problem they present and solve.
