#!/usr/bin/env python
# coding: utf-8

# In[38]:


import numpy as np
import pandas as pd


# In[39]:


credits = pd.read_csv('credits.csv')


# In[40]:


credits


# In[41]:


meta = pd.read_csv('movies_metadata.csv')


# In[42]:


meta['release_date'] = pd.to_datetime(meta['release_date'], errors='coerce')


# In[43]:


meta['year'] = meta['release_date'].dt.year


# In[44]:


meta['year'].value_counts().sort_index()


# In[45]:


# Getting only 2017 movies as we already have movies up to the year 2016 in preprocessing 1 file. 
# We don't have enough data for the movies from 2018, 2019 and 2020. 
# We'll deal with it in the upcoming preprocessing files
new_meta = meta.loc[meta.year == 2017,['genres','id','title','year']]


# In[46]:


new_meta


# In[47]:


new_meta['id'] = new_meta['id'].astype(int)


# In[48]:


data = pd.merge(new_meta, credits, on='id')


# In[49]:


pd.set_option('display.max_colwidth', 75)
data


# In[50]:


# evaluates an expression node or a string containing a Python literal or container display
import ast
data['genres'] = data['genres'].map(lambda x: ast.literal_eval(x))
data['cast'] = data['cast'].map(lambda x: ast.literal_eval(x))
data['crew'] = data['crew'].map(lambda x: ast.literal_eval(x))


# In[51]:


def make_genresList(x):
    gen = []
    st = " "
    for i in x:
        if i.get('name') == 'Science Fiction':
            scifi = 'Sci-Fi'
            gen.append(scifi)
        else:
            gen.append(i.get('name'))
    if gen == []:
        return np.NaN
    else:
        return (st.join(gen))


# In[52]:


data['genres_list'] = data['genres'].map(lambda x: make_genresList(x))


# In[53]:


data['genres_list']


# In[54]:


def get_actor1(x):
    casts = []
    for i in x:
        casts.append(i.get('name'))
    if casts == []:
        return np.NaN
    else:
        return (casts[0])


# In[55]:


data['actor_1_name'] = data['cast'].map(lambda x: get_actor1(x))


# In[56]:


def get_actor2(x):
    casts = []
    for i in x:
        casts.append(i.get('name'))
    if casts == [] or len(casts)<=1:
        return np.NaN
    else:
        return (casts[1])


# In[57]:


data['actor_2_name'] = data['cast'].map(lambda x: get_actor2(x))


# In[58]:


data['actor_2_name']


# In[59]:


def get_actor3(x):
    casts = []
    for i in x:
        casts.append(i.get('name'))
    if casts == [] or len(casts)<=2:
        return np.NaN
    else:
        return (casts[2])


# In[60]:


data['actor_3_name'] = data['cast'].map(lambda x: get_actor3(x))


# In[61]:


data['actor_3_name']


# In[62]:


def get_directors(x):
    dt = []
    st = " "
    for i in x:
        if i.get('job') == 'Director':
            dt.append(i.get('name'))
    if dt == []:
        return np.NaN
    else:
        return (st.join(dt))


# In[63]:


data['director_name'] = data['crew'].map(lambda x: get_directors(x))


# In[64]:


data['director_name']


# In[65]:


movie = data.loc[:,['director_name','actor_1_name','actor_2_name','actor_3_name','genres_list','title']]


# In[66]:


movie


# In[67]:


movie.isna().sum()


# In[68]:


movie = movie.dropna(how='any')


# In[69]:


movie.isna().sum()


# In[70]:


movie = movie.rename(columns={'genres_list':'genres'})
movie = movie.rename(columns={'title':'movie_title'})


# In[71]:


movie['movie_title'] = movie['movie_title'].str.lower()


# In[72]:


movie['comb'] = movie['actor_1_name'] + ' ' + movie['actor_2_name'] + ' '+ movie['actor_3_name'] + ' '+ movie['director_name'] +' ' + movie['genres']


# In[73]:


movie


# In[74]:


old = pd.read_csv('data.csv')


# In[75]:


old


# In[77]:


old['comb'] = old['actor_1_name'] + ' ' + old['actor_2_name'] + ' '+ old['actor_3_name'] + ' '+ old['director_name'] +' ' + old['genres']


# In[78]:


old


# In[79]:


new = old.append(movie)


# In[80]:


new


# In[81]:


new.drop_duplicates(subset ="movie_title", keep = 'last', inplace = True)


# In[82]:


new


# In[85]:


new.to_csv('new_data.csv',index=False)


# In[ ]:




