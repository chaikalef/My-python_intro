
# coding: utf-8

# In[23]:


# Python 2 and 3 compatibility
from __future__ import (absolute_import, division,
                        print_function, unicode_literals)
from builtins import *

__author__ = "Sergey Chaika"
__email__ = "chaikalef@gmail.com"
__status__ = "Prototype"

# Python general libraries
# import numpy as np
# import matplotlib.pyplot as plt
# import pandas as pd
# New library from the book Myuller A. and Gido S.
# Introduction to machine learning
# import mglearn
# Library for work with folders
# import os
# from math import gcd

# In Jupiter Notebook we can use function
# dislpay() without this line
# In another IDE we must import this function
# from IPython.display import display

# Using great features of Jupiter Notebook
# for drawing graphics
# In another IDE we must using function plt.show()
# %matplotlib notebook
# or not so interactive environment
# %matplotlib inline

# To solve the problems of correctly displaying Russian 
# inscriptions in graphs matplotlib
# plt.rc("font", family = "Verdana")

# Считываем с клавиатуры коэффициенты
a, b, c, d = int(input()), int(input()), int(input()), int(input())

for i in range(1001):
    if (a * i ** 3 + b * i ** 2 + c * i + d == 0):
        print(i)

