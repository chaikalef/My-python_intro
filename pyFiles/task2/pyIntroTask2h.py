
# coding: utf-8

# In[24]:


a = int(input())
arr = "korov", "korova", "korovy"

if (a % 10 == 1 and a != 11):
    print(str(a) + ' ' + arr[1])
elif ((a % 10 == 2 or a % 10 == 3 or a % 10 == 4) and 
      a != 12 and a != 13 and a != 14):
    print(str(a) + ' ' + arr[2])
else:
    print(str(a) + ' ' + arr[0])

