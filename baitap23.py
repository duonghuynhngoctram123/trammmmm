# -*- coding: utf-8 -*-
"""
Created on Tue Sep  3 22:34:15 2024

@author: Administrator
"""

print("Giai phuong trinh bac 2:ax^2 + bx + c = 0")
a=float(input("Nhap a"))
b=float(input("Nhap b"))
c=float(input("Nhap c"))
delta= b**2-(4*a*c)
if delta<0:
    print("Phuong trinh vo nghiem" )
elif delta>0:
    print("Phuong trinh co hai nghiem phan biet x1=",(-b+math.sqrt(delta))/(2*a))
    print("Phuong trinh co hai nghiem phan biet x2=",(-b-math.sqrt(delta))/(2*a))
elif delta==0:
    print("Phuong trinh co nghiem kep x1=x2",-b/2*a)
    
    