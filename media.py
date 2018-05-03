import fresh_tomatoes
import webbrowser

class Movie():
    
    def __init__(self, name, description, poster, trailer):
        self.title = name
        self.storyline = description
        self.poster_image_url = poster
        self.trailer_youtube_url = trailer
    
    def show_trailer(self):
        webbrowser.open(self.trailer_youtube_url)
