#oops syntax
'''class classname():
    name="jashuva"
    age=12
    palce="vuij"
    def fname(self):
        print("statements .......")
a=classname()
a.fname()

#class decleration
class details():
    name="jashu"
    age=32
    place="vij"
    def display(self):
        print(self.name,self.age,self.place)
a=details()
#print(dir(a))
a.display()

#object instantiation
class Details():
    def Data(self,name,age,place):
        self.name=name
        self.age=age
        self.place=place
    def Display(self):
        print(self.name,self.age,self.place)
a=Details()
#print(dir(a))
a.Data("pooja",27,"vij")
b=Details()
b.Data("jashuva",22,"vij")
a.Display()
b.Display()

#object initialization
class Details():
    def __init__(self,name,age,place):
        self.name=name
        self.age=age
        self.place=place
    def Display(self):
        print(self.name,self.age,self.place)
a=Details("jashu",23,"vij")
#print(dir(a))
a.Display()'''

'''class Details():
    def __init__(self,name,age,place):
        self.name=name
        self.age=age
        self.place=place
    def Display(self):
        print(self.name,self.age,self.place)
name=input("enter:")
age=int(input("age:"))
place=input("place:")
a=Details(name,age,place)
#print(dir(a))
a.Display()'''

'''class Details():
    def __init__(self):
        self.name=input("name")
        self.age=int(input("age"))
        self.place=input("place")
    def Display(self):
        print(self.name,self.age,self.place)
name=input("enter:")
age=int(input("age:"))
place=input("place:")
a=Details(name,age,place)
#print(dir(a))
a.Display()'''



'''we generally use it for private var 
that means  when ever we use double leading __ fro a var 
our pyhton interpreter treates it as a special var 
in order to avoid name conficts with menthosds and inner classes '''

#diff b/w _and__
'''class Employee():
    def __init__(self):
        self.name="jashuva"
        self._mailid="jasuva@gmail.com"
        self.__sal=10000
a=Employee()
print(dir(a))
print(a.name)
print(a._mailid)
print(a._Employee__sal)'''

class Employee():
    def __init__(self):
        self.name="jashuva"
        self._mailid="jasuva@gmail.com"
        self.__sal=10000
class Employee1():
    def __init__(self):
        self.name="jashuva1"
        self._mailid="jashuva1@gmail.com"
        self.__sal=15000
a=Employee()
b=Employee1()
print(b.name)
print(b._mailid)
print(b._Employee1__sal)