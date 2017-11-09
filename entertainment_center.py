# -*- coding: utf8 -*-
from media import Movie
import fresh_tomatoes

toy_story = Movie(movie_title = "玩具总动员",
              movie_storyline = "一个男孩的玩具之间的故事",
              poster_image = "https://upload.wikimedia.org/wikipedia"\
              "/en/1/13/Toy_Story.jpg",
              trailer_youtube = "https://www.youtube.com/watch?v=KYz2wyBy3kc")

avatar = Movie(movie_title = "阿凡达",
               movie_storyline = "潘多拉星球上面人类和阿凡达的对抗",
               poster_image = "https://upload.wikimedia.org/wikipedia/"\
               "en/b/b0/Avatar-Teaser-Poster.jpg",
               trailer_youtube = "https://www.youtube.com/watch?v=uZNHIU3uHT4")

inside_out = Movie(movie_title = "头脑特工队",
                 movie_storyline = "脑子里的各种情绪小人的外出冒险",
                 poster_image = "https://upload.wikimedia.org/wikipedia/en/0/0a/"\
                 "Inside_Out_%282015_film%29_poster.jpg",
                 trailer_youtube = "https://www.youtube.com/watch?v=yRUAzGQ3nSY")

midnight_in_paris = Movie(movie_title = "午夜巴黎",
                          movie_storyline = "孤独的夜晚孤独的人，独自游览巴黎",
                          poster_image = "https://upload.wikimedia.org/wikipedia/"\
                          "en/9/9f/Midnight_in_Paris_Poster.jpg",
                          trailer_youtube = "https://www.youtube.com/watch?v=BYRWfS2s2v4")
school_of_rock = Movie(movie_title = "摇滚学校",
                       movie_storyline = "一个摇滚青年和他的学生乐队",
                       poster_image = "https://upload.wikimedia.org/wikipedia/"\
                       "en/1/11/School_of_Rock_Poster.jpg",
                       trailer_youtube = "https://www.youtube.com/watch?v=3PsUJFEBC74")
ratatouille = Movie(movie_title = "美食总动员",
                    movie_storyline = "一个倒霉厨师和他的老鼠老师",
                    poster_image = "https://upload.wikimedia.org/wikipedia/"\
                    "en/5/50/RatatouillePoster.jpg",
                    trailer_youtube = "https://www.youtube.com/watch?v=c3sBBRxDAqk")

movies = [toy_story, avatar, inside_out,
          midnight_in_paris, school_of_rock, ratatouille]

fresh_tomatoes.open_movies_page(movies)