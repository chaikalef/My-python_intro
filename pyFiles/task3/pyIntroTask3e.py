
# coding: utf-8

# In[10]:


# Python 2 and 3 compatibility
from __future__ import (absolute_import, division,
                        print_function, unicode_literals)
from builtins import *

__author__ = "Sergey Chaika"
__email__ = "chaikalef@gmail.com"
__status__ = "Prototype"

a = [i for i in input().split()]

for i in range(0, len(a) - 1, 2):
    a[i], a[i + 1] = a[i + 1], a[i]
    print(a[i], end = ' ')
    print(a[i + 1], end = ' ')
    
if (len(a) % 2 != 0):
    print(a[len(a) - 1])

