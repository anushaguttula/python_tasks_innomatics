#say hello
# def sayhello():
#     print("hello")
# sayhello()
# sayhello()
# sayhello()

#named funtion without input and without return
#defining
# def addtwo():
#     a=10
#     b=20
#     sum=a+b
#     print("funtion--- sum=",sum)
# #calling
# addtwo()

#write the code to display the samllest number from given three number
# def smallestnum():
#     a=int(input("Enter a value:"))
#     b=int(input("Enter b value:"))
#     c=int(input("Enter c value:"))
#     if(a<b<c):
#         print(f"{a} is the smallest number")
#     elif(b<a<c):
#         print(f"{b} is the smallest number")
#     else:
#         print(f"{c} is the smallest number")
# smallestnum()

#named funtion with input and without return
# def dipalyname(name):
#     print(name)
# dipalyname("prasanna")

#write the logic to check given number is even or odd
# def evenorodd(n):
#     if(n%2==0):
#         print(n,"Even number")
#     else:
#         print(n,"odd number")
# evenorodd(1)
# evenorodd(4)
# evenorodd(7)

#write the code average of three numbers
# def averageofthree(a,b,c):
#     avg=(a+b+c)/3
#     print("average=",avg)
# averageofthree(3,4,5)

#named funtion without input and with return
# def diplayname():
#     name='hero'
#     return name
# my_name=diplayname()
# print(my_name)

# def factorial():
#     n=3
#     fact=1
#     for i in range(1,n+1,1):
#         fact=fact*i
#     return fact
# # factorial_numb=factorial()
# # print(factorial_numb)
# print(factorial())
             
#write the code to return the sum of even numbers in range 1 to 10
# def sumofeven():
#     sum=0
#     for i in range(1,11,1):
#         if(i%2==0):
#             sum=sum+i
#     return sum
# print(sumofeven())

#named function with input and with return
# def displayname(name):
#     return name
# my_name=displayname('hero')
# print(my_name)

#write the logic print number is prime or not
# def checkprime(n):
    
#     count=0
#     for i in range(1,n+1,1):
#         if(n%i==0):
#             count=count+1
#     if(count==2):
#         return 'prime'
#     else:
#         return 'not prime'
# prime=checkprime(3)
# print(prime)

#Functions Task-1

#named function- without input & without return

#1. Print numbers from 1 to 20 using a for loop.
# def print_num():
#     for i in range(1,21,1):
#         print(i)
# print_num()

#2. Print all even numbers between 1 and 50.
# def print_even():
#     for i in range(1,51,1):
#         if(i%2==0):
#             print(i)
# print_even()

#3. Print all odd numbers between 1 and 50.
# def print_even():
#     for i in range(1,51,1):
#         if(i%2!=0):
#             print(i)
# print_even()

#4. Print all numbers between 1 and 100 that are divisible by 7.
# def print_num():
#     for i in range(1,101,1):
#         if(i%7==0):
#             print(i)
# print_num()

#5. Print numbers from 1 to 50, skipping multiples of 3 using continue.
# def print_mul_three():
#     for i in range(1,51,1):
#         if(i%3==0):
#             continue
#         print(i)
# print_mul_three()

#6. Print the first 5 even numbers between 1 and 50 and stop using break.
# def print_even():
#     count=0
#     for i in range(1,51,1):
#         if(i%2==0):
#             count=count+1
#             print(i)
#         if(count==5):
#             break
# print_even()

#7. Write a function to print the first 5 multiples of 7.
# def print_nums():
#     count=0
#     for i in range(1,51,1):
#         if(i%7==0):
#             count=count+1
#             print(i)
#         if(count==5):
#             break
# print_nums()

#8.Write a function to print the first 5 prime 
# numbers between 1 and 50 using a nested loop.
# def first_5_prime():
#     countp=0
#     for j in range(1,51,1):
#         n=j
#         count=0
#         for i in range(1,n+1,1):
#             if(n%i==0):
#                 count=count+1
#         if(count==2):
#             countp=countp+1
#             print(i)
#         if(countp==5):
#             break
# first_5_prime()

#9. Write a function to find and print the 
# first number between 1 and 500 whose digit sum is 10.
# def first_num():
#     for j in range(1,501,1):
#         n=j
#         new=n
#         sum=0
#         while(n>0):
#             ld=n%10
#             sum=sum+ld
#             n=n//10
#         if(sum==10):
#             print(new)
#             break
# first_num()

#10. Write a function to find and
#  print the first palindrome number between 10 and 500.
# def first_palindrom():
#     for j in range(10,501,1):
#         n=j
#         new=n
#         rev=0
#         while(n>0):
#             ld=n%10
#             rev=rev*10+ld
#             n=n//10
#         if(rev==new):
#             print(new)
#             break
# first_palindrom()

