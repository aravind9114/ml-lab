#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np


# In[2]:


a=np.array([0,1,2])
print(type(a))


# In[3]:


print(a.shape)


# In[4]:


print(a[2])


# In[5]:


a[0]=9


# In[6]:


print(a[0])


# In[7]:


print(a)


# In[10]:


b=np.array([[0,1,2],[3,4,5]])


# In[11]:


print(b.shape)


# In[14]:


print(b[0,0],b[1,2],b[1,1])


# In[17]:


a=np.zeros((4,4))


# In[18]:


print(a)


# In[19]:


b=np.ones((3,3))
print(b)


# In[21]:


b=np.full((3,3),100)
print(b)


# In[22]:


import pandas as pd


# In[24]:


s=pd.Series([1,2,3,np.nan,5,6],index=['A','B','D','C','E','F'])


# In[25]:


print(s)


# In[27]:


data={'gender':['f','m','m'],'empid':['1','2','3'],'age':['23','34','32']}


# In[28]:


print(data)


# In[33]:


df=pd.DataFrame(data,columns=['empid','gender','age'])


# In[34]:


df


# In[40]:


f=pd.read_csv('C:/Users/user/Documents/marks.csv')


# In[41]:


f=pd.read('C:/Users/user/Documents/marks.csv')


# In[42]:


df=pd.to_csv('C:/Users/user/Documents/marks.csv')


# In[ ]:


from numpy import loadtxt
from urllib.request import urlopen

