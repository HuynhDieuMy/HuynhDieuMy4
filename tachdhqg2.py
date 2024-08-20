# -*- coding: utf-8 -*-
"""
Created on Tue Aug 20 18:59:52 2024

@author: L13
"""
s = "Đại học Quốc gia, Khu phố 6, P. Linh Trung, Q. Thủ Đức, Tp. HCM"
s1 = s.split(", ")
for i in s1:
    print(i)
s2 = s.replace('P. ', '').replace('Q. ', '').replace('Tp. ', '').split(", ")
for u in s2:
    print(u)