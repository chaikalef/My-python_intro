
# coding: utf-8

# In[3]:


# Python 2 and 3 compatibility
from __future__ import (absolute_import, division,
                        print_function, unicode_literals)
from builtins import *

__author__ = "Sergey Chaika"
__email__ = "chaikalef@gmail.com"
__status__ = "Prototype"

s = [int(i) for i in input().split()]

mi = s.index(min(s))
ma = s.index(max(s))

s[mi], s[ma] = s[ma], s[mi]

print(*s)

