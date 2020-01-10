# -*- coding: utf-8 -*-
"""
Created on Fri Dec 27 15:58:34 2019

@author: Broadway lab
"""

f=open("text.txt","w")
f.write("this is a written file\n")
f.write("contains two lines")
f.close()
f=open("text.txt","r")
f.seek(10)
print(f.read())
f.close()

f=open("text.txt","a")
f.seek(10)
f.append("hi")
f=open("text.txt")
print(f.read())
