
# coding: utf-8

# In[11]:


inNum = int(input("Enter number: "))

def factorial(num):
    res = 1
    
    if num >= 2:
        for counter in range(2, num + 1):
            res *= counter
    elif num < 0:
        res = 'ValueError'
    
    return res

print(str(inNum) + "! = " + str(factorial(inNum)))

