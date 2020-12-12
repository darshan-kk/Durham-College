#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd


# In[3]:


pwd


# In[8]:


raw_df = pd.read_csv('C:\\Users\\darsh\\downloads\\youtube_dataset.csv', encoding = "ISO-8859-1", engine='python')


# In[10]:


raw_df.sort_values(by=["subscribers"], ascending = False, inplace= True)

raw_df
# In[11]:


raw_df


# In[12]:


top_1000 = raw_df.iloc[:1000]


# In[13]:


top_1000


# In[42]:


import matplotlib.pyplot as plt


# In[22]:


import os 
os.getcwd()


# In[26]:


ctviz = top_1000.groupby("channeltype")["name"].count()


# In[27]:


ctviz.plot.bar()


# In[40]:


def channel_distribution(df):
    df = df.fillna(value=0)
    xx = df.groupby("channeltype")["name"].count()
    return xx.plot.bar()


# In[41]:


cd = channel_distribution(top_1000)


# In[43]:


top_1000.to_csv (r'C:\Users\Darsh\Desktop\export_dataframe.csv', index = False, header=True)


# In[ ]:




