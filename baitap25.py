# -*- coding: utf-8 -*-
"""
Created on Tue Sep  3 23:13:35 2024

@author: Administrator
"""

var=input("Hay nhap mot chu cai")
if len(var)==1:
    if var.islower():
        print(var.upper())
    elif var.isupper():
        print(var.islower())
    else:
        print("Day khong phai mot chu cai hop le")
else:
    print("Hay nhap mot chu cai khac")
    
            