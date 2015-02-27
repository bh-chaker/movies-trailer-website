from movies_page import open_movies_page
from movie import Movie

# Create a movies list with trailers of 'The Lord of the Rings trilogy'.
movies = [
            Movie('The Lord of the Rings: The Fellowship of the Ring', 'http://upload.wikimedia.org/wikipedia/en/0/0c/The_Fellowship_Of_The_Ring.jpg', 'https://www.youtube.com/watch?v=aStYWD25fAQ'),
            Movie('The Lord of the Rings: The Two Towers', 'http://upload.wikimedia.org/wikipedia/en/a/ad/Lord_of_the_Rings_-_The_Two_Towers.jpg', 'https://www.youtube.com/watch?v=f7VjBeSwur0'),
            Movie('The Lord of the Rings: The Return of the King', 'http://upload.wikimedia.org/wikipedia/en/9/9d/Lord_of_the_Rings_-_The_Return_of_the_King.jpg', 'https://www.youtube.com/watch?v=r5X-hFf6Bwo')
         ]

# Generate the html file and open it in the browser.
open_movies_page(movies, 'The Lord of the Rings Trilogy')