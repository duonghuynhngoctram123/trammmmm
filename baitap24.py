# -*- coding: utf-8 -*-
"""
Created on Tue Sep  3 22:45:48 2024

@author: Administrator
"""

h=int(input("Nhap gio:"))
m=int(input("Nhap phut:"))
s=int(input("Nhap giay:"))
if 0<=h<24 and 0<=m<60 and 0<=s<60:
    print("Thoi gian tren hop le")
else:
    print("Thoi gian tren khong hop le")