#            Single Inheritance

#1.Single Inheritance without constructor
# class Employee:
#     def work(self):
#         print('do some work')
#     def salary(self):
#         print('take some salary')
# class Manger(Employee):
#     def assign(self):
#         print('assign the task')
#     def manages(self):
#         print('manages the work')
# m=Manger()
# m.work()
# m.salary()
# m.assign()
# m.manages()

#2.Single Inheritance with constructor
# class Animal:
#     def __init__(self,name,type):
#         self.name=name
#         self.type=type
#     def displayanimaldet(self):
#         print('animal nam:',self.name)
#         print('animal type:',self.type)
# class cat(Animal):
#     def sound(self):
#         print('sounds:meow meow...')
# c=cat('cat','Carnivora')
# c.displayanimaldet()
# c.sound()

#3.Single Inheritance with constructor + super()
# class Parent:
#     def __init__(self,house,car):
#         self.house=house
#         self.car=car
#     def dispalyparentdet(self):
#         print('Parent house:',self.house)
#         print('parent car:',self.car)
# class child(Parent):
#     def __init__(self,house,car,money,land):
#         super().__init__(house,car)
#         self.money=money
#         self.land=land
#     def displaychilddet(self):
#         super().dispalyparentdet()
#         print('child money:',self.money)
#         print('child land:',self.land)
# c=child('vella','BMW','5cr',100)
# c.displaychilddet()

#4.Single Inheritance with constructor + super()
#  using a different real-world example

# class Bankaccount:
#     bank_name='sbi'
#     def __init__(self,name,acc_no):
#         self.name=name
#         self.acc_no=acc_no
#     def displaybankacc(self):
#         print('bank name:',Bankaccount.bank_name)
#         print('bank holder name:',self.name)
#         print('bank account number:',self.acc_no)
# class savingsacc(Bankaccount):
#     def __init__(self, name, acc_no,interest_rate):
#         super().__init__(name, acc_no)
#         self.interest_rate=interest_rate
#     def displaysavings(self):
#         super().displaybankacc()
#         print('interest rate:',self.interest_rate)
# s=savingsacc('sai',12345,'6.5%')
# s.displaysavings()



#            Multiple Inheritance

#1.Multiple Inheritance without constructor
# class Employee:
#     def work(self):
#         print('do some work')
#     def salary(self):
#         print('take some salary')
# class Manger(Employee):
#     def assign(self):
#         print('assign the work')
#     def manages(self):
#         print('manages the work')
# class testingmanger(Manger):
#     def testtask(self):
#         print('assign the testing task ')
#     def testmanaging(self):
#         print('manages the only testing task')
# t=testingmanger()
# t.work()
# t.salary()
# t.assign()
# t.manages()
# t.testtask()
# t.testmanaging()

#2.Multiple Inheritance with constructor
class Animal:
    def __init__(self,name,type):
        self.name=name
        self.type=type
    def displayanima(self):
        print('Animal name:',self.name)
        print('Animal type:',self.type)
class mammal(Animal):
    def babies(self):
        print('have babies and take care of them')
class cat(mammal):
    def sound(self):
        print('sounds:meow meow...')
c=cat('cat','Carnivora')
c.displayanima()
c.babies()
c.sound()


#3.Multiple Inheritance with constructor + super()
# class product:
#     product_platform='amazon'
#     def __init__(self,name,price):
#         self.name=name
#         self.price=price
#     def displayprod(self):
#         print('product platform:',product.product_platform)
#         print('product name:',self.name)
#         print('product price:',self.price)
# class electronic(product):
#     def __init__(self,name,price,warranty):
#         super().__init__(name,price)
#         self.warranty=warranty
#     def dipalyelectronic(self):
#         super().displayprod()
#         print('warrantay:',self.warranty)
# class mobile(electronic):
#     def __init__(self,name,price,warranty,ram):
#         super().__init__(name,price,warranty)
#         self.ram=ram
#     def displaymobile(self):
#         super().dipalyelectronic()
#         print('RAM:',self.ram)
# m=mobile('mobile',20000,'2 years','8 GB')
# m.displaymobile()

#4.Multiple Inheritance with constructor + super() 
class Car:
    def __init__(self,brand,price):
        self.brand=brand
        self.price=price
    def displaycar(self):
        print('car brand:',self.brand)
        print('car price:',self.price)
class Electricvehicle(Car):
    def __init__(self,brand,price,battery):
        super().__init__(brand,price)
        self.battery=battery
    def displayelecvehicle(self):
        super().displaycar()
        print('electric battery:',self.battery)
class electriccar(Electricvehicle):
    def __init__(self,brand,price,battery,model):
        super().__init__(brand,price,battery)
        self.model=model
    def displayeleccar(self):
        super().displayelecvehicle()
        print('car model:',self.model)
ec=electriccar('Tesla',200000,'75 kwh','model 3')
ec.displayeleccar()