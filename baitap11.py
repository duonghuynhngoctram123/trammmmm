# -*- coding: utf-8 -*-
"""
Created on Tue Sep  3 13:36:56 2024

@author: Administrator
"""

char_lower=input("Nhap mot ky tu thuong")
if len(char_lower)==1 and char_lower.islower():
    char_upper=char_lower.upper()
    print("Ky tu chu hoatuongung la",char_upper)
else:
    print("Hay nhap mot ky tu chu thuong khac")
    