
# coding: utf-8

# In[3]:


from math import factorial as f

n, k = int(input()), int(input())

print(int(f(n) / (f(k) * f(n - k))))

