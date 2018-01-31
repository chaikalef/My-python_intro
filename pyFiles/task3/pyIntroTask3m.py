
# coding: utf-8

# In[34]:


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
    input.append(line.strip())

# Выделили количество n и m
n, m = (input.pop(0)).split()
n, m = int(n), int(m)

# Составили интовское множество шаров одного человека
a = []
for i in range(n):
    a.append(int(input.pop(0)))
a = set(a)
    
# Составили интовское множество шаров другого человека
b = []
for i in range(m):
    b.append(int(input.pop(0)))
b = set(b)

# Нашли пересечение, разности
# создали список
# отсортировали список
cross = sorted(list(a.intersection(b)))
a = sorted(list(a.difference(cross)))
b = sorted(list(b.difference(cross)))

# Вывод всего на экран
print(len(cross))
for i in range(len(cross)):
    print(cross[i], end = ' ')

print()
print(len(a))
for i in range(len(a)):
    print(a[i], end = ' ')

print()    
print(len(b))
for i in range(len(b)):
    print(b[i], end = ' ')

