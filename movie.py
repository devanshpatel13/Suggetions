import sys

import pandas as pd
# ratings = pd.read_csv('/home/plutusdev/Downloads/archive/ratings.csv')
# ratings
#
# movies_metadata = pd.read_csv('/home/plutusdev/Downloads/archive/movies_metadata.csv')
# movies_metadata
#
#
# credits = pd.read_csv('/home/plutusdev/Downloads/archive/credits.csv')
# credits
#
# keyword = pd.read_csv('/home/plutusdev/Downloads/archive/keywords.csv')
# keyword
#
# link = pd.read_csv('/home/plutusdev/Downloads/archive/links.csv')
# link


#
# main = pd.read_csv("/home/plutusdev/Downloads/AJAX-Movie-Recommendation-System-with-Sentiment-Analysis-master/main_data.csv")
# main
# data = main.append(ratings,ignore_index=True)
# data
# # import pdb; pdb.set_trace()
#
# data = data.iloc[:6010]
# data
# data.rating
# import random
#
# for i in range(0,6009):
#     n = random.randint(1,10)
#     data.rating[i] = n
#
#
#
#
# data.to_csv('data_rating.csv',index=False)

# import pdb;pdb.set_trace()

data = pd.read_csv("/home/plutusdev/Projects/Task/suggetion/data_rating.csv")

data["rating"].fillna(5.0, inplace = True)

data

#
print(data)
#
# data.groupby('movie_title')['rating'].mean().sort_values(ascending=False)
# data.groupby('movie_title')['rating'].count().sort_values(ascending=False).head(100)
# ratings = pd.DataFrame(data.groupby('movie_title')['rating'].mean())
# ratings['num of ratings'] = pd.DataFrame(data.groupby('movie_title')['rating'].count())
#
#
# moviemat = data.pivot_table(columns ='movie_title', values ='rating')
#
# ratings.sort_values('num of ratings', ascending = False).head(10)
#
#
# starwars_user_ratings = moviemat['1 mile to you']
#
# similar_to_starwars = moviemat.corrwith(starwars_user_ratings)
#
# data.sort_values("rating")
# data
# data.sort_values(by=[float("rating")])
#
# # float(data.rating)
#
#
#
# ratings['num of ratings'] = pd.DataFrame(data['rating'])
#
#
#
# # if data.rating == 10:
# #     print(data.rating)
#
 # if data.rating.values ==    10:
#
#  x = int(data.rating.values)
#
# for x in range("data.rating.values"):
#  if x == 10:
#   print(x)

  # data.rating._get_value("10")10

# import pdb
# pdb.set_trace()
#
# for y in data.values:
#  if y == "rating":
#    for x in data.rating:
#     if x == float(10):
#      print(x)


#  print(y.rating)
#
# if y['rating'] == float(10):
#  print(y)
#
import matplotlib.pyplot as plt

data.drop(['userId', 'movieId','timestamp'], axis=1, inplace=True)

data



data.sort_values("rating", ascending =False, inplace= True)

# df = data.cumsum()
#
# plt.figure();
#
# df.plot();

#
data.plot()
plt.show()
# plt.savefig(sys.stdout.buffer)
# sys.stdout.flush()

print(data)


# data.to_csv('data.csv',index=False)
