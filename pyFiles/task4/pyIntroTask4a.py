
# coding: utf-8

# In[3]:


# Python 2 and 3 compatibility
from __future__ import (absolute_import, division,
                        print_function, unicode_literals)
from builtins import *

__author__ = "Sergey Chaika"
__email__ = "chaikalef@gmail.com"
__status__ = "Prototype"

a,b,c,d=int(input()),int(input()),int(input()),int(input())

print(min(min(a,b), min(c,d)))

