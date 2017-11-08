import media
import fresh_tomatoes

toy_story = media.Movie("Toy Story",
                        "A story of a boy and his toys",
                        "https://upload.wikimedia.org/wikipedia/en/1/13/Toy_Story.jpg",
                        "https://www.youtube.com/watch?v=KYz2wyBy3kc")
#print (toy_story.storyline)

avatar = media.Movie("Avatar",
                     "A marine on an alien planet",
                     "https://upload.wikimedia.org/wikipedia/en/b/b0/Avatar-Teaser-Poster.jpg",
                     "https://www.youtube.com/watch?v=uZNHIU3uHT4")

#print (avatar.storyline)
#avatar.show_trailer()

inside_out = media.Movie("Inside Out",
                         "Inside Out - Official US Trailer",
                         "https://upload.wikimedia.org/wikipedia/en/0/0a/Inside_Out_%282015_film%29_poster.jpg",
                         "https://www.youtube.com/watch?v=yRUAzGQ3nSY")
#inside_out.show_trailer()

midnight_in_paris = media.Movie("Midnight in paris",
                        "he has taken to touring the city alone",
                        "https://upload.wikimedia.org/wikipedia/en/9/9f/Midnight_in_Paris_Poster.jpg",
                        "https://www.youtube.com/watch?v=BYRWfS2s2v4")
school_of_rock = media.Movie("School of rock",
                             "Overly enthusiastic guitarist Dewey Finn (Jack Black) gets thrown out of his bar band and finds himself in desperate need of work",
                             "https://upload.wikimedia.org/wikipedia/en/1/11/School_of_Rock_Poster.jpg",
                             "https://www.youtube.com/watch?v=3PsUJFEBC74")
ratatouille = media.Movie("ratatouille",
                          "Remy (Patton Oswalt), a resident of Paris, appreciates good food and has quite a sophisticated palate",
                          "https://upload.wikimedia.org/wikipedia/en/5/50/RatatouillePoster.jpg",
                          "https://www.youtube.com/watch?v=c3sBBRxDAqk")

movies = [toy_story, avatar, inside_out, midnight_in_paris, school_of_rock, ratatouille]
#fresh_tomatoes.open_movies_page(movies)
#print (media.Movie.VALID_RATINGS)
#print (media.Movie.__doc__)
print (media.Movie.__name__)
print (media.Movie.__module__)