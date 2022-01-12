from Database import Database

from imdb import IMDb

def main():
    #database instance
    db = Database()

    # create an instance of the IMDb class
    ia = IMDb()

    test(ia)

    del db

def test(ia):
    userStr = input("Movie Name: ")

    movies = ia.search_movie(userStr)
    id = movies[0].movieID

    series = ia.get_movie(id)
    genre = series.data['genres']

    print(genre)

if __name__ == "__main__":
    main()