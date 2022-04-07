# -*- coding: utf-8 -*-
"""
Created on Thu Apr  7 12:11:05 2022

@author: Makhon Chandra
"""

a = float(input( "Enter the First Number:"))
b = float(input(" Enter the Secound Number:"))
c = float(input(" Enter the Third Number:"))

s = (a+b+c)/2
area = (s*(s-a)* (s-b)* (s-c) **0.5)

print('The area is: %0.2f' % area )