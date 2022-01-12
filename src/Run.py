from Database import Database
from Movies import Movies
from Users import Users

def main():
    #database instance
    db = Database()
    movies = Movies()
    users = Users()

    # movies.quickSearch()
    # users.addUser(db, "example", "bob", "bob")
    users.newUser(db)

    del db
    del movies
    del users


if __name__ == "__main__":
    main()