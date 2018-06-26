# -*- coding: utf-8 -*-
"""
Created on Sun Jan 28 16:14:12 2018

@author: Administrator
"""

#import my_abs
#student1=my_abs.Student('xiaoming',40,'kaifeng')
#print(student1.name)

class Student():
    #在类内部定义的属性属于类本身的,由操作系统只分配一块内存空间,大家公用这一块内存空间。
    count = 0
    def __init__(self,name,age):
        self._name = name
        self.age = age
        Student.count +=1
    def oout(self):
        print(self._name)


if __name__ == '__main__':
    student1 = Student("lidong",25)
    print(student1.__dict__)
    student2 = Student("wangwu",28)
    print(student2.__dict__)
    print(Student.count)