from imdb import IMDb

class Movies:
    ia = None

    def __init__(self):
        self.ia = IMDb()

    def find(self):
        userStr = input("\nsearch movie: ")
        movies = self.ia.search_movie(userStr)

        for i in range(0,10):
            print("%d. %s (%s)" % (i + 1, movies[i], movies[i]['year']))

        return movies 

    def selectMovie(self, movies):
        userChoice = input("select a movie: ")
        movie = None
        if 1 <= int(userChoice) <= 10:
            movie = movies[int(userChoice) - 1]
        else:
            print("NO MOVIE SELECTED: exiting")
        return movie

    def quickFind(self):
        userStr = input("\nquick search movie: ")
        movies = self.ia.search_movie(userStr)
        return movies[0]

    def getInfo(self, movie):  
        self.ia.update(movie)
        info = []
        info.append(movie.movieID)
        info.append(movie['title'])
        info.append(movie['genre'])
        return info
        
    def search(self):
        movies = self.find()
        movie = self.selectMovie(movies)
        info = self.getInfo(movie)
        print(info)

    def quickSearch(self):
        movie = self.quickFind()
        info = self.getInfo(movie)
        print(info)
