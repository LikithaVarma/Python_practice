#!/usr/bin/env python
# coding: utf-8

# In[1]:


import urllib.request
import requests
from bs4 import BeautifulSoup
import nltk
import operator
from collections import Counter


# In[2]:


url='https://www.php.net/'
my_source_code = requests.get(url).text
soup = BeautifulSoup(my_source_code, 'html.parser')


# In[3]:


def starting(soup_text):
    my_wordlist=[]
    for each_text in soup_text.findAll('div',{'class':'newscontent'}):
        #print(each_text)
        content=each_text.text
        words=content.lower().split()
        for each_word in words:
            my_wordlist.append(each_word)
    word_count={}
    for word in my_wordlist:
        if word in word_count:
            word_count[word]+=1
        else:
            word_count[word]=1
    return word_count


# In[4]:


b=starting(soup)
print(b)


# In[ ]:





# In[ ]:




