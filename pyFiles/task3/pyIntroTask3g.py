
# coding: utf-8

# In[7]:


# Python 2 and 3 compatibility
from __future__ import (absolute_import, division,
                        print_function, unicode_literals)
from builtins import *

__author__ = "Sergey Chaika"
__email__ = "chaikalef@gmail.com"
__status__ = "Prototype"
    
s = input()
li = list(s)
res = str(li[0])

for i in range(1, len(li)):
    res += '*'
    res += str(li[i])

print(res)

