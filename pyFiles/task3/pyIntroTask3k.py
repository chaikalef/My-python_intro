
# coding: utf-8

# In[1]:


# Python 2 and 3 compatibility
from __future__ import (absolute_import, division,
                        print_function, unicode_literals)
from builtins import *

__author__ = "Sergey Chaika"
__email__ = "chaikalef@gmail.com"
__status__ = "Prototype"
    
s = [int(i) for i in input().split()]
mem = set()

for i in range(len(s)):
    if (s[i] in mem):
        print('YES')
    else:
        print('NO')
        mem.add(s[i])

