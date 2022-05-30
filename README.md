#Description
This project is a simple application to track all of the movies you have watched. You can search for movies and add them to your watched movies list. The watched movies list contains basic information about the movie, as well as a rating given by the user. The user can remove or edit information about a movie in the watched list by double clicking it. To sort the watched list by a category click the title button. Lastly, there is a login system for security and keeping multiple profiles.

#Dependencies & Requirements
- python3: https://www.python.org/downloads/
- tkinter: (inluded in python)
- IMDBbPY: https://pypi.org/project/IMDbPY/
- mysqlclient: https://pypi.org/project/mysqlclient/

You will also need to your own mysql server to run the application. You need to put the information of your own server in the src/Database.py file from lines 9-12. If you do not already have a mysql server to use the following is a good resource to get you started: https://dev.mysql.com/doc/mysql-getting-started/en/

Optional:
If you want to compile the project into an application you need to install pyinstaller: https://pyinstaller.org/en/stable/installation.html


#How To Run
Run the following command in the movie-tracker directory: 
    python3 src/Main.py

If you want to compile into application run the following in the movie-tracker directory:
    pyinstaller --onefile --noconsole --name=movie-tracker src/Main.py
The application (movie-tracker.app) will be in a newly created dist directory in the project. Double click the application to run it (it might take a second to launch). This app can be removed from the folder and put anywhere on your machine.