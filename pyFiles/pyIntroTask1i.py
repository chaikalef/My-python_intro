
# coding: utf-8

# In[6]:


# insert three integers separated by commas
a, b, c = [int(i) for i in input().split(',')]
    
if (b > a):
    a = b
    
if (a > c):
    print(a)
else:
    print(c)

