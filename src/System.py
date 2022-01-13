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

        self.loggedUsername = None
        self.loggedPassword = None
        self.loggedFirstname = None
        self.loggedLastname = None

        self.home()

    def __del__(self):
        del self.db
        del self.mv
        del self.us

    #home menu of the system
    def home(self):
        print("\n1. Login\n2. Signup\n3. Exit")
        selected = input("choose an action: ")

        
        if selected == '1':
            self.login()
        elif selected == '2':
            self.signup()
        elif selected == '3':
            print("EXIT\n")
            return
        else:
            print("NOT ACCPETED INPUT: please choose enter 1-3")
            self.home()


    #logs the user into the system
    def login(self):
        userInfo = self.us.checkUsername(self.db)

        #all user info from username query
        if userInfo:
            username = userInfo[0][0]   
            password = userInfo[0][1]
            firstname = userInfo[0][2]
            lastname = userInfo[0][3]

            #checks if password is correct for username
            loggedIn = self.us.checkPassword(self.db, password)
            while (loggedIn == 0):
                loggedIn = self.us.checkPassword(self.db, password)
                if loggedIn == -1:
                    break
            
            #if passwords match login, else return to home
            if loggedIn == 1:
                self.loggedUsername = username
                self.loggedPassword = password
                self.loggedFirstname = firstname
                self.loggedLastname = lastname
                print("WELCOME %s %s! :)" % (firstname, lastname))
                self.actionMenu()
            else:
                self.home()
        else:
            print("LOGIN EXITED")
            self.home()

    #logs the user out of the system
    def logout(self):
        print("GOODBYE %s %s! :(" % (self.loggedFirstname, self.loggedLastname))
        self.loggedUsername = None
        self.loggedPassword = None
        self.loggedFirstname = None
        self.loggedLastname = None
        self.home()

    #signs up a new user
    def signup(self):
        userInfo = self.us.newUser(self.db)
        if userInfo:
            username = userInfo[0]
            password = userInfo[1]
            firstname = userInfo[2]
            lastname = userInfo[3]

            self.loggedUsername = username
            self.loggedPassword = password
            self.loggedFirstname = firstname
            self.loggedLastname = lastname
            self.actionMenu()
        else:
            self.home()

    #menu once a user signed in where action can be performed
    def actionMenu(self):
        print("\n1. Search\n2. Quick Search\n3. Add Movie To Watched Movies\n4. Quick Add Movie To Watched Movies\n5. View My Watched Movies\n6. Remove From Watched Movies\n7. Logout")
        selected = input("choose an action: ")

        if selected == '1':
            self.mv.search()
        elif selected == '2':
            self.mv.quickSearch()
        elif selected == '3':
            self.mv.newUserMovie(self.db, self.loggedUsername)
        elif selected == '4':
            self.mv.newUserMovieQuick(self.db, self.loggedUsername)
        elif selected == '5':
            self.mv.viewUserMovie(self.db, self.loggedUsername)
        elif selected == '6':
            self.mv.selectRemoveMovie(self.db, self.loggedUsername)
        elif selected == '7':
            self.logout()
            return
        else:
            print("NOT ACCPETED INPUT: please choose 1-7")
        
        self.actionMenu()




