ISSUE TRACKING SYSTEM
----------------------
We develop an issue tracking system which helps in keeping track of the issues generated while working on a project. These issues are created only by the authentic users or the admin. The issues are ordered by the date they were created on. The details regarding individual issues are stored and further these can be edited and deleted only by users and admin who have access to perform the operations on the system. Others can only view the list of issues and their details.


We have used the following technologies to create the project:
1.Language:Python3.4
2.Server side framework:Django1.9.0
3.UI framework: Bootstrap
4. Database: SQLite version 3


Steps to view the application
------------------------------
1.First enter into the directory IssueTracking
$ cd IssueTracking

2. Setting up a virtal environment named myvenv to work
$ python3 -m venv myvenv

3.Next we activate a virtual environment, myvenv to work on django
$ source myvenv/bin/activate

4.We need to install django through pip in this virtal environment
For installing pip on linux type the following command
$ python -m pip install -U --force-reinstall pip

For installing django through pip type the following command
$ pip install django~=1.9.0

5.Next we migrate our model to create tables for models in our database
$ python manage.py makemigrations blog
$ python manage.py migrate blog

6.After that we run the server
$ python manage.py runserver
Note: Do not close the terminal as the server is running. Press Ctrl^C to stop the server

7.Finally we go to our browser and enter the following URL to see our application
  http://127.0.0.1:8000

Here we are displayed with a list of issues. Clicking on individual issue gives details about them.

8.We can attain admin privileges and create more users and posts directly for our application. We can view admin page by typing the following URL on our browser.
 http://127.0.0.1:8000/admin

Here we can log in using the below username and password
username:admin
password:datoin@123

Or you can create your own admin and password
$ python manage.py createsuperuser

Here in admin page you further add users and create username and password for users, to make them authentic for the website.

9. We can log in using username and password by clicking on login option at the top right of header and then we can add,edit or remove issues by clicking on them. 
For example:
username:user0001
password:user@pwd

10.To add new issues we can click on new issues and type in the details and click on Save to save the data.

We can click on ISSUE TRACKER logo to view the issue list any time.

 

--THANK YOU--
