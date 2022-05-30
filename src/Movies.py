from imdb import IMDb

class Movies:
    imdb = None

    def __init__(self, db):
        self.imdb = IMDb()
        self.db = db

    #searches for and displays movies based userinput, returns results of search
    def search(self, userStr):

        movies = self.imdb.search_movie(userStr)

        return movies

    # adds a movie to the database
    def addMovie(self, id, title, genre, year):
        self.db.exe("INSERT IGNORE INTO Movies VALUES(%d, '%s', '%s', %d);" % (id, title, genre, year))

    # adds a usermovie to the database
    def addUserMovie(self, username, id, rating):
        self.db.exe("INSERT IGNORE INTO UsersMovies VALUES('%s', %d, %d, curdate());" % (username, id, rating))

    def updateUserMovie(self, username, id, rating):
        self.db.exe("UPDATE UsersMovies SET rating = %d WHERE username = '%s' and movieID = %d;" % (rating, username, id))

    # deletes a usermovie from the database 
    def removeUserMovie(self, username, id):
        self.db.exe("DELETE FROM UsersMovies WHERE (username, movieID) = ('%s', %d);" % (username, id))

    # adds a new user and usermovie to the database
    def newUserMovie(self, username, id, title, genre, year, rating):
        self.addMovie(id, title, genre, year)
        self.addUserMovie(username, id, rating)

    # returns list of all information in a users watchlist [(id, title, genre1, genre2, year, rating)]
    def getWatchlist(self, username):
        results = self.db.exe("""
                SELECT * 
                FROM Movies 
                WHERE imdbID IN (SELECT movieID 
                                    FROM UsersMovies 
                                    WHERE username = '%s');
            """ % (username))
        ratings = self.db.exe("SELECT rating FROM UsersMovies WHERE username = '%s';" % (username))
        i = 0
        results = list(results)
        ratings = list(ratings)
        for i in range(len(results)):
            results[i] = results[i] + ratings[i]

        return results

    # updates a movie's information from imdb
    def updateMovie(self, movie):
        self.imdb.update(movie)


        

