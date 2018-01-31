
# coding: utf-8

# In[8]:


# Python 2 and 3 compatibility
from __future__ import (absolute_import, division,
                        print_function, unicode_literals)
from builtins import *

__author__ = "Sergey Chaika"
__email__ = "chaikalef@gmail.com"
__status__ = "Prototype"

def IsPrime(x):
    if (x in (1,2,3,5,7)):
        return True
    elif (x in (4,6,8)):
        return False
    else:
        for i in range(2, x // 3):
            if x % i == 0:
                return False
        return True
    
b = int(input())
print('YES' if IsPrime(b) else 'NO')

