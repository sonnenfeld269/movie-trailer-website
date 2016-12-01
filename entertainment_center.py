import media
import fresh_tomatoes

cowspiracy = media.Movie("Cowspiracy", 120, "The Sustainability Secret",
                         "http://tinyurl.com/zawacd8",
                         "https://www.youtube.com/watch?v=nV04zyfLyN4")

tomorrow = media.Movie("Tomorrow", 120, "The world is full of solutions.",
                       "http://tinyurl.com/jsemfar",
                       "https://www.youtube.com/watch?v=NUN0QxRB7e0&t=2s")

a_prophet = media.Movie("A Prophet", 120, "Nineteen year-old Franco-Arab "
                        "Malik El Djebena is just starting his six year"
                        " prison sentence in Brecourt.",
                        "http://tinyurl.com/hyuu5pr",
                        "https://www.youtube.com/watch?v=l69ARbQt-Ko")

bad_santa = media.Movie("Bad Santa", 120, "A miserable conman and his partner "
                        "pose as Santa and his Little Helper to rob "
                        "department stores on Christmas Eve.",
                        "http://tinyurl.com/z7w5pgw",
                        "https://www.youtube.com/watch?v=xQvaoRScND4")

ex_machina = media.Movie("EX MACHINA", 120, "Real science fiction is about "
                         "ideas, which means that real science fiction is"
                         " rarely seen on movie screens, a commercially "
                         " minded canvas that's more at ease with sensation "
                         " and spectacle.", "http://tinyurl.com/hdneqkc",
                         "www.youtube.com/watch?v=XYGzRB4Pnq8")

te_days_later = media.Movie("28 Days Later", 120, "Our weeks after a "
                            "mysterious, incurable virus spreads throughout "
                            "the UK, a handful of survivors try to find "
                            "sanctuary.", "http://tinyurl.com/z6gjqa8",
                            "https://www.youtube.com/watch?v=HEkJAaGhJhQ")

district_9 = media.Movie("District 9", 120, "An extraterrestrial race forced "
                         "to live in slum-like conditions on Earth suddenly "
                         "finds a kindred spirit in a government agent who is "
                         "exposed to their biotechnology.",
                         "http://tinyurl.com/h8ecn9k",
                         "https://www.youtube.com/watch?v=DyLUwOcR5pk")

movies = [cowspiracy, tomorrow, a_prophet, bad_santa, ex_machina,
          te_days_later, district_9]

fresh_tomatoes.open_movies_page(movies)
