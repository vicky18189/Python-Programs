import fresh_tomatoes
import media 

toy_story = media.Movie("Toy Story",
                        "A story of a boy and his toys that came to life",
                        "https://upload.wikimedia.org/wikipedia/en/thumb/1/13/Toy_Story.jpg/220px-Toy_Story.jpg",
                        "https://youtu.be/0PmoiC8ensA")

avatar = media.Movie("Avatar",
                    "A marine on an alien planet",
                    "https://upload.wikimedia.org/wikipedia/en/thumb/d/d6/Avatar_%282009_film%29_poster.jpg/220px-Avatar_%282009_film%29_poster.jpg",
                    "https://youtu.be/5PSNL1qE6VY")

james_bond = media.Movie("James Bond",
                        "A secret agent on a mission to save the world",
                        "https://upload.wikimedia.org/wikipedia/en/2/2d/Quantum_of_Solace_-_UK_cinema_poster.jpg",
                        "https://youtu.be/N_gD9-Oa0fg")

avengers = media.Movie("Avengers", 
                        "A team of super-heroes",
                        "https://upload.wikimedia.org/wikipedia/en/8/8a/The_Avengers_%282012_film%29_poster.jpg",
                        "https://youtu.be/eOrNdBpGMv8")

iron_man = media.Movie("Iron Man",
                        "A rich Scientist in a platinum full body suit",
                        "https://upload.wikimedia.org/wikipedia/en/0/02/Iron_Man_%282008_film%29_poster.jpg",
                        "https://youtu.be/8hYlB38asDY")

hunger_games = media.Movie("Hunger Games",
                        "A real reality show",
                        "https://upload.wikimedia.org/wikipedia/en/4/42/HungerGamesPoster.jpg",
                        "https://youtu.be/mfmrPu43DF8")

movies = [toy_story, avatar, james_bond, avengers, iron_man, hunger_games]
fresh_tomatoes.open_movies_page(movies)