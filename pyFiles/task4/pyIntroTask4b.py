
# coding: utf-8

# In[5]:


# Python 2 and 3 compatibility
from __future__ import (absolute_import, division,
                        print_function, unicode_literals)
from builtins import *

__author__ = "Sergey Chaika"
__email__ = "chaikalef@gmail.com"
__status__ = "Prototype"

def IsPointInSquare(x, y):
    return (x<=0 and (y<=x+1 or y>=-x-1)) or (x>0 and (y>=x-1 or y<=-x+1))
    
a,b=float(input()),float(input())

print('YES' if IsPointInSquare(a,b) else 'NO')

