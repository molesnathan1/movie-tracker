import MySQLdb

class Database:
    db = None
    cur = None

    #connects to the database ad
    def __init__(self):
        self.db = MySQLdb.connect(host="localhost",
                     user="root",
                     passwd="4563",
                     db="MovieTracker")

        self.cur = self.db.cursor()
        # self.deleteTables()
        self.createTables()

    #decunstructor that closes the connection to the database
    def __del__(self):
        self.db.close()
    
    #creates all tables in the database
    def createTables(self):
        # sql_file = open("schema.sql", "r")
        # sql_string = sql_file.read()
        # sql_file.close()
        sql_string = """
            CREATE TABLE IF NOT EXISTS Users(
                username varchar(32),
                password varchar (32),
                firstname varchar(32),
                lastname varchar(32),
                PRIMARY KEY (username)
            );

            CREATE TABLE IF NOT EXISTS Movies(
                imdbID int,
                title varchar(32),
                genre varchar(32),
                yearMade int,
                PRIMARY KEY (imdbID)
            );

            CREATE TABLE IF NOT EXISTS UsersMovies(
                username varchar(32),
                movieID int,
                rating int,
                dateAdded datetime,
                FOREIGN KEY (username) REFERENCES Users(username),
                FOREIGN KEY (movieID) REFERENCES Movies(imdbID),
                PRIMARY KEY (username, movieID)
            ); 
        """
        self.cur.execute(sql_string)

    #drop all tables in the database
    def deleteTables(self):
        delete_statement = """
            DROP TABLE IF EXISTS UsersMovies;
            DROP TABLE IF EXISTS Users;
            DROP TABLE IF EXISTS Movies;"""

        self.cur.execute(delete_statement)

    #executes and commits a given sql statement
    def exe(self, statement):
        self.cur.execute(statement)
        result = self.cur.fetchall()
        self.cur.execute("COMMIT;")
        return result