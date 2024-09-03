# -*- coding: utf-8 -*-
"""
Created on Tue Sep  3 21:29:42 2024

@author: Administrator
"""

a=int(input("Nhap so nguyen a"))
b=int(input("Nhap so nguyen b"))
c=int(input("Nhap so nguyen c"))
max=a
if b>max:
    max=b
if c>max:
    max=c
    print("Gia tri lon nhat la:",max)