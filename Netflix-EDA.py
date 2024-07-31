#!/usr/bin/env python
# coding: utf-8

# ## Importing Libraries

# In[1]:


import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import warnings 


# ## Loading data into DataFrame

# In[2]:


data = pd.read_csv(r'C:\Users\Rishikesh\OneDrive\Desktop\Project\netflix_titles_py.csv')


# In[3]:


data


# ## Information about the data

# In[4]:


data.info()


# ## Statistics of the Data

# In[5]:


data.describe().T


# ## Finding null values from each column

# In[6]:


data.isnull().sum().sort_values(ascending = False)


# In[7]:


data.isnull().sum().sort_values(ascending = False)/len(data)*100


# In[8]:


sns.heatmap(data.isnull())
plt.show()


# In[9]:


data.shape


# ## Replacing Null Values

# In[10]:


data['director'].fillna('Unknown',inplace = True)
data['cast'].fillna('Unknown',inplace = True)


# In[11]:


data.isnull().sum()


# In[12]:


col = data.columns
for i in range(0,len(col)):
    data[col[i]] = data[col[i]].replace(np.NaN,data[col[i]].mode()[0])


# In[13]:


data.isnull().sum()


# In[14]:


data.columns


# ## Finding Count of Duplicates

# In[15]:


data['show_id'].duplicated().sum()


# ## Converting invalid Dates to 'NaN'

# In[16]:


data['date_added'] = pd.to_datetime(data['date_added'],errors = 'coerce')


# In[17]:


data.isnull().sum()


# ## Filling NaN values

# In[18]:


data['date_added'].fillna(method = 'bfill',inplace = True)


# ## Creating Release Month Column

# In[19]:


data['Release Month'] = data['date_added'].dt.month_name()


# In[20]:


data.isnull().sum()


# ## Creating 'Monthly Releases Count' Bar Plot

# In[21]:


data['Release Month'].value_counts().sort_values(ascending=False).plot.bar()

plt.title('Monthly Releases Count')
plt.xticks(rotation = 45)
plt.ylabel('Count')
plt.show()


# ## Creating Yearwise Trends Bar Plot

# In[22]:


yearwise = data['release_year'].value_counts()


# In[23]:


plt.figure(figsize = (12,6))

yearwise.plot.bar(color = 'black')

plt.title('Yearwise Trends')

plt.xlabel('Year')

plt.ylabel('Count of releases present on netflix')

plt.show()


# ## Number of Releases Per Type

# In[24]:


plt.figure(figsize = (10,5))
custom_palette = {'Movie':'pink','TV Show':'lightblue'}
x = sns.countplot(data = data, x = 'type',palette = custom_palette)
x.bar_label(x.containers[0])
plt.show()

