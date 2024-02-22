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
3. Install project specific packages:
   ```console
   pip install -r requirements.txt
   ```
   or
   ```console
   python3 -m pip install -r requirements.txt
   ```
4. Create images folder:
   ```console
   mkdir images
   ```
5. Apply migrations:
   ```console
   python3 manage.py makemigrations
   ```
   and then
   ```console
   python3 manage.py migrate
   ```
6. Create superuser:
   ```console
   python3 manage.py createsuperuser
   ```
7. Run server with:
  ```console
   python3 manage.py runserver
   ```
  or for HTTPS server:
  ```console
   python3 manage.py runsslserver
   ```
8. Go to [admin page](http://localhost:8000/admin) or [https admin page](https://localhost:8000/admin) to create normal users. Create two users and head to [login page](http://localhost:8000/login) or [https](https://localhost:8000/login) to log in. Create couple of images for each user to test the app.
9. To see all branches use
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


  Please note that each problem has its own branch in the project! 

 

## FLAW 1: Broken access control: 

[Problem](https://github.com/SPitkanen/cybersecurityproject/blob/4d626ec29ff30d07443c583c4df2b5a7cba854e0/myApp/views.py#L48) on branch brokenAccessControl in myApp/views.py on lines 48 – 51 you can see an example of broken access control. Users can type siteUrl/delete/itemNumberToDelete into the search bar, for example localhost:8000/delete/1 and hit enter to delete any picture that any other user has posted on the site. Normally, logged users can only alter the data that they have posted on the site. If the user views the page, they don't have the option to delete anything, since this has been taken care of in the front end. However, since the backend does not check if the user has rights to the picture, any request can be made to delete pictures. One way for the user to get image id is to open dev tools and inspect the wanted picture and look for description id number. You can also note that making requests only works for logged users, since delete_picture does check if the request maker has logged in. You can test this by making a DELETE request to the same URL for example on Postman without giving any credentials.  

To fix the issue remove comments from the if-clause in myApp/views.py delete_picture on lines 48 and 49 and the second picture.delete() function on line 51. Now the backend checks if the request was made by the user who created the picture and only then deletes it. 

## FLAW 2: Cryptographic failure: 

[Problem](https://github.com/SPitkanen/cybersecurityproject/blob/662c249ea6b19724505721e9963967f13ac6f931/fakeGram/settings.py#L35) The app can be used with or without https protocol. On cryptographicFailure branch sslserver option has been commented in file fakeGram/settings.py INSTALLED_APPS and is not in use. This means that all traffic between client and server is unsecure, and all traffic, including credentials and other sensitive information can be read as plain text. To fix this problem uncomment the sslserver line in INSTALLED_APPS on line 35 and start the server with command ‘python3 manage.py runsslserver’. This enables secure HTTPS protocol to be used between client and server. If runsslserver line is commented, ‘python3 manage.py runserver’ can be used to start the server, but all traffic will be unencrypted. 

 

## FLAW 3: Injection: 

[Problem](https://github.com/SPitkanen/cybersecurityproject/blob/f0a24e9ba5f5c7877bc737a195efd27adc73a232/myApp/views.py#L62) on branch injection sql injection is possible by updating the description (click on your pictures description and press enter when ready). For example, type in: test’; DELETE from myApp_picture where id = 1; This will delete the picture with id 1 and also deletes descriptions from all the other pictures. To fix this, go to fakeGram/myApp/views.py update_description and comment or remove the try-except clause on lines 63-70. After this uncomment the lines 72 and 73. 

The flaw is caused by giving the parameters directly to the query without any sanitation and using the default cursor with executescript function. Executescript allows the execution of many sql queries at once, which in turn allows the attacker to type in and execute as many queries as they feel like. This flaw could be also partially prevented by using the cursor provided by Django, which blocks executing multiple statements. 

## FLAW 4: Insecure design: 

[Problem](https://github.com/SPitkanen/cybersecurityproject/blob/aafe772b3265360d4b2efae4627a0b75ff4ce1bd/fakeGram/settings.py#L36) on branch insecureDesign you can find an example of an app which does not limit the number of login attempts into the app. This means that an attacker could try to brute force themselves in trying all possible username password combinations. To fix this, uncomment all of the following lines in fakeGram/settings.py: Line 36 in INSTALLED_APPS, 54 in MIDDLEWARE, line 131 in AUTHENTICATION_BACKEND and lines 136-138. The app uses ‘Axes’ package to manage login attempts within the app by introducing limits and cooloff times. You can manage these on lines 136 -138. AXES_FAILURE_LIMIT limits the login attempt amounts, AXES_COOLOFF_TIME sets the cooloff in hours and AXES_RESET_ON_SUCCESS sets the login attempt count to zero when the user succesfully logs in. If you want to reset the login attempt count while you test the app, run python3 manage.py axes_reset on your command line within the project. 

## FLAW 5: Security misconfiguration: 

[Problem](https://github.com/SPitkanen/cybersecurityproject/blob/51596c04be9ce05a5e785c0680914ebce7b59a65/fakeGram/settings.py#L27) one form of security misconfiguration is to send excessive error reports/stack traces to users. On branch securityMisconfiguration fakeGram/settings.py DEBUG is set to True, On line 27 set this value to False to fix this problem. This limits the error messages to more general form. 
