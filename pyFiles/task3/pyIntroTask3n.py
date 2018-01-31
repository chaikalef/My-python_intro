
# coding: utf-8

# In[13]:


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

# Выделили количество n
n = int((input.pop(0)))

# Составляем двумерный массив массивов языков учеников
arr = []
for i in range(n):
    # Количество языков Мi
    Mi = int((input.pop(0)))
    arr.append([])
    
    # Выделяем языки i-ого ученика
    for j in range(Mi):
        arr[i].append(input.pop(0))
        
    arr[i] = set(arr[i])

# Нашли пересечение, объединение
cross = set(arr[0].intersection(arr[1]))
allLang = set(arr[0].union(arr[1]))

for i in range(2, len(arr)):
    cross = cross.intersection(arr[i])
    allLang = allLang.union(arr[i])
    
# Создали списки
cross = list(cross)
allLang = list(allLang)

# Вывод всего на экран
print(len(cross))
for i in range(len(cross)):
    print(cross[i])

print(len(allLang))
for i in range(len(allLang)):
    print(allLang[i])

