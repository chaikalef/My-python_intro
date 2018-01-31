
# coding: utf-8

# In[18]:


# Python 2 and 3 compatibility
from __future__ import (absolute_import, division,
                        print_function, unicode_literals)
from builtins import *

__author__ = "Sergey Chaika"
__email__ = "chaikalef@gmail.com"
__status__ = "Prototype"

arr = [i for i in input().split()]

for i in range(len(arr)):
    if (i % 2 == 0):
        print(arr[i], end = ' ')

