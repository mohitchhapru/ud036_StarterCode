import media
import fresh_tomatoes

inception = media.Movie("Inception",
                        "https://images-na.ssl-images-amazon.com/images/I/81AC63tB+ZL._RI_.jpg",
                        "https://youtu.be/d3A3-zSOBT4")

the_imitation_game = media.Movie("The Imitation Game",
                                 "https://i.ytimg.com/vi/UK_LJvgfAf8/movieposter.jpg",
                                 "https://youtu.be/S5CjKEFb-sM")

titanic = media.Movie("Titanic",
                      "http://t0.gstatic.com/images?q=tbn:ANd9GcQhYjUIu2o5v5u3rfJpCq5Cz0Q9WK--XdYxai_N2d0ImohPiIOp",
                      "https://youtu.be/2e-eXJ6HgkQ")

death_wish = media.Movie("Death Wish",
                         "http://t1.gstatic.com/images?q=tbn:ANd9GcQ7l9Mp6mdm0UBcFddU11U87KgkFz7Mf1lwCiGZMrP9_AcJEl6S",
                         "https://youtu.be/v_I4zqC7GN8")

tomb_raider = media.Movie("Tomb Raider",
                          "http://t1.gstatic.com/images?q=tbn:ANd9GcQGBx-FI1Xp1Xk9raKVhCrW2pj-vBUpbjfY5liEfDmU2DzKV-Uf",
                          "https://youtu.be/8ndhidEmUbI")

movies = [inception,the_imitation_game,titanic,death_wish,tomb_raider]
fresh_tomatoes.open_movies_page(movies)
