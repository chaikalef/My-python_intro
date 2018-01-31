
# coding: utf-8

# In[7]:


# Python 2 and 3 compatibility
from __future__ import (absolute_import, division,
                        print_function, unicode_literals)
from builtins import *

__author__ = "Sergey Chaika"
__email__ = "chaikalef@gmail.com"
__status__ = "Prototype"

f = open('input.txt')
s = set()

for line in f:
    line = line.strip().split(" ")
    
    for i in range(len(line)):
        s.add(line[i])
        
print(len(s))

