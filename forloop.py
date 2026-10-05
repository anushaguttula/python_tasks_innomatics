#for loop 
#for variable in range(start,stop,step):
      #logic

# for i in range(1,4,1):
#     print("hello")

# for i in range(2,17,3):
#     print(i)

# for i in range(3,0,-1):
#     print(i)

# for i in range(100,0,-10):
#     print(i)

# n=3
# sum=0
# for i in range(1,4,1):
#     sum=sum+i
# print(f"sum is = {sum}")

# n=int(input("enter the n "))
# sum=0
# for i in range(1,n+1,1):
#     sum=sum+i
# # print("sum of first ",n,"nums=",sum)
# print(f"sum of first {n} nums = {sum}")

#find the average of first n natural numbers using for loop
# n=int(input("enter the n: "))
# sum=0
# for i in range(1,n+1,1):
#     sum=sum+i
# avg=sum/n
# print(f"average of {n} natural numbers is = {avg}")

#multiplication table
# n=int(input("enter the number :"))
# for i in range(1,11,1):
#     print(f"{n} * {i} = {n*i}")

#factorial of number
# n=int(input("enter the number:"))
# fact=1
# for i in range(n,0,-1):
#     fact=fact*i
# print(f"factorial of {n} is ={fact}")

#loops with condition
#print even numbers between 1 to 5
# n=int(input("enter the number:"))
# s=int(input("enter start value:"))
# for i in range(s,n+1,1):
#     if(i%2==0):
#         print(i)
#print odd numbers between 15 and 11
# s=15
# n=11
# for i in range(s,n-1,-1):
#     if(i%2!=0):
#         print(i)

#print numbers divisable by 5 in the range 5 to 10
# s=5
# n=10
# for i in range(s,n+1,1):
#     if(i%5==0):
#         print(i)

#count the even numbers in range 1 to 10
# count=0
# for i in range(1,11,1):
#     if(i%2==0):
#         count=count+1
# print("count of even numbers:",count)

#diplay the sum of odd numbers in the range of 5 to 10
# sum=0
# for i in range(5,11,1):
#     if(i%2!=0):
#         sum=sum+i
# print("sum of odd numbers:",sum)

#code for factors of n
# n=int(input("enter a number:"))
# print("factors of n is")
# for i in range (1,n+1,1):
#     if(n%i==0):
#         print(i)

#count the factors of given number
# n=int(input("enter a number:"))
# count=0
# for i in range (1,n+1,1):
#     if(n%i==0):
#         count=count+1     #count+=1
# print("count of factors of n is :",count)


#prime number
# n=int(input("enter a number:"))
# count=0
# for i in range(1,n+1,1):
#     if(n%i==0):
#         count=count+1
# if(count==2):
#     print(f"{n} is a prime number")
# else:
#     print(f"{n} is not a prime number")

#sum of factors
# n=int(input("enter a number:"))
# sum=0
# print("factors of n is:")
# for i in range(1,n+1,1):
#     if(n%i==0):
#         print(i)
#         sum=sum+i
# print("sum of factors of n :",sum)


#perfect number
# n=int(input("enter a number:"))
# sum=0
# for i in range(1,n,1):  #excluding last value
#     if(n%i==0):
#         sum=sum+i
# print("sum =",sum)
# if(sum==n):
#     print(f"{n} is a perfect number")
# else:
#     print(f"{n} is not a perfect number")
#For loop task
#1.Find the average of numbers from 1 to N.
   # Example: If N = 5, calculate the average of 1, 2, 3, 4, 5.
n=int(input("Enter the n :"))
sum=0
for i in range(1,n+1,1):
    sum=sum+i
avg=sum//n
print(f"average of {n} numbers is: {avg}")


#2.Find the sum of squares of numbers from 1 to N.
   # Example: If N = 5, calculate 1² + 2² + 3² + 4² + 5².
n=int(input("Enter the n: "))
sum=0
for i in range(1,n+1,1):
    sum=sum+(i**2)
print("sum = ",sum)

#3.Find the sum of cubes of numbers from 1 to N.
    #Example: If N = 5, calculate 1³ + 2³ + 3³ + 4³ + 5³.
n=int(input("Enter the n: "))
sum=0
for i in range(1,n+1,1):
    sum=sum+(i**3)
print("sum = ",sum)

#4.Calculate the power of a number without using the ** operator.
    #Example: If base = 2 and power = 5, calculate 2 × 2 × 2 × 2 × 2.
base=int(input("Enter the base value:"))
power=int(input("Enter the power value:"))
res=1
for i in range(1,power+1,1):
    res=res*base
print("power of number = ",res)

#5.Display the first N terms of the Fibonacci series.
   # Example: If N = 7, display 0, 1, 1, 2, 3, 5, 8.
n=int(input("Enter N terms :"))
a=0
b=1
for i in range(0,n,1):
    print(a,end=' ')
    c=a+b
    a=b
    b=c


#6.Display the first N terms of the series:
    # 1, 1/2, 1/3, 1/4, ...
    # Example: If N = 4, display 1, 1/2, 1/3, 1/4.
n=int(input("Enter the n:"))
for i in range(1,n+1,1):
    print(f"1/{i}")

# 7.Display the first N terms of the series:
    # 1, 11, 111, 1111, 11111, ...
    # Example: If N = 5, display 1, 11, 111, 1111, 11111.

n=int(input("enter the n:"))
num=0
for i in range(1,n+1,1):
    num=num*10+1
    print(num)

#8.Display the first N terms of the series:
    # 1, 3, 9, 27, 81, ...
    # Each term is obtained by multiplying the previous term by 3.
n=int(input("enter the n:"))
mul=1
for i in range(1,n+1,1):
    print(mul,end=' ')
    mul=mul*3