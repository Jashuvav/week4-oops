#polymoriphism
#operator overloading
a=2;b=5
print(a+b) #7
print(a.__add__(b)) #7
print(a.__add__(6)) #8
print(a.__mul__(b)) #10
print(a.__mul__(3)) #6
print(a.__sub__(b)) #-3
print(a.__sub__(1)) #1
print(a.__pow__(b)) #32
print(a.__pow__(2)) #4
print(a.__le__(b)) #True
print(a.__ge__(b)) #False
print(a.__eq__(b)) #False
a=[1,2,3,4,5];b=[6,7,8,9,10]
print(a+b) #[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(a.__add__(b)) #[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(a.__getitem__(2)) #3
print(b.__getitem__(4)) #10
a="Hello";b="World"
print(a+b) #HelloWorld
print(a.__add__(b)) #HelloWorld
print(a.__add__(" "+b).upper()) #HELLO WORLD

#operator overriding
class A:
    def __init__(self,a):
        self.a=a
    def __add__(self,value):
        return self.a*value.b
class B:
    def __init__(self,b):
        self.b=b
x=A(5);y=B(10)
print(x+y) #50
