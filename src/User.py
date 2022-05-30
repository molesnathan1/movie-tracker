class User:

    def __init__(self, db):
        self.loggedUsername = None
        self.loggedPassword = None
        self.loggedFirstname = None
        self.loggedLastname = None
        self.currentUser = None

        self.db = db

    # Checks if username and password match. If successful sets loggeduser's information.
    def login(self, entryUser, entryPass):
        userInfo = self.db.exe("SELECT * FROM Users WHERE (username, password) = ('%s', '%s');" % (entryUser, entryPass))
        if userInfo:
            username = userInfo[0][0]   
            password = userInfo[0][1]
            firstname = userInfo[0][2]
            lastname = userInfo[0][3]
            if entryUser == username and entryPass == password:
                self.loggedUsername = username
                self.loggedPassword = password
                self.loggedFirstname = firstname
                self.loggedLastname = lastname
                return 1
        return 0

    # Checks if username is available. If it is adds the user and sets loggeduser's information.
    def signup(self, entryUser, entryPass, entryFirst, entryLast):
        result = self.db.exe("SELECT * FROM Users WHERE username = '%s';" % (entryUser))
        if not result:
            self.addUser(entryUser, entryPass, entryFirst, entryLast)
            self.loggedUsername = entryUser
            self.loggedPassword = entryPass
            self.loggedFirstname = entryFirst
            self.loggedLastname = entryLast
            return 1
        return 0

    # sets all stored information about the logged user to none
    def logout(self):
        self.loggedUsername = None
        self.loggedPassword = None
        self.loggedFirstname = None
        self.loggedLastname = None

    #adds a user to the database
    def addUser(self, username, password, firstname, lastname):
        self.db.exe("INSERT INTO Users VALUES ('%s', '%s', '%s', '%s');" % (username, password, firstname, lastname))

    #removes a user from the database
    def removeUser(self, db, username):
        db.exe("DELETE FROM Users WHERE username = '%s';" % (username))
            

    


