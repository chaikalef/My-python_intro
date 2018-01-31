
# coding: utf-8

# In[4]:


# Python 2 and 3 compatibility
from __future__ import (absolute_import, division,
                        print_function, unicode_literals)
from builtins import *

__author__ = "Sergey Chaika"
__email__ = "chaikalef@gmail.com"
__status__ = "Prototype"

print(len(set([i for i in input().split()]).intersection(set([i for i in input().split()]))))

