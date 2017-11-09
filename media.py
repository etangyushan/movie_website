# -*- coding:utf8 -*-
import webbrowser

#定义一个电影的封装类
class Movie():
    ''' 这个类提供一个存储电影信息的功能 '''

    VALID_RATINGS = ["G", "PG", "PG-13", "R"]
    '''
    Input:
        movie_title：电影名称
        movie_storyline: 电影简介
        poster_image:电影海报
        trailer_youtube:电影的预告片
    '''
    def __init__(self, movie_title, movie_storyline, poster_image, trailer_youtube):
        self.title = movie_title
        self.storyline = movie_storyline
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_youtube

    #显示预告片
    def show_trailer(self):
        webbrowser.open(self.trailer_youtube_url)