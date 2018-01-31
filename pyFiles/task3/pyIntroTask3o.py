
# coding: utf-8

# In[18]:


# Python 2 and 3 compatibility
from __future__ import (absolute_import, division,
                        print_function, unicode_literals)
from builtins import *

__author__ = "Sergey Chaika"
__email__ = "chaikalef@gmail.com"
__status__ = "Prototype"
    
f = open('input.txt')

# Считали из файла
input = []
for line in f:
    input.append(line.strip(" ,:;.'\n"))
    tmp = (input.pop()).split()
    for i in range(len(tmp)):
        input.append((tmp[i].strip(" ,:;.'\n")).lower())

mem = []

for i in range(len(input)):
    if (input[i] in mem):
        print(mem.count(input[i]), end = ' ')
        mem.append(input[i])
    else:
        print(0, end = ' ')
        mem.append(input[i])

