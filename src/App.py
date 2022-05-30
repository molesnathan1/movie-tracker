import tkinter as tk

class Window:

    def signin_window(self):
        self.frame.destroy()
        self.app = Signin(self.master, self.system)

    def login_window(self):
        self.frame.destroy()
        self.app = Login(self.master, self.system)

    def signup_window(self):
        self.frame.destroy()
        self.app = Signup(self.master, self.system)

    def menu_window(self):
        self.frame.destroy()
        self.app = Menu(self.master, self.system)

    def add_window(self, movie):
        self.frame.destroy()
        self.app = Add(self.master, self.system, movie)

    def edit_window(self, movieTuple):
        self.frame.destroy()
        self.app = Edit(self.master, self.system, movieTuple)


class Signin(Window):
    def __init__(self, master, system):
        self.system = system
        self.master = master
        self.master.title("Movie Tracker")
        self.frame = tk.Frame(self.master)

        # login button
        self.loginButton = tk.Button(self.frame, text = 'Login', width = 25, command = self.login_window)
        self.loginButton.grid(row=1,column=1)

        # signup button
        self.signupButton = tk.Button(self.frame, text = 'Signup', width = 25, command = self.signup_window)
        self.signupButton.grid(row=2,column=1)

        self.frame.pack()
        


class Login(Window):
    def __init__(self, master, system):
        self.system = system
        self.master = master
        self.master.title("Login")
        self.frame = tk.Frame(self.master)

        # username label
        self.usernameLabel = tk.Label(self.frame, text = 'Username:') 
        self.usernameLabel.grid(row=1,column=1)
        # username entry
        self.usernameEntry = tk.Entry(self.frame) 
        self.usernameEntry.grid(row=1,column=2)
        self.usernameEntry.focus_force()

        # password label
        self.passwordLabel = tk.Label(self.frame, text = 'Password:') 
        self.passwordLabel.grid(row=2,column=1)
        # password entry
        self.passwordEntry = tk.Entry(self.frame) 
        self.passwordEntry.grid(row=2,column=2)
        self.passwordEntry.config(show="*")
        self.passwordEntry.focus_force()

        # submit button
        self.submitButton = tk.Button(self.frame, text = 'Submit', command = self.check_info)
        self.submitButton.grid(row=3,column=2)

        # cancel button
        self.cancelButton = tk.Button(self.frame, text = 'Cancel', command = self.signin_window)
        self.cancelButton.grid(row=4,column=2)

        self.frame.pack()
        
    # empty field error messsage
    def empty_field(self):
        self.usernameLabel = tk.Label(self.frame, text = 'Fill The Empty Field!') 
        self.usernameLabel.grid(row=0,column=2)

    # incorrect login error message
    def incorrect_login(self):
        self.usernameLabel = tk.Label(self.frame, text = 'Login Does Not Exist!') 
        self.usernameLabel.grid(row=0,column=2)

    # checks if the login information entered is correct. Logs in user if correct
    def check_info(self):
        entryUser = self.usernameEntry.get()
        entryPass = self.passwordEntry.get()
        if not entryUser or not entryPass:
            self.empty_field()
        else:
            if self.system.user.login(entryUser, entryPass) == 1:
                self.menu_window()
            else:
                self.incorrect_login()


