import webbrowser


class Movie():

    """A Movie class.

    Parameters
    ----------
    title : string
        The movie title.
    duration : int
        The duration of the movie in minutes.
    movie_storyline : string
        A short storyline about the movie.
    poster_image : string
        A link to a cover image of the movie.
    trailer_youtube : string
        A link to the youtube trailer of the movie.

    Attributes
    ----------
    VALID_RATINGS : array of strings representing the ratings

    """

    VALID_RATINGS = ["G", "PG", "PG-13", "R"]

    def __init__(self, title, duration, movie_storyline, poster_image,
                 trailer_youtube):

        self.title = title
        self.duration = duration
        self.storyline = movie_storyline
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_youtube

    def show_trailer(self):
        # Opens the default browser and launches the site with the given url
        webbrowser.open(self.trailer_youtube_url)
