from imdb import IMDb
from sqlalchemy.sql.functions import user

class Movies:
    ia = None

    def __init__(self):
        self.ia = IMDb()

    #searches for and displays movies based userinput, returns results of search
    def find(self):
        userStr = input("\nsearch movie: ")
        movies = []

        if userStr == "":
            return movies
        else:
            movies = self.ia.search_movie(userStr)

            for i in range(0,10):
                print("%d. %s (%s)" % (i + 1, movies[i], movies[i]['year']))

            return movies 

    #user selects a movie from a search, returns selected movie
    def selectMovie(self, movies):
        userChoice = input("select a movie: ")
        movie = None
        if 1 <= int(userChoice) <= 10:
            movie = movies[int(userChoice) - 1]
        else:
            print("NO MOVIE SELECTED: exiting")
        return movie

    #searches for a movie and selects the first option in the query, return the movie
    def quickFind(self):
        userStr = input("\nquick search movie: ")
        movies = []

        if userStr == "":
            return movies
        else:
            movies = self.ia.search_movie(userStr)
            return movies[0]

    #gets and returns a list of the wanted info of a movie
    def getInfo(self, movie):  
        self.ia.update(movie)
        info = []
        info.append(movie.movieID)
        info.append(movie['title'])
        info.append(movie['genre'])
        return info
        
    #performs a search and allows user to select a movie, gets info on the movie
    def search(self):
        info = []
        movies = self.find()
        if movies: 
            movie = self.selectMovie(movies)
            if movie:
                info = self.getInfo(movie)
                return info

    #performs a quick search for a movie, gets the info of the movie
    def quickSearch(self):
        info = []
        movie = self.quickFind()
        if movie:
            info = self.getInfo(movie)
            return info

    def addMovie(self, db, id, title, genre):
        db.exe("INSERT INTO Movies VALUES(%d, '%s', '%s');" % (id, title, genre))

    def addUserMovie(self, db, username, id, rating):
        db.exe("INSERT INTO UsersMovies VALUES('%s', %d, %d);" % (username, id, rating))

    def removeUserMovie(self, db, username, id, rating):
        db.exe("DELETE FROM UsersMovies WHERE (username, movieID) = ('%s', %d);" % (username, id))

    def newUserMovie(self, db, username):
        info = self.search()
        if info:
            id = int(info[0])
            title = info[1]
            primaryGenre = info[2][0]

            results = db.exe("SELECT * FROM Movies WHERE imdbID = '%s';" % (id))
            if results:
                id = results[0][0]
                rating = self.getRating
                self.addUserMovie(db, username, id, rating)
            else:
                self.addMovie(db, id, title, primaryGenre)
                rating = self.getRating
                self.addUserMovie(db, username, id, rating)

    def getRating(self):
        userStr = input("Movie Rating: ")
        rating = int(userStr)
        return rating

    def newUserMovieQuick(self, db, username):
        info = self.quickSearch()

        if info:
            id = int(info[0])
            title = info[1]
            primaryGenre = info[2][0]

            results = db.exe("SELECT * FROM Movies WHERE imdbID = %d;" % (id))
            if results:
                id = results[0][0]
                rating = self.getRating()
                self.addUserMovie(db, username, id, rating)
            else:
                self.addMovie(db, id, title, primaryGenre)
                rating = self.getRating()
                self.addUserMovie(db, username, id, rating)

    def viewUserMovie(self, db, username):
        results = db.exe("""
                SELECT * 
                FROM Movies 
                WHERE imdbID IN (SELECT movieID 
                                    FROM UsersMovies 
                                    WHERE username = '%s');
            """ % (username))
        ratings = db.exe("SELECT rating FROM UsersMovies WHERE username = '%s';" % (username))
        
        print("\nMY WATCHED MOVIES")
        i = 0
        for m in results:
            i += 1
            rating = ratings[i - 1][0]
            print("%d. %s (%d)" % (i, m[1], rating))
        return results

    def selectRemoveMovie(self, db, username):
        movies = self.viewUserMovie(db, username)

        userStr = input("select movie to remove: ")
        
        if userStr == "":
            print("EXITING")
        else:
            userNum = int(userStr) - 1
            if userNum in range(0, len(movies)):
                id = int(movies[userNum][0])
                title = movies[userNum][1]
                self.removeUserMovie(db, username, id)
                print("REMOVED %s FROM WATCHED LIST" % (title))
        

