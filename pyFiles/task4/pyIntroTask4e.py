
# coding: utf-8

# In[3]:


# Python 2 and 3 compatibility
from __future__ import (absolute_import, division,
                        print_function, unicode_literals)
from builtins import *

__author__ = "Sergey Chaika"
__email__ = "chaikalef@gmail.com"
__status__ = "Prototype"

def C(n, k):
    if (n > 0 and k > 0):
        return C(n-1,k-1) + C(n-1,k)
    elif (n == 0 and k > 0):
        return 0
    else:
        return 1
    
b,d = int(input()),int(input())
print(C(b,d))

