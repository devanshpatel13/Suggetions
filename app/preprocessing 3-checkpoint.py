#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np

# import pdb; pdb.set_trace()

# ## Extracting features of 2018 movies from Wikipedia

# In[2]:

# import pdb;pdb.set_trace()
link = "https://en.wikipedia.org/wiki/List_of_American_films_of_2018"
df1 = pd.read_html(link, header=0)[2]
df2 = pd.read_html(link, header=0)[3]
df3 = pd.read_html(link, header=0)[4]
df4 = pd.read_html(link, header=0)[5]


# In[3]:


df = df1.append(df2.append(df3.append(df4,ignore_index=True),ignore_index=True),ignore_index=True)


# In[4]:


df


# In[5]:


from tmdbv3api import TMDb
import json
import requests
tmdb = TMDb()
tmdb.api_key = '31bfa441a915968c9c1f35f5476c7687'


# In[6]:


from tmdbv3api import Movie
tmdb_movie = Movie()
def get_genre(x):
    genres = []
    result = tmdb_movie.search(x)
    movie_id = result[0].id
    response = requests.get('https://api.themoviedb.org/3/movie/{}?api_key={}'.format(movie_id,tmdb.api_key))
    data_json = response.json()
    if data_json['genres']:
        genre_str = " " 
        for i in range(0,len(data_json['genres'])):
            genres.append(data_json['genres'][i]['name'])
        return genre_str.join(genres)
    else:
        np.NaN


# In[7]:


df['genres'] = df['Title'].map(lambda x: get_genre(str(x)))


# In[8]:


df


# In[9]:


df_2018 = df[['Title','Cast and crew','genres']]


# In[10]:


df_2018


# In[11]:


def get_director(x):
    if " (director)" in x:
        return x.split(" (director)")[0]
    elif " (directors)" in x:
        return x.split(" (directors)")[0]
    else:
        return x.split(" (director/screenplay)")[0]


# In[12]:


df_2018['director_name'] = df_2018['Cast and crew'].map(lambda x: get_director(x))


# In[13]:


def get_actor1(x):
    return ((x.split("screenplay); ")[-1]).split(", ")[0])


# In[14]:


df_2018['actor_1_name'] = df_2018['Cast and crew'].map(lambda x: get_actor1(x))


# In[15]:


def get_actor2(x):
    if len((x.split("screenplay); ")[-1]).split(", ")) < 2:
        return np.NaN
    else:
        return ((x.split("screenplay); ")[-1]).split(", ")[1])


# In[16]:


df_2018['actor_2_name'] = df_2018['Cast and crew'].map(lambda x: get_actor2(x))


# In[17]:


def get_actor3(x):
    if len((x.split("screenplay); ")[-1]).split(", ")) < 3:
        return np.NaN
    else:
        return ((x.split("screenplay); ")[-1]).split(", ")[2])


# In[18]:


df_2018['actor_3_name'] = df_2018['Cast and crew'].map(lambda x: get_actor3(x))


# In[19]:


df_2018


# In[20]:


df_2018 = df_2018.rename(columns={'Title':'movie_title'})


# In[21]:


new_df18 = df_2018.loc[:,['director_name','actor_1_name','actor_2_name','actor_3_name','genres','movie_title']]


# In[22]:


new_df18


# In[23]:


new_df18['actor_2_name'] = new_df18['actor_2_name'].replace(np.nan, 'unknown')
new_df18['actor_3_name'] = new_df18['actor_3_name'].replace(np.nan, 'unknown')


# In[24]:


new_df18['movie_title'] = new_df18['movie_title'].str.lower()


# In[25]:


new_df18['comb'] = new_df18['actor_1_name'] + ' ' + new_df18['actor_2_name'] + ' '+ new_df18['actor_3_name'] + ' '+ new_df18['director_name'] +' ' + new_df18['genres']


# In[26]:


new_df18


# ## Extracting features of 2019 movies from Wikipedia

# In[27]:


link = "https://en.wikipedia.org/wiki/List_of_American_films_of_2019"
df1 = pd.read_html(link, header=0)[2]
df2 = pd.read_html(link, header=0)[3]
df3 = pd.read_html(link, header=0)[4]
df4 = pd.read_html(link, header=0)[5]


# In[28]:


df = df1.append(df2.append(df3.append(df4,ignore_index=True),ignore_index=True),ignore_index=True)


# In[29]:


df


# In[30]:


df['genres'] = df['Title'].map(lambda x: get_genre(str(x)))


# In[31]:


df_2019 = df[['Title','Cast and crew','genres']]


# In[32]:


df_2019


# In[33]:


def get_director(x):
    if " (director)" in x:
        return x.split(" (director)")[0]
    elif " (directors)" in x:
        return x.split(" (directors)")[0]
    else:
        return x.split(" (director/screenplay)")[0]


# In[34]:


df_2019['director_name'] = df_2019['Cast and crew'].map(lambda x: get_director(str(x)))


# In[35]:


def get_actor1(x):
    return ((x.split("screenplay); ")[-1]).split(", ")[0])


# In[36]:


df_2019['actor_1_name'] = df_2019['Cast and crew'].map(lambda x: get_actor1(x))


# In[37]:


def get_actor2(x):
    if len((x.split("screenplay); ")[-1]).split(", ")) < 2:
        return np.NaN
    else:
        return ((x.split("screenplay); ")[-1]).split(", ")[1])


# In[38]:


df_2019['actor_2_name'] = df_2019['Cast and crew'].map(lambda x: get_actor2(x))


# In[39]:


def get_actor3(x):
    if len((x.split("screenplay); ")[-1]).split(", ")) < 3:
        return np.NaN
    else:
        return ((x.split("screenplay); ")[-1]).split(", ")[2])


# In[40]:


df_2019['actor_3_name'] = df_2019['Cast and crew'].map(lambda x: get_actor3(x))


# In[41]:


df_2019 = df_2019.rename(columns={'Title':'movie_title'})


# In[42]:


new_df19 = df_2019.loc[:,['director_name','actor_1_name','actor_2_name','actor_3_name','genres','movie_title']]


# In[43]:


new_df19['actor_2_name'] = new_df19['actor_2_name'].replace(np.nan, 'unknown')
new_df19['actor_3_name'] = new_df19['actor_3_name'].replace(np.nan, 'unknown')


# In[44]:


new_df19['movie_title'] = new_df19['movie_title'].str.lower()


# In[45]:


new_df19['comb'] = new_df19['actor_1_name'] + ' ' + new_df19['actor_2_name'] + ' '+ new_df19['actor_3_name'] + ' '+ new_df19['director_name'] +' ' + new_df19['genres']


# In[46]:


new_df19


# In[47]:


my_df = new_df18.append(new_df19,ignore_index=True)


# In[50]:


my_df


# In[51]:


old_df = pd.read_csv('/home/plutusdev/Downloads/AJAX-Movie-Recommendation-System-with-Sentiment-Analysis-master/datasets/new_data.csv')


# In[52]:


old_df


# In[53]:


final_df = old_df.append(my_df,ignore_index=True)


# In[54]:


final_df


# In[55]:


final_df.isna().sum()


# In[56]:


final_df = final_df.dropna(how='any')


# In[57]:


final_df.isna().sum()


# In[58]:


final_df.to_csv('/home/plutusdev/Downloads/AJAX-Movie-Recommendation-System-with-Sentiment-Analysis-master/datasets/final_data.csv',index=False)

