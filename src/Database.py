import MySQLdb

class Database:
    db = None
    cur = None

    #constructor that connects to the database and sets it up
    def __init__(self):
        self.db = MySQLdb.connect(host="localhost",
                     user="admin",
                     passwd="angle_4L",
                     db="MovieTracker")

        self.cur = self.db.cursor()
        # self.deleteTables()
        self.createTables()

    #decunstructor that closes the connection to the database
    def __del__(self):
        self.db.close()
    
    #creates all tables in the database
    def createTables(self):
        sql_file = open("schema.sql", "r")
        sql_string = sql_file.read()
        sql_file.close()
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