# -*- coding: utf-8 -*-
"""
Created on Tue Sep  3 21:16:03 2024

@author: Administrator
"""

a=int(input("Nhap so nguyen a"))
b=int(input("Nhap so nguyen b"))
c=int(input("Nhap so nguyen c"))
d=int(input("Nhap so nguyen d"))
if a<b and a<c and a<d:
    print("Gia tri nho nhat la:",a)
elif b<a and b<c and b<d :
    print("Gia tri nho nhat la:",b)
elif c<b and c<a and c<d:
    print("Gia tri nho nhat la:",c)
elif d<c and d<b and d<c:
    print("Gia tri nho nhat la:",d)