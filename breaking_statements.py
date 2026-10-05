# for i in range(1,11,1):
#     print(i)
#     if(i==5):
#         break
# i=20
# while(i<=30):
#     print(i)
#     if(i==24):
#         break
#     i=i+1
#dispaly first divisible of 5 in the range of 6 to 20
# print("first divisible of 5 in the range of 6 to 20")
# for i in range(6,21,1):

#     if(i%5==0):
#         print(i)
#         break
# print("the last number which is divisible by 3 in the range of 11 to 28:")
# for i in range(28,10,-1):
#     if(i%3==0):
#         print(i)
#         break

#first 3 number in range of 3 to 10
# c=0  
# for i in range(3,10,1):
#     c=c+1
#     print(i)
#     if(c==3):
#         break

#last even digit in number
# n=63251
# while(n>0):
#     ld=n%10
#     if(ld%2==0):
#         print(ld)
#         break
#     n=n//10
 #display the first digit which is less than 3 in given number from the right side

# n=28914
# while(n>0):
#     ld=n%10
#     if(ld<3):
#         print(ld)
#         break
#     n=n//10
#====================continue==============
# for i in range(1,11,1):
#     if(i==5):
#         continue
#     print(i)
#while loop
# i=1
# while(i<11):
#     if(i==5):
#         i=i+1
#         continue
#     print(i)
#     i=i+1
    

#write the code to skip the unlucky year from 2020 to 2026
# ul=2021
# for i in range(2020,2027,1):
#     if(i==ul):
#         continue
#     print(i)

#skip all the even numbers in range 1 to 10
# for i in range(1,11,1):
#     if(i%2==0):
#         continue
#     print(i)
#skip odd digits in the given number
# n=62341
# while(n>0):
#     ld=n%10
#     if(ld%2!=0):
#         n=n//10
#         continue
#     print(ld)
#     n=n//10


#pass
# n=11
# if(n%2==0):
#     pass
# else:
#     print("odd")

# for i in range(1,6):
#     pass

#in functions
# def function():
#     pass


#loop else
# for i in range(1,6,1):
#     print(i)
# else:
#     print("Loop Else:Loop is terminated")

# for i in range(1,6,1):
#     if(i==3):
#         break
#     else:
#         print(i)

# print("loop is terminated")
#loop else
# for i in range(1,6,1):
#     if(i==3):
#         break
#     else:
#         print(i)
# else:
#     print("loop is terminated")


# for i in range(1,6,1):
#     if(i==3):
#         continue
#     else:
#         print(i)
# else:
#     print("loop is terminated")

#break and continue task
#1.Find the first even digit from the left in 753914286.

# n=753914286
# l=len(str(n))
# for n in range (1,l+1,n//10):
#     ld=n%10
#     if(ld%2==0):
#         print(ld)
#         break

#2.Find the first prime number between 50 and 100.
# for j in range(50,101,1):
#     n=j
#     count=0
#     for i in range(1,n+1,1):
#         if(n%i==0):
#             count=count+1
#     if(count==2):
#         print(i)
#         break
#3.Find the first number whose digit sum is 10.

# for j in range(1,21,1):
#     n=j
#     new=n
#     sum=0
#     while(n>0):
#         ld=n%10
#         sum=sum+ld
#         n=n//10
#     if(sum==10):
#         print(new)
#         break

#4.Find the first number with exactly 3 divisors between 1 and 100.
# for j in range(1,101,1):
#     n=j
#     count=0
#     for i in range(1,n+1,1):
#         if(n%i==0):
#             count=count+1
#     if(count==3):
#         print(i)
#         break

#5.Stop when 3 consecutive odd numbers occur between 1 and 50.
# count=0
# for j in range(1,51,1):     
#     if(j%2!=0):
#         print(j)
#         count=count+1
#     if(count==3):
#         break

