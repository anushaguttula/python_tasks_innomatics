#single inheitance
# class A:
#     def m1(self):
#         print('m1 behaves softly')
# class B(A):
#     #method overriding
#     def m1(self):
#         print('m1 behaves angryly')
# # b=B()
# # b.m1()

# a=A()
# a.m1()

#multilevel inheritance
# class A:
#     def m1(self):
#         print('m1 behaves softly')
# class B(A):
#     #method overriding
#     def m1(self):
#         print('m1 behaves angryly')
# class C(B):
#     def m1(self):
#         print('m1 behaves sweetly')
    
# b=B()
# b.m1()

# a=A()
# a.m1()

# c=C()
# c.m1()

#multilevel inheritance
#camera
# class Mobile:
#     def camera(self):
#         print('camera quality: 5px')
# class SmartPhone(Mobile):
#     #overriding
#     def camera(self):
#         print('camera quality: 64px')
# class Latestsmartphone(SmartPhone):
#     #overriding
#     def camera(self):
#         print('camera quality: 200px')
# # l=Latestsmartphone()
# # l.camera()

# # s=SmartPhone()
# # s.camera()

# m=Mobile()
# m.camera()

#camera
# class Mobile:
#     def call(self):
#         print('Calling')
#     def camera(self):
#         print('camera quality: 5px')
        
# class SmartPhone(Mobile):
#     #overriding
#     def internet(self):
#         print('internet browsing')
#     def camera(self):
#         print('camera quality: 64px')
       
# class Latestsmartphone(SmartPhone):
#     #overriding
#     def fingerprint(self):
#         print('finger print')
#     def camera(self):
#         print('camera quality: 200px')
        
# l=Latestsmartphone()
# l.call()
# l.internet()
# l.fingerprint()
# l.camera()

# s=SmartPhone()
# s.camera()

# m=Mobile()
# m.camera()

#Animal
#hierarchial inheritance
# class Animal:
#     def sound(self):
#         print('Makes sound')
# class Dog(Animal):
#     def sound(self):
#         print('bow bow..')
# class cat(Animal):
#     def sound(self):
#         print('meow meow....')
# c=cat()
# c.sound()

# d=Dog()
# d.sound()

# a=Animal()
# a.sound()

#method over loading in python
#won't work


# class Test:
#     def add(self,a,b):
#         print('2 parameters')
#     def add(self,a,b,c):
#         print('3 parameters')
# t=Test()
# t.add(10,20)

#operator polymorphism
# print(10+20)    #addition
# print('hello'+'world')   #concatination
# print([1,2,3]+[4,5,6])   #merging

#polymorphism Task
#methodoverriding
#1.single inheritance

# class Employee:
#     def work(self):
#         print('Employee is working')
# class Manger(Employee):
#     #overriding
#     def work(self):
#         print('manger is managing the team')
# m=Manger()
# e=Employee()
# m.work()
# e.work()

#2.

# class Payment:
#     def pay(self):
#         print('payment being processed')
# class Upi:
#     def pay(self):
#         print('payment made through upi')
# u=Upi()
# p=Payment()
# u.pay()
# p.pay()

#3.multilevel inheritance
# class Person:
#     def role(self):
#         print('iam a person')
# class Employee(Person):
#     def role(self):
#         print('iam a employee')
# class Manger(Employee):
#     def role(self):
#         print('iam a manger')
# m=Manger()
# e=Employee()
# p=Person()
# m.role()
# e.role()
# p.role()

#4.
# class Device:
#     def __init__(self,brand):
#         self.brand=brand
#     def displaydevice(self):
#         print('device brand:',self.brand)
#     def operate(self):
#         print('Device is operating')
# class Mobile(Device):
#     def __init__(self,brand,model,price):
#         super().__init__(brand)
#         self.model=model
#         self.price=price
#     def displaymobile(self):
#          super().displaydevice()
#          print('mobile model:',self.model)
#          print('mobile price:',self.price)
#     def operate(self):
#         print('mobile is making a call')
# class Smartphone(Mobile):
#     def __init__(self,brand,model,price,storage,camera):
#         super().__init__(brand,model,price)
#         self.storage=storage
#         self.camera=camera
#     def dislaysmart(self):
#         super().displaymobile()
#         print('storage:',self.storage)
#         print('camera:',self.camera)
#     def operate(self):
#         print('smartphone is running apps')
# s=Smartphone('samsung','A55',35000,'256gb','50mp')
# s.dislaysmart()
# s.operate()
# m=Mobile('Samsung', 'A55', 35000)
# m.operate()
# d=Device('Samsung')
# d.operate()


#5.hierarchical inheritance
# class Employee:
#     def work(self):
#         print('employee do some work')
# class Developer(Employee):
#     def work(self):
#         print('Developer writes code')
# class Manager(Employee):
#     def work(self):
#         print('Manager manages team')
# m=Manager()
# d=Developer()
# e=Employee()
# m.work()
# d.work()
# e.work()

#6.Vehicle

# class Vehicle:
#     def move(self):
#         print('Vehicle can move')
# class Car:
#     def move(self):
#         print('car can move on on road')
# class Bike:
#     def move(self):
#         print('bike can move narrow places')
# b=Bike()
# c=Car()
# v=Vehicle()
# b.move()
# c.move()
# v.move()


#7.multiple inheritance
# class printer:
#     def operate(self):
#         print('prints document')
# class Scanner:
#     def operate(self):
#         print('Scans a document')
# class Mulifunctiondevice(printer,Scanner):
#     def operate(self):
#         print('do print and scan')
# m=Mulifunctiondevice()
# s=Scanner()
# p=printer()
# m.operate()
# s.operate()
# p.operate()
# print(Mulifunctiondevice.mro())