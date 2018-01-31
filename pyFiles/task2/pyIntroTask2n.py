
# coding: utf-8

# In[4]:


from math import factorial as f

n = int(input())
res = 0

for x in range(1, n + 1):
    res += f(x)

print(res)

