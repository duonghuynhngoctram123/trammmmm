# -*- coding: utf-8 -*-
"""
Created on Tue Sep  3 13:57:26 2024

@author: Administrator
"""
time_input=input("Nhap vao gio,phut,giay theo dinh dang hh:mm:ss: ")
hh, mm, ss= map(int,time_input.split(':'))
a=hh*3600+mm*60+ss
print("Tong so giay la:",a)

