import pandas as pd

movieData = pd.read_csv("tobitheghost/static/pages/movies/movies.csv")

# print(movieData["title"].values)
listoftitles = movieData["poster"].values
# print(listoftitles[0])
