#inheritance
#single inheritance
'''class RBI():
    cash=100000
    def avl_cash(jash):
        print("avalible cash is",jash.cash)
        print(" avaliable cash is ",RBI.cash)

class SBI(RBI):
    pass
class HDFC(RBI):
    cash=55000
    def new_cash(jash):
        print("new cash",jash.cash+jash.cash)
        print("new and update",jash.cash+RBI.cash)
a=HDFC()
a.avl_cash()
a.new_cash()

#multiple inheritance
class Father():
    height = 5.8
    def show_height(self):
        print("height is", self.height)
class Mother():
    weight = 60
class Child(Father, Mother):
    DOB = "01-01-2000"
    def show_dob(self):
        print("DOB is", self.DOB)
c = Child()
c.show_height()
c.show_dob()'''

#multilevel inheritance
class grandparent():
    acres=100
    def show_acers(self):
        print("acers are ",self.acres)
class parent(grandparent):
    house="2 houses"
    def show_house(self):
        print("house + acers",self.house)
class child(parent):
    car="BNW"
    def show_car(self):
        print("car + house",self.car)
a=child()
a.show_house()
a.show_car()
a.show_acers()

class dog():
    
    def shepard(self):
        print("dog is shepard",self.shepard)
class bread(dog):
   
    def puppy(self):
        print("shepard is puppy",self.puppy)
class bread1(bread):
    
    def blackdog(self):
        print("black dog is a good pet",self.blackdog)
a=bread1()
a.blackdog()
a.puppy()
a.shepard()

#super()
class Parent():
    def __init__(self, name):
        self.name = name
        print("Parent constructor called")
class Child(Parent):
    def __init__(self, name, age):
        super().__init__(name)
        self.age = age
        print("Child constructor called")
c = Child("Alice", 10)
print("Name:", c.name)
print("Age:", c.age)

#encapsulation
#publicdata()
class parents():
    public_data = 10
    def public_method(self):
        print(self.public_data)
class child(parents):
    def access_public(self):
        print(self.public_data)
obj1 = child()
obj1.access_public()
obj1.public_method()

#protected data
class parents():
    _protected_data = 20
    def protected_method(self):
        print(self._protected_data)
class child(parents):
    def access_protected(self):
        print(self._protected_data)
obj1 = child()
obj1.access_protected()
obj1.protected_method()

#private data
class parents():
    __private_data = 30
    def private_method(self):
        print(self.__private_data)
class child(parents):
    def access_private(self):
        print(self._parents__private_data)
obj1 = child()
obj1.access_private()
obj1.private_method()
