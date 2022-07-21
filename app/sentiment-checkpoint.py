#!/usr/bin/env python
# coding: utf-8

# In[15]:


import pandas as pd
import numpy as np
import nltk
from nltk.corpus import stopwords
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.model_selection import train_test_split
from sklearn import naive_bayes
from sklearn.metrics import roc_auc_score,accuracy_score
import pickle


# In[2]:


import pdb; pdb.set_trace()

nltk.download("stopwords")


# In[3]:


dataset = pd.read_csv('/home/plutusdev/Downloads/AJAX-Movie-Recommendation-System-with-Sentiment-Analysis-master/datasets/reviews.txt',sep = '\t', names =['Reviews','Comments'])


# In[4]:


dataset


# In[5]:


stopset = set(stopwords.words('english'))


# In[6]:


vectorizer = TfidfVectorizer(use_idf = True,lowercase = True, strip_accents='ascii',stop_words=stopset)


# In[16]:


X = vectorizer.fit_transform(dataset.Comments)
# vectorizer.get_feature_names_out()
# vectorizer
y = dataset.Reviews
pickle.dump(vectorizer, open('tranform.pkl', 'wb'))
print(X.shape)

# In[17]:


X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.20, random_state=42)


# In[18]:


clf = naive_bayes.MultinomialNB()
clf.fit(X_train,y_train)
clf

# In[19]:


accuracy_score(y_test,clf.predict(X_test))*100

accuracy_score
# In[20]:


clf = naive_bayes.MultinomialNB()
clf.fit(X,y)


# In[21]:


accuracy_score(y_test,clf.predict(X_test))*100


# In[22]:


filename = 'nlp_model.pkl'
pickle.dump(clf, open(filename, 'wb'))

