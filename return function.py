# -*- coding: utf-8 -*-
"""
Created on Sun Jan 12 16:44:57 2020

@author: Broadway lab
"""

def Hello_decorator(func):
    def inner1(*args,**kwargs):
        print("before execution")
        returned_value=func(*args,**kwargs)
        print("after execution")
        
        
        return returned_value
    
    return inner1


@Hello_decorator
def sum_two_numbers(a,b):
    print("Inside the function")
    return a+b


a,b=1,2
print("sum=",sum_two_numbers(a,b))