class Signup(Window):
    def __init__(self, master, system):
        self.system = system
        self.master = master
        self.master.title("Signup")
        self.frame = tk.Frame(self.master)

        # username label
        self.usernameLabel = tk.Label(self.frame, text = 'Username:') 
        self.usernameLabel.grid(row=1,column=1)
        # username entry
        self.usernameEntry = tk.Entry(self.frame) 
        self.usernameEntry.grid(row=1,column=2)
        self.usernameEntry.focus_force()

        # password label
        self.passwordLabel = tk.Label(self.frame, text = 'Password:') 
        self.passwordLabel.grid(row=2,column=1)
        # password entry
        self.passwordEntry = tk.Entry(self.frame) 
        self.passwordEntry.grid(row=2,column=2)
        self.passwordEntry.focus_force()
        
        # firstname label
        self.firstnameLabel = tk.Label(self.frame, text = 'First Name:') 
        self.firstnameLabel.grid(row=3,column=1)
        # firstname entry
        self.firstnameEntry = tk.Entry(self.frame) 
        self.firstnameEntry.grid(row=3,column=2)
        self.firstnameEntry.focus_force()

        # lastname label
        self.lastnameLabel = tk.Label(self.frame, text = 'Last Name:') 
        self.lastnameLabel.grid(row=4,column=1)
        # lastname entry
        self.lastnameEntry = tk.Entry(self.frame) 
        self.lastnameEntry.grid(row=4,column=2)
        self.lastnameEntry.focus_force()

        # submit button
        self.submitButton = tk.Button(self.frame, text = 'Submit', command = self.check_info)
        self.submitButton.grid(row=5,column=2)

        # cancel button
        self.cancelButton = tk.Button(self.frame, text = 'Cancel', command = self.signin_window)
        self.cancelButton.grid(row=6,column=2)

        self.frame.pack()
        
    # empty field error message
    def empty_field(self):
        self.usernameLabel = tk.Label(self.frame, text = 'Fill The Empty Field!') 
        self.usernameLabel.grid(row=0,column=2)

    # username name is unavailable error message
    def unavailable(self):
        self.usernameLabel = tk.Label(self.frame, text = 'Username Unavailable!') 
        self.usernameLabel.grid(row=0,column=2)

    # gets all entry boxes and checks if the signup info is valid
    def check_info(self):
        entryUser = self.usernameEntry.get()
        entryPass = self.passwordEntry.get()
        entryFirst = self.firstnameEntry.get()
        entryLast = self.lastnameEntry.get()
        if entryUser and entryPass and entryFirst and entryLast:
            if self.system.user.signup(entryUser, entryPass, entryFirst, entryLast):
                self.menu_window()
            else:
                self.unavailable()
        else:
            self.empty_field()

