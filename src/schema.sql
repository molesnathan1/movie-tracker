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
    primaryGenre varchar(32),
    PRIMARY KEY (imdbID)
);

CREATE TABLE IF NOT EXISTS UsersMovies(
    username varchar(32),
    movieID int,
    rating int,
    FOREIGN KEY (username) REFERENCES Users(username),
    FOREIGN KEY (movieID) REFERENCES Movies(imdbID),
    PRIMARY KEY (username, movieID)
);