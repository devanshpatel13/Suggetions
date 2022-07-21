#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np
import requests
import bs4 as bs
import urllib.request


# ## Extracting features of 2020 movies from Wikipedia

# In[2]:


link = "https://en.wikipedia.org/wiki/List_of_American_films_of_2020"


# In[3]:


source = urllib.request.urlopen(link).read()
soup = bs.BeautifulSoup(source,'lxml')


# In[4]:


tables = soup.find_all('table',class_='wikitable sortable')


# In[5]:


len(tables)


# In[6]:


type(tables[0])


# In[7]:


df1 = pd.read_html(str(tables[0]))[0]
df2 = pd.read_html(str(tables[1]))[0]
df3 = pd.read_html(str(tables[2]))[0]
df4 = pd.read_html(str(tables[3]).replace("'1\"\'",'"1"'))[0] # avoided "ValueError: invalid literal for int() with base 10: '1"'


# In[8]:


df = df1.append(df2.append(df3.append(df4,ignore_index=True),ignore_index=True),ignore_index=True)


# In[9]:


df


# In[10]:


df_2020 = df[['Title','Cast and crew']]


# In[11]:


df_2020


# In[12]:


# get_ipython().system('pip install tmdbv3api')


# In[13]:


from tmdbv3api import TMDb
import json
import requests
tmdb = TMDb()
tmdb.api_key = ''


# In[14]:


from tmdbv3api import Movie
tmdb_movie = Movie() 
def get_genre(x):
    genres = []
    result = tmdb_movie.search(x)
    if not result:
      return np.NaN
    else:
      movie_id = result[0].id
      response = requests.get('https://api.themoviedb.org/3/movie/{}?api_key={}'.format(movie_id,tmdb.api_key))
      data_json = response.json()
      if data_json['genres']:
          genre_str = " " 
          for i in range(0,len(data_json['genres'])):
              genres.append(data_json['genres'][i]['name'])
          return genre_str.join(genres)
      else:
          return np.NaN


# In[15]:


df_2020['genres'] = df_2020['Title'].map(lambda x: get_genre(str(x)))


# In[16]:


df_2020


# In[17]:


def get_director(x):
    if " (director)" in x:
        return x.split(" (director)")[0]
    elif " (directors)" in x:
        return x.split(" (directors)")[0]
    else:
        return x.split(" (director/screenplay)")[0]


# In[18]:


df_2020['director_name'] = df_2020['Cast and crew'].map(lambda x: get_director(str(x)))


# In[19]:


def get_actor1(x):
    return ((x.split("screenplay); ")[-1]).split(", ")[0])


# In[20]:


df_2020['actor_1_name'] = df_2020['Cast and crew'].map(lambda x: get_actor1(str(x)))


# In[21]:


def get_actor2(x):
    if len((x.split("screenplay); ")[-1]).split(", ")) < 2:
        return np.NaN
    else:
        return ((x.split("screenplay); ")[-1]).split(", ")[1])


# In[22]:


df_2020['actor_2_name'] = df_2020['Cast and crew'].map(lambda x: get_actor2(str(x)))


# In[23]:


def get_actor3(x):
    if len((x.split("screenplay); ")[-1]).split(", ")) < 3:
        return np.NaN
    else:
        return ((x.split("screenplay); ")[-1]).split(", ")[2])


# In[24]:


df_2020['actor_3_name'] = df_2020['Cast and crew'].map(lambda x: get_actor3(str(x)))


# In[25]:


df_2020


# In[26]:


df_2020 = df_2020.rename(columns={'Title':'movie_title'})


# In[27]:


new_df20 = df_2020.loc[:,['director_name','actor_1_name','actor_2_name','actor_3_name','genres','movie_title']]


# In[28]:


new_df20


# In[29]:


new_df20['comb'] = new_df20['actor_1_name'] + ' ' + new_df20['actor_2_name'] + ' '+ new_df20['actor_3_name'] + ' '+ new_df20['director_name'] +' ' + new_df20['genres']


# In[30]:


new_df20.isna().sum()


# In[31]:


new_df20 = new_df20.dropna(how='any')


# In[32]:


new_df20.isna().sum()


# In[33]:


new_df20['movie_title'] = new_df20['movie_title'].str.lower()


# In[34]:


new_df20


# In[ ]:


old_df = pd.read_csv('final_data.csv')


# In[ ]:


old_df


# In[ ]:


final_df = old_df.append(new_df20,ignore_index=True)


# In[ ]:


final_df


# In[ ]:


final_df.to_csv('main_data.csv',index=False)

