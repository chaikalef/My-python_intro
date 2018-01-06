
# coding: utf-8

# In[6]:


inCathet1 = float(input("Enter one cathetus: "))
inCathet2 = float(input("Enter another cathetus: "))

def isErrInInput(num1, num2):
    if (num1 > 0) & (num2 > 0):
        return False
    else:
        return True

def hypotenuse(cat1, cat2):
    return (cat1 ** 2 + cat2 ** 2) ** 0.5

if not isErrInInput(inCathet1, inCathet2):
    print("Hypotenuse = " + str(hypotenuse(inCathet1, inCathet2)))
else:
    print("valueError")

