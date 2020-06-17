#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np


# In[2]:


df = pd.DataFrame({'From_To': ['LoNDon_paris', 'MAdrid_miLAN',
'londON_StockhOlm','Budapest_PaRis', 'Brussels_londOn'],
'FlightNumber': [10045, np.nan, 10065, np.nan, 10085],
'RecentDelays': [[23, 47], [], [24, 43, 87], [13], [67, 32]],
'Airline': ['KLM(!)', '<Air France> (12)', '(British Airways. )',
'12. Air France', '"Swiss Air"']})


# In[3]:


df


# In[4]:


df[['From','To']]=df['From_To'].str.split('_',expand=True)


# In[5]:


df['From_To'].str.capitalize()


# In[6]:


df['From']=df['From'].str.capitalize()
df['To']=df['To'].str.capitalize()


# In[7]:


df


# In[8]:


df.drop(columns='From_To',inplace=True)


# In[9]:


df


# In[10]:


df[['Delay_1','Delay_2','Delay_3']]=pd.DataFrame(df['RecentDelays'].tolist())


# In[11]:


df.rename(columns={'RecentDelays':'Delays'},inplace=True)


# In[12]:


df


# In[15]:


df['FlightNumber']=df['FlightNumber'].astype('Int32')


# In[16]:


df


# In[17]:


df['FlightNumber']=df['FlightNumber'].fillna(axis=0,method='ffill')+df.groupby(df['FlightNumber'].notnull().cumsum()).cumcount()


# In[ ]:


df.groupby(df['FlightNumber'].notnull().cumsum())


# In[18]:


df['FlightNumber']=df['FlightNumber'].astype('Int32')


# In[ ]:


s = pd.Series([2, np.nan, 5, -1, 0])
s


# In[ ]:


s.cumsum()


# In[19]:


df


# In[23]:


df.groupby(df['FlightNumber'].isnull().cumsum()).cumcount()


# In[32]:


df.groupby(df['Delay_3'].notnull().cumsum()).cumcount()


# In[ ]:





# In[ ]:




