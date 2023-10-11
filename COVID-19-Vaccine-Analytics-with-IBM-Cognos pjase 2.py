#!/usr/bin/env python
# coding: utf-8

# 
# # COVID-19-Vaccine-Analytics-with-IBM-Cognos Phase 2
# 

# In[1]:


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os
for dirname, _, filenames in os.walk('/kaggle/input'):
    for filename in filenames:
        print(os.path.join(dirname, filename))


# In[2]:


data = pd.read_csv("country_vaccinations.csv")
data.head()


# In[3]:


data.describe()


# In[4]:


pd.to_datetime(data.date)
data.country.value_counts()


# In[5]:


data = data[data.country.apply(lambda x: x not in ["England", "Scotland", "Wales", "Northern Ireland"])]
data.country.value_counts()


# In[6]:


data.vaccines.value_counts()


# In[7]:


df = data[["vaccines", "country"]]
df.head()


# In[8]:


dict_ = {}
for i in df.vaccines.unique():
  dict_[i] = [df["country"][j] for j in df[df["vaccines"]==i].index]
vaccines = {}
for key, value in dict_.items():
  vaccines[key] = set(value)
for i, j in vaccines.items():
  print(f"{i}:>>{j}")


# In[9]:


import plotly.express as px
import plotly.offline as py
vaccine_map = px.choropleth(data, locations = 'iso_code', color = 'vaccines')
vaccine_map.update_layout(height=300, margin={"r":0,"t":0,"l":0,"b":0})
vaccine_map.show()


# In[ ]:




