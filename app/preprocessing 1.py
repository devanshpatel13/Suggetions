#!/usr/bin/env python
# coding: utf-8

# In[18]:


import pandas as pd
import numpy as np


# In[19]:


data = pd.read_csv('/home/plutusdev/Downloads/AJAX-Movie-Recommendation-System-with-Sentiment-Analysis-master/datasets/movie_metadata.csv')



# In[21]:


data.head(11)


# In[22]:


data.shape


# In[23]:


data.columns


# In[24]:


# we have movies only upto 2016
import matplotlib.pyplot as plt
data.title_year.value_counts(dropna=False).sort_index().plot(kind='barh',figsize=(15,16))
plt.show()


# In[ ]:


# recommendation will be based on these features only
data = data.loc[:,['director_name','actor_1_name','actor_2_name','actor_3_name','genres','movie_title']]


# In[ ]:


data.head(10)


# In[ ]:


data['actor_1_name'] = data['actor_1_name'].replace(np.nan, 'unknown')
data['actor_2_name'] = data['actor_2_name'].replace(np.nan, 'unknown')
data['actor_3_name'] = data['actor_3_name'].replace(np.nan, 'unknown')
data['director_name'] = data['director_name'].replace(np.nan, 'unknown')


# In[ ]:


data


# In[7]:


data['genres'] = data['genres'].str.replace('|', ' ')


# In[16]:


data


# In[17]:


data['movie_title'] = data['movie_title'].str.lower()


# In[18]:


# null terminating char at the end
data['movie_title'][1]


# In[19]:


# removing the null terminating char at the end
data['movie_title'] = data['movie_title'].apply(lambda x : x[:-1])


# In[20]:


data['movie_title'][1]


# In[21]:


data.to_csv('data.csv',index=False)

