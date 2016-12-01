import webbrowser


class Video():
    def __init__(self, title, duration):
        self.title = title
        self.duration = duration


class Movie(Video):

    """
    Movie class constructor.
    Creates an instance of this class and sets its instance variables.

    Parameters
    ----------
    title : string
        The movie title.
    duration : int
        The duration of the movie in minutes.
    movie_storyline : string
        A short storyline about the movie.
    poster_image : string
        A link to the image of the movie.
    trailer_youtube : string
        A link to the youtube trailer of the movie.
    """

    VALID_RATINGS = ["G", "PG", "PG-13", "R"]

    def __init__(self, title, duration, movie_storyline, poster_image,
                 trailer_youtube):

        Video.__init__(self, title, duration)
        self.storyline = movie_storyline
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_youtube

    def show_trailer(self):
        webbrowser.open(self.trailer_youtube_url)


class TvShow(Video):

    """This is a TvShow class."""

    def __init__(self, title, duration, season, episode, the_station):
        Video.__init__(self, title, duration)
        self.episode = episode
        self.season = season
        self.station = the_station
