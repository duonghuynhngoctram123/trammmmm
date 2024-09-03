# -*- coding: utf-8 -*-
"""
Created on Sun Sep  1 23:31:33 2024

@author: Administrator
"""

a=int(input("Nhap so nguyen duong a:"))
b=int(input("Nhap so nguyen duong b:"))
if a>0 and b>0:
    x=a%b
    y=a//b
    print("chia lay phan nguyen la:",x)
    print("chia la phan du la:",y)
else:
    print("So nhap vao khong phai la so nguyen duong")