#6.Find the first palindrome between 10 and 500.
# for j in range(10,501,1):
#     n=j
#     new=n
#     rev=0
#     while(n>0):
#         ld=n%10
#         rev=rev*10+ld
#         n=n//10
#     if(rev==new):
#         print(new)
#         break
#7.Find the first perfect number between 1 and 1000.
# for j in range(1,1001,1):
#     n=j
#     sum=0
#     for i in range(1,n,1):
#         if(n%i==0):
#             sum=sum+i
#     if(sum==n):
#         print(n)
#         break
#8.Print the first 5 even numbers.
# count=0
# for j in range(1,21,1):
#     n=j
#     if(n%2==0):
#         print(n)
#         count=count+1
#     if(count==5):
#         break

#9.Print the first 5 prime numbers.
# countp=0
# for j in range(1,31,1):
#     n=j
#     count=0
#     for i in range(1,n+1,1):
#         if(n%i==0):
#             count=count+1
#     if(count==2):
#         countp=countp+1
#         print(n)
#     if(countp==5):
#         break

#10.Print the first 3 numbers divisible by 7.
# count=0
# for j in range(1,31,1):
#     n=j
#     if(n%7==0):
#         print(n)
#         count=count+1
#     if(count==3):
#         break

#continue
#1.Print 1–30, skipping even numbers.
# for i in range(1,31,1):
#     n=i
#     if(n%2==0):
#         continue
#     print(n)    

#2.Print 1–40, skipping multiples of 4.
# for i in range(1,41,1):
#     n=i
#     if(n%4==0):
#         continue
#     print(n)

#3.Print 1–30, skipping numbers from 10–20.
# for i in range(1,31,1):
#     if(10<=i<=20):
#         continue
#     print(i)

#4.Print 1–50, skipping multiples of 3.
# for i in range(1,51,1):
#     if(i%3==0):
#         continue
#     print(i)

#5.Extract 502304, skipping digit 0.
# n=502304
# while(n>0):
#     ld=n%10
#     if(ld==0):
#         n=n//10
#         continue
#     print(ld,end='')
#     n=n//10

#6.Extract 5832461, printing only even digits.
# n=5832461
# while(n>0):
#     ld=n%10
#     if(ld%2!=0):
#         n=n//10
#         continue
#     print(ld)
#     n=n//10

#7.Extract 1432578, skipping odd digits.
# n=1432578
# while(n>0):
#     ld=n%10
#     if(ld%2!=0):
#         n=n//10
#         continue
#     print(ld,end='')
#     n=n//10

#8.Print 1–200, skipping multiples of 3 or 5.
# for j in range(1,201,1):
#     n=j
#     if(n%3==0 or n%5==0):
#         continue
#     print(n)

#9.Print 1–500, skipping numbers with odd digit sum
# for j in range(1,501,1):
#     n=j
#     new=n
#     sum=0
#     while(n>0):
#         ld=n%10
#         sum=sum+ld
#         n=n//10
#     if(sum%2!=0):
#         continue
#     print(new)

#10.Print 1–500, skipping numbers containing digit 0.
# for j in range(1,501,1):
#     n=j
#     new=n
#     flag=0
#     while(n>0):
#         ld=n%10
#         if(ld==0):
#             flag=1
#             break
#         n=n//10
#     if(flag==1):
#         continue
#     print(new)

#break+continue
#1.Print 1–50, skip multiples of 3, stop at 40.
# for j in range(1,51,1):
#     n=j
#     if(n%3==0):
#         continue
#     if(n>40):
#         break
#     print(n)


#2.Print odd numbers, skip evens, stop at the first multiple of 7.
# for j in range(1,51,1):
#     n=j
#     if(n%2==0):
#         continue
#     if(n%7==0):
#         break
#     print(n)

#3.Extract 5830421, skip odd digits, stop at 0.
# n=5830421
# div=10**(len(str(n))-1)
# while(div>0):
#     ld=n//div
#     if(ld==0):
#         break
#     if(ld%2!=0):
#         n=n%div
#         div=div//10
#         continue
#     print(ld,end='')
#     n=n%div
#     div=div//10

#Extract 8325147, print digits until 5.
# n=8325147
# div=10**(len(str(n))-1)
# while(div>0):
#     ld=n//div
#     if(ld==5):
#         break
#     print(ld,end='')
#     n=n%div
#     div=div//10

#Search from 51, skip non-multiples of 9, 
# stop at the first multiple of 9.
for j in range(51,101,1):
    n=j
    if(n%9!=0):
        continue
    print(n)
    break