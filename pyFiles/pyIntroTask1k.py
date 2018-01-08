
# coding: utf-8

# In[7]:


# insert four integers separated by commas
a, b, c, d = [int(i) for i in input().split(',')]
    
print('YES' if (a == c) or (b == d) else 'NO')