class Menu(Window):

    def __init__(self, master, system):
        self.system = system
        self.master = master
        self.master.title("Menu")
        self.frame = tk.Frame(self.master)

        # name label
        self.nameLabel = tk.Label(self.frame, text = "%s: %s %s" % (self.system.user.loggedUsername, self.system.user.loggedFirstname, self.system.user.loggedLastname))
        self.nameLabel.grid(row=0,column=2,sticky="w")

        # logout button
        self.logoutButton = tk.Button(self.frame, text = 'Logout', command = self.logout)
        self.logoutButton.grid(row=0,column=1)

        # search button
        self.searchButton = tk.Button(self.frame, text = 'Search', command = self.search)
        self.searchButton.grid(row=1,column=3)
        # search entry
        self.searchEntry = tk.Entry(self.frame, width=30) 
        self.searchEntry.grid(row=1,column=2)
        self.searchEntry.focus_force()

        # watch list title label
        self.watchlistLabel = tk.Label(self.frame, text = 'MY WATCHED MOVIES') 
        self.watchlistLabel.grid(row=0,column=4)

        # watch list movie title label
        self.titleButton = tk.Button(self.frame, text = 'Title', command = self.sortTitle) 
        self.titleButton.grid(row=1,column=4)
        # watch list movie title listbox
        self.titleListbox = tk.Listbox(self.frame, height=30, width=25)
        self.titleListbox.grid(row=2, column=4, sticky = 'w')
        self.titleListbox.focus_force()
        self.titleListbox.bind('<Double-1>', self.selectTitle) #when item is double clicked

        # watch list movie genre label
        self.genreButton = tk.Button(self.frame, text = 'Genre', command = self.sortGenre) 
        self.genreButton.grid(row=1,column=5)
        # watch list movie genre listbox
        self.genreListbox = tk.Listbox(self.frame, height=30, width=10)
        self.genreListbox.grid(row=2, column=5, sticky = 'w')
        self.genreListbox.bind('<Double-1>', self.selectGenre) #when item is double clicked
        self.genreListbox.focus_force()

        # watch list movie genre label
        self.yearButton = tk.Button(self.frame, text = 'Year', command = self.sortYear) 
        self.yearButton.grid(row=1,column=6)
        # watch list movie genre listbox
        self.yearListbox = tk.Listbox(self.frame, height=30, width=10)
        self.yearListbox.grid(row=2, column=6, sticky = 'w')
        self.yearListbox.bind('<Double-1>', self.selectYear) #when item is double clicked
        self.yearListbox.focus_force()

        # watch list movie rating label
        self.ratingButton = tk.Button(self.frame, text = 'Rating', command = self.sortRating) 
        self.ratingButton.grid(row=1,column=7)
        # watch list movie rating listbox
        self.ratingListbox = tk.Listbox(self.frame, height=30, width=10)
        self.ratingListbox.grid(row=2, column=7, sticky = 'w')
        self.ratingListbox.bind('<Double-1>', self.selectRating) #when item is double clicked
        self.ratingListbox.focus_force()
        
        self.sortDate()

        self.frame.pack()

    def clearWatchlist(self):
        self.titleListbox.delete(0,'end')
        self.genreListbox.delete(0,'end')
        self.ratingListbox.delete(0,'end')
        self.yearListbox.delete(0,'end')

    def sortTitle(self):
        self.watchlist = self.system.movies.getWatchlist(self.system.user.loggedUsername)
        self.watchlist.sort(key = lambda watchlist: watchlist[1])
        self.update_watchlist()

    def sortGenre(self):
        self.watchlist = self.system.movies.getWatchlist(self.system.user.loggedUsername)
        self.watchlist.sort(key = lambda watchlist: watchlist[2])
        self.update_watchlist()

    def sortYear(self):
        self.watchlist = self.system.movies.getWatchlist(self.system.user.loggedUsername)
        self.watchlist.sort(key = lambda watchlist: watchlist[3])
        self.update_watchlist()    

    def sortRating(self):
        self.watchlist = self.system.movies.getWatchlist(self.system.user.loggedUsername)
        self.watchlist.sort(key = lambda watchlist: watchlist[4])
        self.watchlist.reverse()
        self.update_watchlist()

    def sortDate(self):
        self.watchlist = self.system.movies.getWatchlist(self.system.user.loggedUsername)
        self.update_watchlist()
        
    # logs out the user
    def logout(self):
        self.system.user.logout()
        self.signin_window()

    # displays search results in a listbox
    def search(self):
        userSearch = self.searchEntry.get()
        self.moviesTuple = self.system.movies.search(userSearch)
        

        self.searchListbox = tk.Listbox(self.frame, width=30)
        self.searchListbox.grid(row=2, column=2, sticky="N")
        self.searchListbox.bind('<Double-1>', self.select_search)

        for i in range(0,10):
            self.searchListbox.insert(i, "%s (%d)" % (self.moviesTuple[i], self.moviesTuple[i]['year']))

    # selects a search result and opens the add window with it
    def select_search(self, event):
        selectIndex = self.searchListbox.curselection()[0]
        self.searchListbox.destroy()

        selectedMovie = self.moviesTuple[selectIndex]

        self.add_window(selectedMovie)

    # displays the watch list
    def update_watchlist(self):
        self.clearWatchlist()

        for i in range(0, len(self.watchlist)):
            self.titleListbox.insert(i, "%s" % (self.watchlist[i][1]))
            self.genreListbox.insert(i, "%s" % (self.watchlist[i][2]))
            self.yearListbox.insert(i, "%s" % (self.watchlist[i][3]))
            self.ratingListbox.insert(i,"%s" % (self.watchlist[i][4]))

    # 
    def selectTitle(self, event):
        selectIndex = self.titleListbox.curselection()[0]
        selectedMovie = self.watchlist[selectIndex]

        self.edit_window(selectedMovie)
    
    def selectGenre(self, event):
        selectIndex = self.genreListbox.curselection()[0]
        selectedMovie = self.watchlist[selectIndex]

        self.edit_window(selectedMovie)

    def selectYear(self, event):
        selectIndex = self.yearListbox.curselection()[0]
        selectedMovie = self.watchlist[selectIndex]

        self.edit_window(selectedMovie)

    def selectRating(self, event):
        selectIndex = self.ratingListbox.curselection()[0]
        selectedMovie = self.watchlist[selectIndex]

        self.edit_window(selectedMovie)

