#if block

# if False:
#     print("If block id excuted")
# print("if ended")

#1.write a program to check whether it is equal to 10
# n=int(input("enter the number:"))
# if n==10:
#     print("TRUE :Equal to 10")
# print("Program Ended")

#program which gives 15% discount if the billing price is grater than 5000 in total bill
  
# bp=int(input("enter billing price:"))
# if bp>5000:
#     discount=0.15*bp
#     totalbill=bp-discount
#     print("Bill =",bp)
#     print("bill after discount :",totalbill)
# print("program ended")

#if-else

# if True:
#     print("True :if block is excuted")
# else:
#     print("False block is excuted")

# 1.check given number is eqaul to 10 or not
# n=int(input("enter the number:"))
# if(n==10):
#     print("n is equal to 10")
# else:
#     print("n is not eqaul to 10")

#2. check the given number is positive or negative

# n=int(input("enter the number:"))
# if n<0:
#     print("n is negative")
# else:
#     print("n is positive")

#3.check the biggest among two numbers
# a=int(input("enter the first number:"))
# b=int(input("enter the second number:"))
# if a>b:
#     print("a is the biggest number")
# else:
#     print("b is the biggest number")

#4.check the nuber is even or not
# n=int(input("enter the number:"))
# if n%2!=0:
#     print("n is odd number")
# else:
#     print("n is even number")

#5.check the value is vowel or not
# ch=input("enter the value : ")
# if ch=='A' or ch=='E' or ch=='I' or ch=='O' or ch=='U' or ch=='a' or ch=='e' or ch=='i' or ch=='o' or ch=='u':
#     print("ch is a vowel")
# else:
#     print("ch is not a vowel")

# 6.check gievn value is alphabet or not
# ch=input("enter the value : ")
# if ch>='A' and ch<='Z' or ch>='a' and ch<='z':
#     print("ch is a alphabet")
# else:
#     print("ch is not a alphabet")

# 7.check given value is number or not
# ch=input("enter the value : ")
# if ch>= "0" and ch<="9":
#     print("ch is digit ")
# else:
#     print("ch is not a digit")

#8.check name and password is valid or not
# name=input("enter the name : ")
# pas=input("enter the password:")
# if name=="hero" and pas=="hero@123":
#     print("login successfull")
# else:
#     print("invalid details")


#Truthy and falsy

# if(set()):
#     print("True : if block will excutes")
# else:
#     print("False: elase block will excutes")

#if-elif-else

# if(True):
#     print("Condition 1 is true: if block is excuted")
# elif(False):
#     print("condition 1 is false and cond 2 is true: 1st elif block is excuted")
# elif(False):
#      print("condition 1&2 is false and cond 3 is true: 2st elif block is excuted")
# else:
#     print("all the above conditions is false")


#1.check wether the given number is positive or negative or zero
# n=int(input("Enter the number:"))
# if(n>0):
#     print("positive number")
# elif(n<0):
#     print("negaitive number")
# else:
#     print("zero")

#2.check given charcter is alphabet,digit or symbol
# ch=input("enter the charcter:")
# if(ch>='A' and ch<="Z" or ch>='a' and ch<="z"):
#     print("charcter is alphabet")
# elif(ch>"0" and ch<="9"):
#     print("chracter is number")
# else:
#     print("charcter is symbol")

#3.display the grade based on given marks
#above 90:0
#71 to 90 :A
#51 to 70 :B
#35 to 50 :C
#below 35:Fail

# m=int(input("enter the marks :"))
# if(m>90):
#     print("Grade: O")
# elif(m>=71 and m<=90):
#     print("Grade: A")
# elif(m>=51 and m<=70):
#     print("Grade :B")
# elif(m>=35 and m<=50):
#     print("Grade : C")
# else:
#     print("Fail")

#nested if
# if(True):
#     print("Outer if block")
#     if(True):
#         print("inner if block")
#     else:
#         print("inner else block")
# else:
#     print("outer else block")

#1.check a number is even or odd only if it is positive

# n=int(input("enter the number :"))
# if(n>0):
#     print("positive number")
#     if(n%2==0):
#         print(" n is even number")
#     else:
#         print("n is odd number")
# else:
#     print("negative number")

#2.display the smallest number from given two values only if they are not equal

# a=int(input("enter the value of a:"))
# b=int(input("enter the value of b:"))
# if(a!=b):
#     print("they are not equal")
#     if(a<b):
#         print( a," is the smallest number")
#     else:
#         print( b," is the smallest number")
# else:
#     print("they are equal")

#multiple IF'S

# if(True):
#     print("1st if block")
# if(True):
#     print("2nd if block")
# if(True):
#     print("3rd if block")

