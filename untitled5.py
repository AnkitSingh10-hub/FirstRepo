# -*- coding: utf-8 -*-
"""
Created on Fri Jan  3 15:16:19 2020

@author: Broadway lab
"""
'''
class CSStudent:
    stream='cse'
    roll=111
    def __init__(self,roll):
        self.roll=roll
a=CSStudent(101)
b=CSStudent(102)
print(a.stream)
print(b.stream)
print(a.roll)
print(b.roll)
print(CSStudent.stream)
CSStudent.roll=10
print(CSStudent.roll)
a.stream='abc'
print(a.stream)    
print(b.stream)    

'''
'''
class CSStudent:
    stream='cse'
    def __init__(self,roll):
        self.roll=roll
    def setAddress(self,address):
        self.address=address
    def getAddress(self):
        return self.address
a=CSStudent(101)
a.setAddress("sukhedhara,ktm")
print(a.getAddress())
'''
'''
class MyClass:
    number=0
    name="noname"
def main():
    my=MyClass()
    my.number=10
    my.name="ajayyandra"
    
    
    print(my.name+""+str(my.number))
if __name__=='__main__':
    main()    
    '''
    



class abc:
    number=0
    name="noname"
 
my=abc()
print(abc().number)
       