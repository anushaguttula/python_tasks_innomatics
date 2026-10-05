#average of three numbers
# n1=int(input("enter num 1:"))
# n2=int(input("enter num2:"))
# n3=int(input("enter num3:"))
# sum=n1+n2+n3
# avg=sum/3
# print("average of three :",avg)

# # 1.cal profit percentage
# sp=int(input("enter sp :"))
# cp=int(input("enter cp :"))
# profit=sp-cp
# pp=(profit/cp)*100
# print("profit percentage :",pp,"%")


# #2. calculating missing angle  
# a=int(input("enter angle 1:"))
# b=int(input("enter angle 2:"))
# sum=a+b
# miss=180-sum
# print('missing angle :',miss)


# #3.last digit of given number
# num=int(input("enter number :"))
# last=num%10
# print("last digit:",last)

# #4.remove last digit from number
# num=int(input("enter the number:"))
# rld=num//10
# print("number without last digit:",rld)


# #5.find the first digit of 4 digit number
# n=int(input("Enter the number:"))
# fdn=n//1000
# print("first digit of 4 digit number:",fdn)

# #6.sum of first n natural numbers
# n=int(input("Enter the number:"))
# sum=n*(n+1)/2
# print("sum of natural number:",sum)

# #7.avg of first n natural numbers
# n=int(input("Enter the number:"))
# sum=n*(n+1)/2
# avg=sum/n
# print("avg of natural number:",avg)


#8.find gross salary
# basic_sal=int(input("enter basic salary:"))
# bonus_per=int(input("enter bonus percentage:"))
# inc_per=int(input("enter incentive percentage:"))
# b=(bonus_per/100)*basic_sal
# i=(inc_per/100)*basic_sal
# gross_sal=basic_sal+b+i
# print("gross salary:",gross_sal)

#9.find salary in hand
# basic_sal=int(input("enter basic salary:"))
# bonus_per=int(input("enter bonus percentage:"))
# inc_per=int(input("enter incentive percentage:"))
# pf_per=int(input("enter pf percentage :"))
# health_per=int(input("enter health percentage :"))
# b=(bonus_per/100)*basic_sal
# i=(inc_per/100)*basic_sal
# gross_sal=basic_sal+b+i

# pf=(pf_per/100)*basic_sal
# health=(health_per/100)*basic_sal
# ded=pf+health

# salary_in=gross_sal-ded
# print("salary in hand:",salary_in)

#10.swapping two numbers 
# a=int(input("Enter a value:"))
# b=int(input("enter b value:"))
# print("Before swapping")
# print("a = ",a)
# print("b =",b)

# #swapping using three variables
# c=a
# a=b
# b=c
# print("After swapping")
# print("a = ",a)
# print("b =",b)

#swapping two numbers using two variables
a=int(input("Enter a value:"))
b=int(input("enter b value:"))
print("Before swapping")
print("a = ",a)
print("b =",b)

#swapping using three variables
# a=a+b
# b=a-b
# a=a-b

a=a*b
b=a//b
a=a//b

print("After swapping")
print("a = ",a)
print("b =", b)