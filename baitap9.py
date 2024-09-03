# -*- coding: utf-8 -*-
"""
Created on Mon Sep  2 00:11:34 2024

@author: Administrator
"""

print("=============MENU============")
print("1.Hu tieu")
print("2.Chao long")
print("3.Banh canh")
print("4.Bun rieu")
print("5.Pho bo")
print("=============================")
a=int(input("Nhap lua chon:"))
if a==1:
    print("Mon ban chon la Hu tieu")
elif a==2:
    print("Mon ban chon la Chao long")
elif a==3:
    print("Mon ban chon la Banh  canh")
elif a==4:
    print("Mon ban chon la Bun rieu")
elif a==5:
    print("Mon ban chon la Pho bo")
elif a>4 or a<1:
    print("Mon ban chon hien chua co tren menu!")
    
    
    