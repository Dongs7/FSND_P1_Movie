class Movie():
    """ This class stores movie information """
    
    def __init__(self, title, story,poster_url,trailer_url,rating, year):
        """Initiate the Movie class with relevant attributes"""
        
        self.title = title
        self.story = story
        self.poster_url = poster_url
        self.trailer_url = trailer_url
        self.rating = rating
        self.year = year
