
# coding: utf-8

# In[3]:


a = []
for i in range(3):
    a.append(int(input()))
    
# a, b, c = int(input()), int(input()), int(input())

a.sort()

print("{0} {1} {2}".format(a[0], a[1], a[2]))

