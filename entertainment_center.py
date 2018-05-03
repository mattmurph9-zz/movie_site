import media
import fresh_tomatoes

toy_story = media.Movie("Toy Story",
                        "Toys come alive and get into trouble", 
                        "https://images-na.ssl-images-amazon.com/images/I/91q0UP6%2BUTL._SY450_.jpg",
                        "https://www.youtube.com/watch?v=KYz2wyBy3kc")

jurassic_park = media.Movie("Jurassic Park",
                        "Dinosaurs come alive and get into trouble", 
                        "https://images-na.ssl-images-amazon.com/images/I/41P-6BnVLbL._SY450_.jpg",
                        "https://www.youtube.com/watch?v=QWBKEmWWL38")

goonies = media.Movie("The Goonies",
                        "Children get into trouble", 
                        "https://images-na.ssl-images-amazon.com/images/I/91bHRU1T0VL._SY450_.jpg",
                        "https://www.youtube.com/watch?v=hJ2j4oWdQtU")

movie_list = [toy_story, jurassic_park, goonies]

fresh_tomatoes.open_movies_page(movie_list)

