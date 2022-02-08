from asyncore import file_dispatcher
import csv
from tkinter import W
from typing import final

with open("movies.csv") as file:
    file_read = csv.reader(file)
    data = list(file_read)
    all_movies = data[1:]
    headers = data[0]

headers.append("Poster_Link")

# To create a new file called final.csv and to merge the movies and the links
with open("final.csv", "a+") as file:
    file_write = csv.writer(file)
    file_read.writerow(headers)
    
with open("movie_links.csv") as file:
    file_read = csv.reader(file)
    data = list(file_read)
    all_movie_links = data[1:]

for i in all_movies:
    poster_find = any(i[8] in movie_links for movie_links in all_movie_links)

    if poster_find:

        for movie_links in all_movie_links:
 
            if i[8] == movie_links[0]:
                i.append(movie_links[1])

                if len(i) == 28:

                    with open("final.csv", "a+") as file:
                        file_write = csv.writer(file)
                        file_read.writerow(i)