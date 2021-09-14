#!/usr/bin/env python
# coding: utf-8

# ## Q1.Write a Python program to get a list, sorted in increasing order by the last element in each tuple from a given list of non-empty tuples
# 
# 
# 
# Sample List : [(2, 5), (1, 2), (4, 4), (2, 3), (2, 1)]
# 
# Expected Result : [(2, 1), (1, 2), (2, 3), (4, 4), (2, 5)]

# In[5]:


def pos(n):
    return n[-1]  
def sort(tuples):
    return sorted(tuples, key=pos)
a=[(2, 5), (1, 2), (4, 4), (2, 3), (2, 1)]
print(sort(a))


# ## Q2.Write a Python program to print a dictionary whose keys should be the alphabet from a-z and the value should be corresponding ASCII values.

# In[7]:


dict = {}
for x in range (97,123):
    dict[chr(x)] = x
print(dict)


# In[ ]:




