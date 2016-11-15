import webbrowser

# The Movie class defines movie objects
class Movie():
    """The Movie class creates instances of movie objects"""
    VALID_RATINGS = ['G', 'PG', 'PG-13', 'R']
    def __init__(self, title, storyline, poster, trailer_url):
        self.title = title
        self.storyline = storyline
        self.poster_image_url = poster
        self.trailer_youtube_url = trailer_url

    # Shows the trailer for the movie
    def show_trailer(self):
        webbrowser.open(self.trailer_url)
