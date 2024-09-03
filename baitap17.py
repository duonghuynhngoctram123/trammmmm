# -*- coding: utf-8 -*-
"""
Created on Tue Sep  3 16:59:10 2024

@author: Administrator
"""

a=int(input("Nhap so nguyen thu nhat"))
b=int(input("Nhap so nguyen thu hai"))
c=int(input("Nhap so nguyen thu ba"))
if a>b and a>c:
    print("So lon nhat la a=",a)
elif b>a and b>c:
    print("So lon nhat la b=",b)
else:
    print("So lon nhat la c=",c)
if a<b and b<c:
    print("So nho nhat la a=",a)
elif b<a and b<c:
    print("So nho nhat la b=",b) 
else:
    print("So nho nhat la c=",)
        