#----------Named Function — With Input & Without Return-----------
#1.Write a function that accepts n and prints numbers from 1 to n.
# def print_nums(n):
#     for i in range(1,n+1,1):
#         print(i)
# print_nums(20)

#12.prints all even numbers from 1 to n.
# def print_all_even(n):
#     for i in range(1,n+1,1):
#         if(i%2==0):
#             print(i)
# print_all_even(10)

#13.prints the multiplication table of n.
# def multiplication_table(n):
#     for i in range(1,11,1):
#         print(f"{n} x {i} = {n*i}")
# multiplication_table(8)

#14.prints all the factors of n.
# def factors_num(n):
#     for i in range(1,n+1,1):
#         if(n%i==0):
#             print(i)
# factors_num(7)

#15.prints whether the number is prime or not prime.
# def prime_or_not(n):
#     count=0
#     for i in range(1,n+1,1):
#         if(n%i==0):
#             count=count+1
#     if(count==2):
#         print("Prime number")
#     else:
#         print("Not a prime number")
# prime_or_not(5)

#16.prints the digits of n from right to left, using a while loop.
# def digits_l_r(n):
#     while(n>0):
#         ld=n%10
#         print(ld)
#         n=n//10
# digits_l_r(2341)

#17.prints the digits of n from left to right, skipping all 0 digits.
# def digits_r_1(n):
#     div=10**(len(str(n))-1)
#     while(div>0):
#         ld=n//div
#         print(ld)
#         n=n%div
#         div=div//10
# digits_r_1(502304)

#18.prints whether n is a palindrome.
# def palindrom_not(n):
#     new=n
#     rev=0
#     while(n>0):
#         ld=n%10
#         rev=rev*10+ld
#         n=n//10
#     if(rev==new):
#         print("It is a palindrom")
#     else:
#         print("It is not a palindrom number")
# palindrom_not(135)

#19.prints whether n is a perfect number.
# def perfect_not(n):
#     sum=0
#     for i in range(1,n,1):
#         if(n%i==0):
#             sum=sum+i
#     if(sum==n):
#         print("It is a perfect number")
#     else:
#         print("It is not a perfect number")
# perfect_not(5)

#20.prints whether n is an Armstrong number.
# def asrmstrong(n):
#     new=n
#     l=len(str(n))
#     sum=0
#     while(n>0):
#         ld=n%10
#         sum=sum+ld**l
#         n=n//10
#     if(sum==new):
#         print("Armstrong number")
#     else:
#         print("not a armstrong number")
# asrmstrong(152)

#--------------Named Function — Without Input & With Return---------
#21.sum of numbers from 1 to 20.
# def sum_numbers():
#     sum=0
#     for i in range(1,21,1):
#         sum=sum+i
#     return sum
# print(sum_numbers())

#22.count of even numbers between 1 and 50.
# def count_even():
#     count=0
#     for i in range(1,51,1):
#         if(i%2==0):
#             count=count+1
#     return count
# print(count_even())        

#23.count of odd numbers between 1 and 50.
# def count_even():
#     count=0
#     for i in range(1,51,1):
#         if(i%2!=0):
#             count=count+1
#     return count
# print(count_even()) 

#24.Write a function that searches from 1 to 100 and returns 
# the first number divisible by 7.

# def first_num():
#     for i in range(1,101,1):
#         if(i%7==0):
#             return i
#             break
# print(first_num())

#25.Write a function that searches from 1 to 100 and returns the 
# first number having exactly 3 factors.
# def search_fact():
#     for j in range(1,101,1):
#         n=j
#         count=0
#         for i in range(1,n+1,1):
#             if(n%i==0):
#                 count=count+1
#         if(count==3):
#             return n
#             break
# print(search_fact())

#26. Write a function that searches from 1 to 100 and returns
#  the first number whose digit sum is 10.
# def digit_sum():
#     for j in range(1,101,1):
#         n=j
#         new=n
#         sum=0
#         while(n>0):
#             ld=n%10
#             sum=sum+ld
#             n=n//10
#         if(sum==10):
#             return new
#             break
# print(digit_sum())

#27.Write a function that searches from 10 to 500 and 
# returns the first palindrome number.
# def serch_palindrom():
#     for j in range(10,501,1):
#         n=j
#         new=n
#         rev=0
#         while(n>0):
#             ld=n%10
#             rev=rev*10+ld
#             n=n//10
#         if(rev==new):
#             return new
#             break
# print(serch_palindrom())

#28.Write a function that searches from 1 to 1000 and 
# returns the first perfect number.

# def search_perfect():
#     for j in range(1,1001,1):
#         n=j
#         sum=0
#         for i in range(1,n,1):
#             if(n%i==0):
#                 sum=sum+i
#         if(sum==n):
#             return n
#             break
# print(search_perfect())

#29.Write a function that searches from 1 to 500 and returns 
# the first number containing the digit 0.

