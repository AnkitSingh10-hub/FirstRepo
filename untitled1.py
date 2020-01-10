# -*- coding: utf-8 -*-
"""
Created on Fri Jan 10 15:25:34 2020

@author: Broadway lab
"""

class Base:
    def printABC(self):
        print("hi")
class Derived(Base):
    def printXYZ(self):
        print("hi2")        
        
        
d=Derived()
b=Base()
d.printABC()
d.printXYZ()
b.printABC()
