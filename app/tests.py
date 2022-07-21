# from bs4 import BeautifulSoup
# import requests
# import re
# import pandas as pd
#
#
# import pdb; pdb.set_trace()
# # import pdb; pdb.set_trace()
# # Downloading imdb top 250 movie's data
# url = 'https://www.imdb.com/best-of/top-indian-movies/ls576200429/'
# response = requests.get(url)
# soup = BeautifulSoup(response.text, "html.parser")
# movies = soup.select('td.titleColumn')
# crew = [a.attrs.get('title') for a in soup.select('td.titleColumn a')]
# ratings = [b.attrs.get('data-value')
#            for b in soup.select('td.posterColumn span[name=ir]')]
#
# # create a empty list for storing
# # movie information
# list = []
#
# # Iterating over movies to extract
# # each movie's details
# for index in range(0, len(movies)):
#     # Separating movie into: 'place',
#     # 'title', 'year'
#     movie_string = movies[index].get_text()
#     movie = (' '.join(movie_string.split()).replace('.', ''))
#     movie_title = movie[len(str(index)) + 1:-7]
#     year = re.search('\((.*?)\)', movie_string).group(1)
#     place = movie[:len(str(index)) - (len(movie))]
#     data = {"place": place,
#             "movie_title": movie_title,
#             "rating": ratings[index],
#             "year": year,
#             "star_cast": crew[index],
#             }
#     list.append(data)
# # printing movie details with its rating.
# for movie in list:
#     print(movie['place'], '-', movie['movie_title'], '(' + movie['year'] +
#           ') -', 'Starring:', movie['star_cast'], movie['rating'])
#
# ##.......##
# # import pdb; pdb.set_trace()
#
# df = pd.DataFrame(list)
# df.to_csv('imdb_top_250_movies.csv', index=False)




# import pandas library
import matplotlib
import pandas as pd

# Get the data
from jedi.api.refactoring import inline
import pdb; pdb.set_trace()

column_names = ['user_id', 'item_id', 'rating', 'timestamp']

path = 'https://media.geeksforgeeks.org/wp-content/uploads/file.tsv'

df = pd.read_csv(path, sep='\t', names=column_names)

# Check the head of the data
df.head()
# Check out all the movies and their respective IDs
movie_titles = pd.read_csv('https://media.geeksforgeeks.org/wp-content/uploads/Movie_Id_Titles.csv')
movie_titles.head()
data = pd.merge(df, movie_titles, on='item_id')
data.head()
# Calculate mean rating of all movies
data.groupby('title')['rating'].mean().sort_values(ascending=False).head()
# Calculate count rating of all movies
data.groupby('title')['rating'].count().sort_values(ascending=False).head()
# creating dataframe with 'rating' count values
ratings = pd.DataFrame(data.groupby('title')['rating'].mean())

ratings['num of ratings'] = pd.DataFrame(data.groupby('title')['rating'].count())

ratings.head()


# import matplotlib.pyplot as plt
# import seaborn as sns
#
# sns.set_style('white')%matplotlib inline
# # plot graph of 'num of ratings column'
# plt.figure(figsize =(10, 4))
#
# ratings['num of ratings'].hist(bins = 70)
# # plot graph of 'ratings' column
# plt.figure(figsize =(10, 4))
#
# ratings['rating'].hist(bins = 70)
# Sorting values according to
# the 'num of rating column'
moviemat = data.pivot_table(index ='user_id',
			columns ='title', values ='rating')

moviemat.head()

ratings.sort_values('num of ratings', ascending = False).head(10)
# analysing correlation with similar movies
starwars_user_ratings = moviemat['Star Wars (1977)']
liarliar_user_ratings = moviemat['Liar Liar (1997)']

starwars_user_ratings.head()
# analysing correlation with similar movies
similar_to_starwars = moviemat.corrwith(starwars_user_ratings).sort_values(ascending=False)
# similar_to_starwars = moviemat.corr()['Star Wars (1977)'].sort_values(ascending=False).iloc[:20]

similar_to_liarliar = moviemat.corrwith(liarliar_user_ratings)

corr_starwars = pd.DataFrame(similar_to_starwars, columns =['Correlation'])
corr_starwars.dropna(inplace = True)

corr_starwars.head()
# Similar movies like starwars
corr_starwars.sort_values('Correlation', ascending = False).head(10)
corr_starwars = corr_starwars.join(ratings['num of ratings'])

corr_starwars.head()

corr_starwars[corr_starwars['num of ratings']>100].sort_values('Correlation', ascending = False).head()


# Similar movies as of liarliar
corr_liarliar = pd.DataFrame(similar_to_liarliar, columns =['Correlation'])
corr_liarliar.dropna(inplace = True)

corr_liarliar = corr_liarliar.join(ratings['num of ratings'])
corr_liarliar[corr_liarliar['num of ratings']>100].sort_values('Correlation', ascending = False).head()