#Match case
# n=7
# match n:
#     case 1:
#         print("case 1 is excuted ")
#     case 2:
#         print("case 2 is excuted ")
#     case 3:
#         print("case 3 is excuted ")
#     case 4:
#         print("case 4 is excuted ")
#     case _:
#         print("default case")
  
#1.example traffic lights
# ch=input("enter color name : ")
# match ch:
#     case "red":
#         print("Stop the vehicle")
#     case "orange":
#         print("Rady to go")
#     case "green":
#         print("Go,Have a safe ride")
#     case _:
#         print("Traffic light error")

#2.sides

# s=int(input("enter the number of sides:"))
# match s:
#     case 1:
#         print("line")
#     case 3:
#         print("traiangle")
#     case 4:
#         print("square or rectangle")
#     case 5:
#         print("pentagon")
#     case 6:
#         print("hexagon")
#     case _:
#         print("invalid number sides")

#3.days
# d=int(input("enter the number : "))
# match d:
#     case 0:
#         print("sunday")
#     case 1:
#         print("monday")
#     case 2:
#         print("tuesday")
#     case 3:
#         print("wednesday")
#     case 4:
#         print("thursday")
#     case 5:
#         print("friday")
#     case 6:
#             print("saturday")
#     case _:
#         print("invalid day number")


#4.operations

# a=int(input("enter first number:"))
# b=int(input("enter second number:"))
# print("selct an option from the given choices:")
# print("1.Add")
# print("2.Sub")
# print("3.mul")
# print("4.div")
# print("5.remainder")
# opr=int(input("Your option :"))
# match opr:
#     case 1:
#         print("sum =",a+b)
#     case 2:
#         print("sub =",a-b)
#     case 3:
#         print("mul =",a*b)
#     case 4:
#         print("div = ",a/b)
#     case 5:
#         print("remainder:",a%b)
#     case _:
#         print("invalid operator")

# Restaurant Menu
# print("-------  MENU ------")
# print("1.Biryani")
# print("2.Chicken 65")
# print("3.Veg Pulao")
# print("4.Butter Chicken")
# print("5.Panner Tikka")
# opt=int(input("Enter your choice:"))
# match opt:
#     case 1:
#         print("Item  :  Biryani ")
#         print("Price  : ₹250")
#         print("Description : A flavorful rice dish cooked with aromatic spices and chicken.")
#     case 2:
#         print("Item  :  Chicken 65")
#         print("Price  : ₹180")
#         print("Description : Crispy and spicy deep-fried chicken pieces.")
#     case 3:
#         print("Item  :  Veg Pulao")
#         print("Price  : ₹160")
#         print("Description : Fragrant basmati rice cooked with fresh vegetables and spices.")
#     case 4:
#         print("Item  :  Butter Chicken")
#         print("Price  : ₹200")
#         print("Description : Tender chicken cooked in a rich, creamy and buttery tomato gravy.")
#     case 5:
#         print("Item  :   Panner Tikka")
#         print("Price  : ₹200")
#         print("Description : Grilled paneer cubes marinated with spices and yogurt.")
#     case _:
#         print("Item is not available")

#ATM MENU
# print("----ATM MENU -----")
# print("1.Check Balance")
# print("2.Deposit")
# print("3.Withdraw")
# print("4.Exit")
# opt=int(input("Enter your choice :"))
# match opt:
#     case 1:
#         print("Current Balance : 10000")
#     case 2:
#         d=int(input("Enter deposit amount :"))
#         print("Amount deposited successfully .")
#         print("Updated Balance :",10000+d)
#     case 3:
#         w=int(input("Enter withdrawal amount: "))
#         print("Withdrawal Successful.")
#         print("Remaining Balance :",10000-w)
#     case 4:
#         print("Thank you using the ATM.")
#     case _:
#         print("Invalid case")


#1.Electricity Bill Calculator

# units=int(input("Enter electrcity bill :"))
# if (units<100):
#     print("total bill : ₹" ,units*2)
# elif(units>=101 and units<=200):
#     print("total bill : ₹",units*4)
# elif(units>=201 and units<=300):
#     print("total bill :₹" ,units*6)
# else:
#     print("total bill :₹",units*8)

# #2.Leap Year
# y=int(input("Enter Year :"))
# if(y%400==0):
#     print("Leap Year")
# elif(y%4==0 and y%100!=0):
#     print("Leap Year")
# else:
#     print("Not a leap year")
#if-else task
# 1.check given number is a 3-digit number or not 
n=int(input("enter a number"))
if(100<=n<=999):
    print("given number is 3-digit number")
else:
    print("given number is not a 3-digit number")

#2.Check whether a given number is divisible by both 3 and 5 or not.
n=int(input("Enter a number:"))
if(n%3==0 and n%5==0):
    print("Given number is divisible by 3 and 5")
