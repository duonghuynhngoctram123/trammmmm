# -*- coding: utf-8 -*-
"""
Created on Mon Sep  2 00:11:34 2024

@author: Administrator
"""

a=float(input("Can nang cua ban la:"))
b=float(input("Chieu cao cua ban la:"))
BMI=a/(b**2)
print("BMI=",BMI)
if BMI<18.5:
    print("Ban bi thieu can.")
if BMI>=18.5 and BMI<23:
    print("Ban co chi so binh thuong")
if BMI>=23:
    print("Ban bi thua can")