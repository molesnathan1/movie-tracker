from Database import Database
from Movies import Movies
from Users import Users

class System:
    loggedUsername = None
    loggedPassword = None
    loggedFirstname = None
    loggedLastname = None

    def __init__(self):
        self.db = Database()
        self.mv = Movies()
        self.us = Users()
        self.home()

    def __del__(self):
        del self.db
        del self.mv
        del self.us

    def home(self):
        print("\n1. Login\n2. Signup")
        selected = input("choose an action: ")

        if selected == '1':
            self.login()
        elif selected == '2':
            self.signup()
        else:
            print("NOT ACCPETED INPUT: please choose enter 1 or 2")
        self.home()


    def login(self):
        userInfo = self.us.checkUsername(self.db)

        username = userInfo[0][0]
        password = userInfo[0][1]
        firstname = userInfo[0][2]
        lastname = userInfo[0][3]

        loggedIn = self.us.checkPassword(self.db, password)

        while (loggedIn == 0):
            loggedIn = self.us.checkPassword(self.db, password)
            if loggedIn == -1:
                break
        
        if loggedIn == 1:
            self.loggedUser = username
            self.loggedPassword = password
            self.loggedFirstname = firstname
            self.loggedLastname = lastname
            print("WELCOME %s %s!" % (firstname, lastname))
            self.actionMenu()
        else:
            print("LOGIN EXITED")
            self.home()

    def signup(self):
        success = self.us.newUser(self.db)
        if success == 1:
            self.actionMenu()
        else:
            self.home()

    def actionMenu(self):
        print("\n1. Search\n2. Quick Search")
        selected = input("choose an action: ")
        if selected == '1':
            self.mv.search()
        elif selected == '2':
            self.mv.quickSearch()
        else:
            print("NOT ACCPETED INPUT: please choose enter 1 or 2")
        self.actionMenu()

