class Users:
    currentUser = None

    #checks if users inputted passwrod is correct
    def checkPassword(self, db, password):
        inputPassword = input("password: ")
        if inputPassword == "":
            return -1
        if inputPassword == password:
            return 1
        else:
            print("INCORRECT PASSWORD")
            return 0

    #checks if inputted username exists, if it does returns a tuple of its info 
    def checkUsername(self, db):
        username = input("\nusername: ")

        #exists recursive function
        if username == "":
            return

        #checks if username exists
        result = db.exe("SELECT * FROM Users WHERE username = '%s';" % (username))

        #if username doesnt exists ask for name and return info
        if result:
            return result
        else:
            print("USER DOES NOT EXIST")
            self.checkUsername(db)

    #gets a unique username from user
    def getNewUsername(self, db):
        username = input("\nusername: ")

        #exists recursive function
        if username == "":
            return

        #checks if username exists
        result = db.exe("SELECT * FROM Users WHERE username = '%s';" % (username))

        #if username doesnt exists ask for name and return info
        if not result:
            return username
        else:
            print("the selected username already exists")
            self.getUserInfo(db)
    
    #gets info from the user for a new login
    def getUserInfo(self, db):
        username = self.getNewUsername(db)
        info = []

        if username:
            password = input("password: ")
            firstname = input("firstname: ")
            lastname = input("lastname: ")
            info = [username, password, firstname, lastname]

        return info

    #adds a user to the database
    def addUser(self, db, username, password, firstname, lastname):
        db.exe("INSERT INTO Users VALUES ('%s', '%s', '%s', '%s');" % (username, password, firstname, lastname))

    #creates a new user
    def newUser(self, db):
        info = self.getUserInfo(db)
        if info:
            self.addUser(db, info[0], info[1], info[2], info[3])
            return 1

        return 0

    #removes a user from the database
    def removeUser(self, db, username):
        db.exe("DELETE FROM Users WHERE username = '%s';" % (username))

