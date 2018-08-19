
# coding: utf-8

# In[1]:


import os
os.listdir()


# In[2]:


import pandas


# In[3]:


df1 = pandas.read_csv("supermarkets.csv")
df1.set_index("ID")


# In[4]:


df2 = pandas.read_json("supermarkets.json")
df2.set_index("ID")


# In[5]:


df3 = pandas.read_excel("supermarkets.xlsx", sheet_name=0)
df3.set_index("ID")


# In[6]:


df4 = pandas.read_csv("supermarkets-commas.txt")
df4.set_index("ID")


# In[7]:


df5 = pandas.read_csv("supermarkets-semi-colons.txt", sep=";")
df5.set_index("ID")


# In[8]:


df6 = pandas.read_json("http://pythonhow.com/supermarkets.json")
df6 = df6.set_index("Address")
df6


# In[9]:


df6.loc["332 Hill St": "1056 Sanchez St","Country":"Name"]


# In[10]:


df6.iloc[1:,1:4]


# In[11]:


df6


# In[12]:


df6 = df6.drop("ID", 1)
df6


# In[14]:


df6 = df6.drop("332 Hill St", 0)
df6


# In[16]:


df6 = df6.drop(df6.columns[0:2], 1)
df6


# In[17]:


df6 = df6.drop(df6.index[2:4], 0)
df6


# In[22]:


df6["Continent"] = df6.shape[0]*["North America"]
df6


# In[21]:


df6["Continent"] = df6["State"] + ", " + "North America"
df6


# In[24]:


df6_t = df6.T
df6_t


# In[28]:


df6_t["My Address"] = [10, "Sofia", "Bulgaria", "Europe"]
df6_t


# In[30]:


df6 = df6_t.T
df6


# In[1]:


from geopy.geocoders import Nominatim


# In[6]:


nom = Nominatim()


# In[7]:


import pandas


# In[8]:


df = pandas.read_csv("supermarkets.csv")
df


# In[9]:


df["Address"] = df["Address"] + ", " + df["City"] + ", " + df["State"] + ", " + df["Country"]
df


# In[10]:


df["Coordinates"] = df["Address"].apply(nom.geocode)
df


# In[13]:


df["Latitude"] = df["Coordinates"].apply(lambda x: x.latitude if x != None else None)
df["Longitude"] = df["Coordinates"].apply(lambda x: x.longitude if x != None else None)
df

