
# coding: utf-8

# In[12]:


a, b = int(input()), int(input())

if (a == 0 and b != 0):
    print("NO")
elif (a == 0 and b == 0):
    print("INF")
else:
    res = -b / a
    if (res % 1 == 0):
        print(int(res))
    else:
        print("NO")

