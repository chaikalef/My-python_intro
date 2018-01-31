
# coding: utf-8

# In[15]:


# insert three integers separated by commas
a, b, c = [int(i) for i in input().split(',')]

print('YES' if (a + b > c) and (a + c > b) and (b + c > a) else 'NO')

