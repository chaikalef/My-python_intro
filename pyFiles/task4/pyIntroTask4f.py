
# coding: utf-8

# In[2]:


# Python 2 and 3 compatibility
from __future__ import (absolute_import, division,
                        print_function, unicode_literals)
from builtins import *

__author__ = "Sergey Chaika"
__email__ = "chaikalef@gmail.com"
__status__ = "Prototype"

def sum(a, b):
    if a > 0:
        return sum(a-1, b) + 1
    elif b > 0:
        return sum(a, b-1) + 1
    else:
        return 0
    
a,b = int(input()),int(input())
print(sum(a, b))

