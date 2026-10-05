# class Test:
#     #parametarized constructor
#     def __init__(self,name):
#         # print('Iam a constructor')
#         # print('name =',name)
#         # print('age=',age)
#         # print('my course=',course)
#         return None
#     # def m1(self,name):
#     #     print('name=',name)
# t1=Test('Hero')
# print(t1)
# # t1.m1('hero')


# class student:
#     #creatiing instance variable
#     def __init__(self,name):
#         self.myname=name
#     def displaydata(self):
#         print('my name is:',self.myname)
# s1=student('Hero')
#s1.display()

# class student:
#     ins_name='innomatics'
#     def __init__(self,name,age,course):
#         self.myName=name
#         self.myage=age
#         self.mycourse=course
#     def displaydetails(self):
#         print('institute name:',student.ins_name)
#         print('name:',self.myName)
#         print('age:', self.myage)
#         print('course:',self.mycourse)
# s1=student('hero',22,'python')
# print('========student1=======')
# s1.displaydetails()
# s2=student('zero',23,'java')
# print('=======student2========')
# s2.displaydetails()
# s3=student('sai',24,'ds')
# print('=======student3========')
# s3.displaydetails()

#Bank object
#4=instance variables
#2=static variables
#assgin the values using constuctor
#2 other examples

# #Example-1
# class Bank:
#     bank_name='SBI'
#     bank_head='raju'
#     def __init__(self,accname,accnumber,balance,acc_type):
#         self.Baccname=accname
#         self.Baccnumber=accnumber
#         self.Bbalance=balance
#         self.Bacc_type=acc_type
#     def displaydetails(self):
#         print('Bank name:',Bank.bank_name)
#         print('Bank head name:',Bank.bank_head)
#         print('Bank account holder name:',self.Baccname)
#         print('Bank account number:',self.Baccnumber)
#         print('Bank account balance:',self.Bbalance)
#         print('Bank account type:',self.Bacc_type)
# a1=Bank('Ravi',1001,25000,'Savings')
# print('======account1=======')
# a1.displaydetails()

# a2=Bank('sujatha',1002,45000,'current')
# print('======account2=======')
# a2.displaydetails()

# a3=Bank('Ramu',1003,18000,'Savings')
# print('======account3=======')
# a3.displaydetails()

# a4=Bank('Priya',1004,75000,'Savings')
# print('======account4=======')
# a4.displaydetails()

# a5=Bank('Kiran',1005,32000,'current')
# print('======account5=======')
# a5.displaydetails()

#Example-2
# class Library:
#     lib_name='city central library'
#     lib_head='somu'
#     def __init__(self,book_name,author,price,publisher):
#         self.Lbook_name=book_name
#         self.Lauthor=author
#         self.Lprice=price
#         self.Lpublisher=publisher
#     def displaydetails(self):
#         print('library name:',Library.lib_name)
#         print('Library head:',Library.lib_head)
#         print('Book name:',self.Lbook_name)
#         print('Book author:',self.Lauthor)
#         print('Book price:', self.Lprice)
#         print('Book publisher:',self.Lpublisher)
# b1=Library('python_basics','ravikumar',450,'Tech publications')
# print('=========Book1=======')
# b1.displaydetails()

# b2=Library('Data Structures','Mark Allen',600,'pearson')
# print('=========Book2=======')
# b2.displaydetails()

# b3=Library('Machine Learning','Anitha Rao',750,'Wiely')
# print('=========Book3=======')
# b3.displaydetails()

# b4=Library('Web Development','John Smith',550,'McGraw Hill')
# print('=========Book4=======')
# b4.displaydetails()

# b5=Library('DataBase Systems','Kiran Patel',650,'Oxford Press')
# print('=========Book5=======')
# b5.displaydetails()

#Example-3
# class Hospital:
#     hosp_name='City care hospital'
#     hosp_chair_person='DR.shiva'
#     def __init__(self,Doctor_name,specialization,experince,shift):
#         self.Hhosp_name=Doctor_name
#         self.Hspecilization=specialization
#         self.Hexperince=experince
#         self.Hshift=shift
#     def displaydetails(self):
#         print('Hospital name=',Hospital.hosp_name)
#         print('Hospital chair person=',Hospital. hosp_chair_person)
#         print('Doctor name:',self.Hhosp_name)
#         print('Doctor specilization:',self.Hspecilization)
#         print('Doctor experince:',self.Hexperince)
#         print('Doctor shift:',self.Hshift)
# d1=Hospital('Ravi','Cardiologist','10 years0','Morning')
# print('======doctor1=======')
# d1.displaydetails()

# d2=Hospital('Priya','Dermatologist','6 years','Afternoon')
# print('======doctor2=======')
# d2.displaydetails()

# d3=Hospital('Suresh','Neurologist','12 years','Night')
# print('======doctor3=======')
# d3.displaydetails()

# d4=Hospital('Anitha','Pediatrician','8 years','Morning')
# print('======doctor4=======')
# d4.displaydetails()

# d5=Hospital('Kiran','Orthopedic','5 years','Evening')
# print('======doctor5=======')
# d5.displaydetails()

class Test:
    def cons(self,fname):
        print('name=',self.fname)
t1=Test()