class Add(Window):
    def __init__(self, master, system, movie):
        self.system = system
        self.movie = movie
        self.master = master
        self.master.title("Add")

        system.movies.updateMovie(movie)
        self.title = movie['title']
        self.year = movie['year']
        self.genre = movie['genre']
        self.id = int(movie.movieID)

        self.frame = tk.Frame(self.master)

        self.titleLabel = tk.Label(self.frame, text = 'Title: %s' % self.title) 
        self.titleLabel.grid(row=1,column=1)

        self.yearLabel = tk.Label(self.frame, text = 'Year: %s' % self.year) 
        self.yearLabel.grid(row=1,column=2)

        self.genreLabel = tk.Label(self.frame, text = 'Genre: %s' % (self.genre[0]))
        self.genreLabel.grid(row=1,column=2)

        self.ratingLabel = tk.Label(self.frame, text = 'Rating (1-10): ') 
        self.ratingLabel.grid(row=2,column=1)
        
        self.ratingEntry = tk.Entry(self.frame) 
        self.ratingEntry.grid(row=2,column=2)
        self.ratingEntry.focus_force()

        self.submitButton = tk.Button(self.frame, text = 'Cancel', command = self.menu_window)
        self.submitButton.grid(row=3,column=1)

        self.addButton = tk.Button(self.frame, text = 'Add', command = self.add)
        self.addButton.grid(row=3,column=2)

        self.frame.pack()
        

    def empty_field(self):
        self.usernameLabel = tk.Label(self.frame, text = 'Fill The Empty Field!') 
        self.usernameLabel.grid(row=2,column=3)

    def add(self):
        rating = self.ratingEntry.get()
        if rating:
            rating = int(rating)
            if rating >= 1 and rating <=10:
                self.system.movies.newUserMovie(self.system.user.loggedUsername, self.id, self.title, self.genre[0], self.year, rating)
                self.frame.destroy()
                self.menu_window()
            else:
                self.ratingErrorLabel = tk.Label(self.frame, text = 'Choose a rating from 1-10') 
                self.ratingErrorLabel.grid(row=2,column=3)
        else:
            self.empty_field()


class Edit(Window):
    def __init__(self, master, system, movieTuple):
        self.system = system

        self.master = master
        self.master.title("Edit")

        self.id = movieTuple[0]
        self.title = movieTuple[1]
        self.genre = movieTuple[2]
        self.year = movieTuple[3]
        self.rating = movieTuple[4]

        self.frame = tk.Frame(self.master)

        self.titleLabel = tk.Label(self.frame, text = 'Title: %s' % self.title) 
        self.titleLabel.grid(row=1,column=1)

        self.yearLabel = tk.Label(self.frame, text = 'Year: %s' % self.year) 
        self.yearLabel.grid(row=1,column=2)

        self.genreLabel = tk.Label(self.frame, text = 'Genre: %s' % (self.genre))
        self.genreLabel.grid(row=2,column=1)

        self.ratingLabel = tk.Label(self.frame, text = 'Rating:') 
        self.ratingLabel.grid(row=2,column=2)

        self.ratingEntry = tk.Entry(self.frame, width = 10)
        self.ratingEntry.grid(row=2,column=3)
        self.ratingEntry.insert(0,self.rating)
        self.ratingEntry.focus_force()

        self.cancelButton = tk.Button(self.frame, text = 'Cancel', command = self.menu_window)
        self.cancelButton.grid(row=3,column=1)

        self.deleteButton = tk.Button(self.frame, text = 'Delete', command = self.delete)
        self.deleteButton.grid(row=3,column=2)

        self.updateButton = tk.Button(self.frame, text = 'Update', command = self.update)
        self.updateButton.grid(row=3,column=3)

        self.frame.pack()

    def empty_field(self):
        self.errorLabel = tk.Label(self.frame, text = 'Fill The Empty Field!') 
        self.errorLabel.grid(row=2,column=4)

    def update(self):
        rating = self.ratingEntry.get()
        if rating:
            rating = int(rating)
            if rating >= 1 and rating <=10:
                self.system.movies.updateUserMovie(self.system.user.loggedUsername, self.id, rating)
                self.frame.destroy()
                self.menu_window()
            else:
                self.ratingErrorLabel = tk.Label(self.frame, text = 'Choose a rating from 1-10') 
                self.ratingErrorLabel.grid(row=2,column=3)
        else:
            self.empty_field()

    def delete(self):
        self.system.movies.removeUserMovie(self.system.user.loggedUsername, self.id)
        self.menu_window()