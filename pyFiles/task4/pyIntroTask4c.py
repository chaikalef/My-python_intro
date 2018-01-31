
# coding: utf-8

# In[7]:


# Python 2 and 3 compatibility
from __future__ import (absolute_import, division,
                        print_function, unicode_literals)
from builtins import *

__author__ = "Sergey Chaika"
__email__ = "chaikalef@gmail.com"
__status__ = "Prototype"

def power(a, n):
    if (n>1):
        return a * power(a, n-1)
    else:
        return a
    
b,c = float(input()),int(input())
print(power(b,c))

