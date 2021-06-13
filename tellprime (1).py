#!/usr/bin/env python
# coding: utf-8

# # This file contains a code for function which tell us that a given number is prime or not

# In[1]:


get_ipython().run_line_magic('pylab', 'inline')


# In[2]:


from numba import jit
import math as m


# ### Version 1

# In[4]:


@jit(nopython=True)
def tellprime1(z):
    if z==2:
        return True
    elif z==3:
        return True
    else:
        i = 2
        l = m.sqrt(z)
        u = True 
        while i<=l and u:
            if z%i==0:
                return False
                break
            elif i+1>l and z%i != 0:
                return True
                break
            else:
                i+=1
            u = (i%6 in [1,5]) or (i in [2,3])
            while u == False:
                i+=1
                if z%i==0:
                    return False
                    break
                elif i+1>l and z%i != 0:
                    return True
                    break
                u = i%6 in [1,5]

                

get_ipython().run_line_magic('time', 'tellprime(23)')


# In[6]:


#The 570,004,517,329th prime is 16,765,962,748,063.                
             
get_ipython().run_line_magic('time', 'print(tellprime(16765962748063))')


# ### version 2
# 

# In[8]:


@jit(nopython=True)
def tellprime2(z):
    if z == 1:
        return False
    elif z in [2,3]:
        return True
    elif z%2==0:
        return False
    elif z%3==0:
        return False
    else:
        for i in range(4, int(z**(.5))+1):
            if i%6 in [1,5]:
                if z%i==0:
                    return False
        return True
    
tellprime2(23)


# In[9]:


get_ipython().run_line_magic('time', 'print(tellprime2(16765962748063))')


# In[ ]:




