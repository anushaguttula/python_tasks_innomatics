#display pairs whose sum is 5 
# for j in range(1,6,1):
#     for i in range(1,6,1):
#         if(j+i==5):
#             print(f"j={j} ,i={i} ,sum={j+i}")


#range programs
#display the even numbers in the range 1 to 10
# for i in range(1,11,1):
#     n=i
#     if(n%2==0):
#         print(n)

#dispaly the odd numbers in range of 1 to 10
# print("odd numbers in range of 1 to 10:")
# for i in range(1,11,1):
#     n=i
#     if(n%2!=0):
#         print(n)


# for j in range(1,6,1):
#     n=j
#     print(f"{n}'s multiplication table:")
#     for i in range(1,11,1):
#         print(f"{n}*{i}={n*i}")

#display factorials of each number in the given range 1 to 5
#10 to 15
# for j in range (10,16,1):
#     n=j
#     fact=1
#     for i in range(1,n+1,1):
#         fact=fact*i
#     print(f"factorial of {n} : {fact}")


#print the prime numbers in the range of 1 to 100
# print("---------prime numbers in given range---------")
# for j in range (1,101,1):
#     n=j
#     count=0
#     for i in range(1,n+1,1):
#         if(n%i==0):
#             count=count+1
#     if(count==2):
#         print(n)
 
#perfect numbers in range 1 to 10000
# for j in range(1,10001,1):
#     n=j
#     sum=0
#     for i in range(1,n,1):
#         if(n%i==0):
#             sum=sum+i
#     if(sum==n):
#         print(n)


# display palindroms in range 100 to 150
# for j in range(100,151,1):
#     n=j
#     new=n
#     rev=0
#     while(n!=0):
#         ld=n%10
#         rev=rev*10+ld
#         n=n//10
#     if(new==rev):
#         print(new)

#task on range

#1.Find the sum of all prime numbers between 20 and 150.
# sum=0
# for j in range(20,151,1):
#     n=j
#     count=0
#     for i in range(1,n+1,1):
#         if(n%i==0):
#             count+=1
#     if(count==2):
#         sum=sum+n
# print(sum)

#2.Find the average of all perfect numbers between 1 and 1000.
# sump=0
# count=0
# for j in range(1,1001,1):
#     n=j
#     sum=0
#     for i in range(1,n,1):
#         if(n%i==0):
#             sum=sum+i
#     if(sum==n):
#         sump=sump+n
#         count=count+1
# avg=sump/count
# print("average of perfect numbers=",avg)

#3.Leap Years in a Range(Not Nested Loop Logic)
#Print all leap years between 1900 and 2026.
# for j in range(1990,2027,1):
#     year=j
#     if(year%400==0 or year%100!=0 and year%4==0):
#         print(year)

#4.Palindrome Numbers
#Print all palindrome numbers between 100 and 500.
# for j in range(100,501,1):
#     n=j
#     new=n
#     rev=0
#     while(n>0):
#         ld=n%10
#         rev=rev*10+ld
#         n=n//10
#     if(rev==new):
#         print(new)

#5.Digit Sum = 10
#Print all numbers between 120 and 850 whose digit sum is exactly 10.
# for j in range(120,851,1):
#     n=j
#     new=n
#     sum=0
#     while(n>0):
#         ld=n%10
#         sum=sum+ld
#         n=n//10
#     if(sum==10):
#         print(new)

#6.Pairs with Target Sum
#Print all pairs (a, b) between 1 and 50 whose sum is 30. Print each pair only once.
# for i in range(1,51,1):
#     for j in range(1,15,1):
#         a=i
#         b=j
#         if(a+b==30):
#             print(f'a={a},b={b},sum={a+b}')

#7.Exactly 3 Factors
#Print all numbers between 10 and 300 that have exactly 3 factors.
# for j in range(10,301,1):
#     n=j
#     count=0
#     for i in range(1,n+1,1):
#         if(n%i==0):
#             count=count+1
#     if(count==3):
#         print(n)

#8.Prime Factors
#Print the prime factors of every number between 20 and 50.
# for k in range(20,51,1):
#     n=k
#     print('prime factors of ',n,":",end=' ')
#     for i in range(1,n+1,1):
#         count=0
#         for j in range(1,i+1,1):
#             if(i%j==0):
#                 count=count+1
#         if n%i==0 and count==2:
#             print(i,end=' ')
#     print()

#9.Armstrong Numbers
#Print all Armstrong numbers between 100 and 999.
# for i in range(100,1000,1):
#     n=i
#     new=n
#     nd=len(str(n))
#     sum=0
#     while(n>0):
#         ld=n%10
#         sum=sum+ld**nd
#         n=n//10
#     if(sum==new):
#         print(new)

#10. Maximum Factors
# Find the number between 50 and 150 that has the maximum number of factors.
max=0
max_num=0
for j in range(50,151,1):
    n=j
    count=0
    for i in range(1,n+1,1):
        if(n%i==0):
            count=count+1
    if(count>max):
        max=count
        max_num=n
print(max_num)
print(max)