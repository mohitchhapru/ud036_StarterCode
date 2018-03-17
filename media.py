class Movie:  # Class Movie is a user defined data structure to combine details of a movie
    # Constructor with paramaeters
    def __init__(self, title, poster_image_url, trailer_youtube_url):
        self.title = title  #: This field contains the name of the movie
        self.poster_image_url = poster_image_url  #: This field contains the URL of the movie poster
        self.trailer_youtube_url = trailer_youtube_url  #: This field contains the YouTube URL of the movie trailer
