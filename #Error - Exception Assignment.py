#!/usr/bin/env python
# coding: utf-8

# 1- Let us define a division operation inside a function (using def) but to get an error, define the denominator as 0. So, type except statement properly.

# In[25]:


def division(a):
    try:
        div = a/0
        return div
    except:
        print('Division on Zero is not possible')
print(division(50))


# 2- It is possible to get multiple errors after the execution of one try block. So, please define an error-exception issue with NameError.

# In[23]:


def my_message():
    try:
        code = "Python"
        return Python
    except NameError:
        return "NameError occurred."
print(my_message())


# 3- Please define a function and with this function, generate a ValueError exception simply by entering a string instead of numerical value.

# In[15]:


try:
    x = int(input("Please enter a number: "))
except ValueError:
    print('Non-numeric data in the folder.')


# 4- Write a function called circumference that takes the diameter of a circle as input and produces the circumference of the circle. Your function should use try...except to check for a type error in the event a string is passed.

# In[21]:


import numpy
try:
    r = float(input())
    circumference = 2 * numpy.pi * r
    print(circumference)
except:
    print('Please type numeric data, not a string')

