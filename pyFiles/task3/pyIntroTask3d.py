
# coding: utf-8

# In[2]:


# Python 2 and 3 compatibility
from __future__ import (absolute_import, division,
                        print_function, unicode_literals)
from builtins import *

__author__ = "Sergey Chaika"
__email__ = "chaikalef@gmail.com"
__status__ = "Prototype"

s = input()

a = s.find('h')
b = s.rfind('h')

print(s[:a] + s[b + 1:])

