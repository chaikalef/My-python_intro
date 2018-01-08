
# coding: utf-8

# In[8]:


# insert four integers separated by commas
a, b, c, d = [int(i) for i in input().split(',')]
    
print('YES' if a in range(1, 8) and b in range(1, 8) and c in range(1, 8) and d in range(1, 8) and 
      ((c == a + 2 and d == b + 1) or (c == a + 1 and d == b + 2)) else 'NO')

