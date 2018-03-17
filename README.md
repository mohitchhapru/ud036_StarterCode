Movie Trailer:
In Movie Trailer, poster and title of the movies are displayed as tiles on the web page, on clicking poster of the movie, an online YouTube video containing movie trailer is played. Python foundation is used to develop a user defined data type i.e. Class Movie. Instance/Objects are created and initialized with user defined inputs and passed to web page.

Below are the files in the project:
•	media.py contain __init__ (constructor) with below parameters:
o	self: this is a default parameter. 
o	movie_title: This field contains the name of the movie 
o	movie_poster_image: This field contains the URL of the movie poster
o	movie_youtube_url: This field contains the YouTube URL of the movie trailer
•	movie_trailer.py: This file initializes multiple instances/object of class Movie with user defined data and combine them in a set of array, now this array is passed as a parameter to the function open_movies_page defined in fresh_tomatoes.py which creates and open the web page with user defined movie tiles and required functionality.
•	fresh_tomatoes.py: This module is called from movie_trailer.py which helps in rendering HTML content of user defined data.

To Run:
•	Click “Clone and Download” and then Download the Zip file.
•	Unzip the files on local system
•	If Python is not Installed then, download and install python from this URL: https://www.python.org/downloads/
•	After installing Python, right-click on movie_trailer.py and click on 'Edit with IDLE'
•	Now select Run from menu and click 'Run the Module'.
