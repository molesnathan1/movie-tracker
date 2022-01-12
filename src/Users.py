from Database import Database

class Users:
    def getUserInfo(self, db):
        username = input("username: ")

        #exists recursive function
        if username == "":
            return

        #checks if username exists
        result = db.exe("SELECT * FROM Users WHERE username = '%s';" % (username))
        print(result)

        #if username doesnt exists ask for name and return info
        if not result:
            firstname = input("firstname: ")
            lastname = input("lastname: ")
            info = [username, firstname, lastname]
            return info
        else:
            print("the selected username already exists")
            self.getUserInfo(db)

    def addUser(self, db, username, firstname, lastname):
        db.exe("INSERT INTO Users VALUES ('%s', '%s', '%s');" % (username, firstname, lastname))

    def newUser(self, db):
        info = self.getUserInfo(db)
        if info:
            self.addUser(db, info[0], info[1], info[2])

    def removeUser(self, db, username):
        db.exe("DELETE FROM Users WHERE username = '%s';" % (username))

