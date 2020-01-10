# -*- coding: utf-8 -*-
"""
Created on Fri Jan 10 15:55:09 2020

@author: Broadway lab
"""

class Base(object):
    pass


class Derived(Base):
    pass
    
print(issubclass(Derived,Base))
print(issubclass(Base,Derived))

d=Derived()
b=Base()


print(isinstance(b,Derived))
print(isinstance(d,Base))    