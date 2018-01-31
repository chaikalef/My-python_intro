
# coding: utf-8

# In[12]:


a, b, c = int(input()), int(input()), int(input())
a, b = min(a, b), max(a, b)
flag = False

def searchAnswerIf_c_IsBetween_a_And_b(a, b ,c):
    while (a <= b and c >= a):
        c -= a
        b -= 1
    else:
        if (c < a):
            pass
        elif ((c % a == 0 and c // a in range(1, b + 1)) or
              (c % b == 0 and c // b in range(1, a + 1))):
                flag = True
        else:
            a, b = b, a
            while (a <= b and c >= a):
                c -= a
                b -= 1
            else:
                if (c < a):
                    pass
                elif ((c % a == 0 and c // a in range(1, b + 1)) or 
                      (c % b == 0 and c // b in range(1, a + 1))):
                        flag = True
                else:
                    pass

if (c < a):
    pass

elif ((c % a == 0 and c // a in range(1, b + 1)) or 
      (c % b == 0 and c // b in range(1, a + 1))):
        flag = True
        
elif (c > b):
    while (c > b and a > 0):
        c -= b
        a -= 1
        if ((c % a == 0 and c // a in range(1, b + 1)) or 
            (c % b == 0 and c // b in range(1, a + 1))):
                flag = True
                break
    else:
        if (a == 0):
            pass
        else:
            searchAnswerIf_c_IsBetween_a_And_b(a, b ,c)

else:
    searchAnswerIf_c_IsBetween_a_And_b(a, b ,c)
    
if (flag):
    print('YES')
else:
    print('NO')

