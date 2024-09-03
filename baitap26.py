# -*- coding: utf-8 -*-
"""
Created on Tue Sep  3 22:55:18 2024

@author: Administrator
"""

a=int(input("Nhap a"))
b=int(input("Nhap b"))
c=int(input("Nhap c"))
s=0
if a>b:
    s=a
    a=b
    b=s
if a>c:
    s=a
    a=c
    c=s
if b>c:
    s=b
    b=c
    c=s
    print("Thu tu tang dan cac so la:",a,b,c)