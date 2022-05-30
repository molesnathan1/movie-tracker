from Database import Database
from Movies import Movies
from User import User

class System:

    def __init__(self):
        self.db = Database()
        self.movies = Movies(self.db)
        self.user = User(self.db)
        self.app = App()

    def __del__(self):
        del self.user
        del self.movies
        del self.db