# def search_digit():
#     for j in range(1,501,1):
#         n=j
#         new=n
#         flag=0
#         while(n>0):
#             ld=n%10
#             if(ld==0):
#                 flag=1
#                 break
#             n=n//10
#         if(flag==1):
#             return new
# print(search_digit())

#30.Write a function that searches from 1 to 500
#  and returns the first number whose
#  digit sum is even and which is not divisible by 5.

# def search_num():
#     for j in range(1,501,1):
#         n=j
#         new=n
#         sum=0
#         while(n>0):
#             ld=n%10
#             sum=sum+ld
#             n=n//10
#         if(sum%2==0 and sum%5!=0):
#             return new
# print(search_num())

#-------------------Named Function — With Input & With Return--------
#31.swap two numbers
# def swap_two(a,b):
#     c=a
#     a=b
#     b=c
#     return a,b
# print(swap_two(20,30))

#32.count the number of digits in n.
# def count_digits(n):
#     new=n
#     count=0
#     while(n>0):
#         ld=n%10
#         count=count+1
#         n=n//10
#     return count
# print(count_digits(5830421))

#33.leap year or not a leap year
# def leap_year_not(year):
#     if(year%400==0 or year%100!=0 and year%4==0):
#         return 'leap year'
#     else:
#         return 'not a leap year'
# print(leap_year_not(2024))

#34.display the average of digits from the given number
# def average_digits(n):
#     new=n
#     sum=0
#     count=0
#     while(n>0):
#         ld=n%10
#         sum=sum+ld
#         count=count+1
#         n=n//10
#     avg=sum/count
#     return avg
# print(average_digits(4568))

#35.write code for the following pattern
# 543212345
#  5432345
#   54345
#    545
#     5
# def pattern(n):
#     result=''
#     for j in range(1,n+1,1):
#         for s in range(1,j,1):
#             result=result+" "
#         for i in range(n,j-1,-1):
#             result=result+str(i)
#         for k in range(j+1,n+1,1):
#             result=result+str(k)
#         result=result+'\n'
#     return result
# print(pattern(5))

#36.display the palindrome years from till the given year
# def palindrom(year):
#     result=''
#     for j in range(1,year+1,1):
#         n=j
#         new=n
#         rev=0
#         while(n>0):
#             ld=n%10
#             rev=rev*10+ld
#             n=n//10
#         if(rev==new):
#             result=result+str(new)+'\n'
#     return result
# print(palindrom(2026))

#37.Find the average of prime numbers in the range of 1 to n
# def avg_prime_nums(n):
#     sum=0
#     countp=0
#     for j in range(1,n+1,1):
#         count=0
#         for i in range(1,j+1,1):
#             if(j%i==0):
#                 count=count+1
#         if(count==2):
#             sum=sum+j
#             countp=countp+1
#     avgp=sum/countp
#     return avgp
# print(avg_prime_nums(10))

#38.Display the first armstrong  number in the range of 10 to n.
# def armstrong(n):
#     for j in range(10,n+1,1):
#         num=j
#         new=num
#         l=len(str(num))
#         sum=0
#         while(num>0):
#             ld=num%10
#             sum=sum+ld**l
#             num=num//10
#         if(sum==new):
#             return new
# print(armstrong(1000))

#39.Write the code to skip the 0 from the given number 10405
# def skip_zero(n):
#     result=''
#     while(n>0):
#         ld=n%10
#         n=n//10
#         if(ld==0):
#             continue
#         result=result+str(ld)+' '
#     return result
# print(skip_zero(10405))

#40.first digit from the left that is even.
# def firs_even(n):
#     div=10**(len(str(n))-1)
#     while(n>0):
#         ld=n//div
#         if(ld%2==0):
#             return ld
#         n=n%div
#         div=div//10
# print(firs_even(1234567))

#lambda function
#without  input and without return
# sayhello=lambda:print('hello')
# sayhello()

#with input and without return
#syntax:
#lambda parameter:expression

# dispalyname=lambda fname:print("my name is",fname)
# dispalyname('prasanna')


 #3.without input and with return
#syntax
#lamda:'value to be returned'

# displaymsg=lambda:'hello world'
# print(displaymsg())


#4.with input and with return
# displayname=lambda fname:'my name is:'+fname
# print(displayname('shravya'))

#sum of numbers
# sum=lambda a,b:f'sum={a+b}'
# print(sum(10,20))


# sayhello=lambda:print('hello')
# print(sayhello())

#lambda function with conditional statements

#syntax
#lambda:truevalue if condition else false value

# checkeven=lambda:'even' if 5%2==0 else 'odd'
# print(checkeven())

#with input and with retun

# checkeven=lambda n:'even' if n%2==0 else 'odd'
# print(checkeven(10))

#unreachable code
# def myfunction():
#     return 'hero'
#     print("statment after return")  #unreachable code
# print(myfunction())