else:
    print("given number is not  divisible by 3 and 5 ")
#3.Check whether a given triangle is a valid triangle or not.
     #hint :The sum of any two sides should be greater than the third side.
a=int(input("Enter first side:"))
b=int(input("Enter second side:"))
c=int(input("Enter third side:"))
if(a+b>c and b+c>a and c+a>b):
    print("given triangle is valid triangle ")
else:
    print("given triangle is not a valid triangle")

#4.Check whether a given number is a multiple of 10 or not.
n=int(input("enter the number:"))
if(n%10==0):
    print("Multiple of 10")
else:
    print("not a multiple of 10")


#if-elif-else -task
#1.Check the type of triangle based on its sides.
       # Equilateral, Isosceles, or Scalene.
a=int(input("Enter first side:"))
b=int(input("Enter second side:"))
c=int(input("Enter third side:"))
if(a==b==c):
    print("Equilateral triangle")
elif(a==b!=c or b==c!=a or c==a!=b):
    print("Isosceles triangle")
else:
    print("Scalene triangle")

#2.Calculate the electricity bill based on units consumed.
   # 0–100: ₹2/unit, 101–200: ₹3/unit, 201–300: ₹5/unit, above 300: ₹7/unit.
units=int(input("Enter electrcity bill :"))
if (units<100):
    print("total bill : ₹" ,units*2)
elif(units>=101 and units<=200):
    print("total bill : ₹",units*3)
elif(units>=201 and units<=300):
    print("total bill :₹" ,units*5)
else:
    print("total bill :₹",units*7)

#3.Display the age category.
   # Below 13 → Child, 13–19 → Teenager, 20–59 → Adult, 60 and above → Senior Citizen.
age=int(input("Enter the age:"))
if(age<13):
    print("Child")
elif(13<=age<=19):
    print("Teenager")
elif(20<=age<=59):
    print("Adult")
else:
    print("Senior Citizen")

#4.Calculate the discount based on shopping amount.
    #Below ₹1,000 → No discount, ₹1,000–₹4,999 → 10%, ₹5,000–₹9,999 → 20%, ₹10,000 and above → 30%.
amount=int(input("enter the amount:"))
if(amount<1000):
    print("No discount")
elif(1000<=amount<=4999):
    print("discount=10%")
elif(5000<=amount<=9999):
    print("discount=20%")
else:
    print("discount=30%")

#5.Display the season based on the month number.
  #  3–5 → Spring, 6–8 → Summer, 9–11 → Autumn, 12/1/2 → Winter.
month_num=int(input("Enter the month number:"))
if(3<=month_num<=5):
    print("Spring")
elif(6<=month_num<=8):
    print("Summer")
elif(9<=month_num<=11):
    print("Autuman")
else:
    print("Winter")

#6.Check whether a given year is a Leap Year or not.
    # Condition 1: year % 400 == 0
    # Condition 2: year % 4 == 0 and year % 100 != 0
y=int(input("Enter Year :"))
if(y%400==0):
    print("Leap Year")
elif(y%4==0 and y%100!=0):
    print("Leap Year")
else:
    print("Not a leap year")

#Nested if – Tasks
#1.Check whether a person is eligible to donate blood.
    #Age should be between 18 and 60. If eligible by age, weight should be above 50 kg.
age=int(input("Enter the age:"))
if(18<=age<=60):
    weight=int(input("Enter the weight:"))
    if(weight>50):
        print("eligible to donate blood")
    else:
        print("not eligible")
else:
    print("not eligible")

#2.Display the grade based on average only if the student has passed in all 4 subjects.
a=int(input("Enter the marks in maths:"))
b=int(input("enter the marks in science:"))
c=int(input("Enter the marks in social:"))
d=int(input("Enter the marks in english:"))
if(a>=35 and b>=35 and c>=35 and d>=35):
    avg=(a+b+c+d)/4
    if(avg>90):
        print("Grade= s")
    elif(81<=avg<=90):
        print("Grade=A")
    elif(71<=avg<=80):
        print("Grade=B")
    elif(61<=avg<=70):
        print("Grade=C")
    elif(51<=avg<=60):
        print("Grade=D")
    elif(41<=avg<=50):
        print("Grade=E")
    else:
        print("Fail")
else:
    print("Fail")

#.Check whether a student is eligible for a scholarship.
    #Age should be above 18. If eligible by age, score should be above 86.
age=int(input("Enter the age of student:"))
if(age>18):
    score=int(input("Enter the score:"))
    if(score>86):
        print("Eligible for a scholarship.")
    else:
        print("Not eligible")
else:
    print("Not Eligible")