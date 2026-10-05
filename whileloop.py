#while loop
# i=1
# while(i<=5):
#     print(i)
#     i=i+1

# 0,5,10,15,20
# i=0
# while(i<=20):
#     print(i)
#     i=i+5

#10 9 8 7 6 5
# i=10
# while(i>=5):
#     print(i)
#     i=i-1
#9 6 3 0
# i=9
# while(i>=0):
#     print(i)
#     i=i-3

#reverse of number
# n=345
# while n!=0:
#     ld=n%10
#     print(ld,end="")
#     n=n//10

#count the digits of given number
# n=4328
# count=0
# while n!=0:
#     count=count+1
#     n=n//1
# print(count)

#sum of the digits
# n=123
# new=n
# sum=0
# while n!=0:
#     ld=n%10
#     sum=sum+ld
#     n=n//10
# print(f"sum of digits in {new} is = {sum}")

#reverse of number
# n=4328
# rev=0
# while n!=0:
#     ld=n%10
#     rev=rev*10+ld
#     n=n//10
# print(rev)

#palindrome number
# n=int(input("enter the n:"))
# newnum=n
# rev=0
# while(n!=0):
#     ld=n%10
#     rev=rev*10+ld
#     n=n//10
# if(newnum==rev):
#     print("it is a palindrome")
# else:
#     print("not a palindrome")

#code for to display odd digits from given number
# n=1234
# while(n!=0):
#     ld=n%10
#     if(ld%2!=0):
#         print(ld)
#     n=n//10

#code for the even digits in given number
# n=456789
# count=0
# while(n!=0):
#     ld=n%10
#     if(ld%2==0):
#         count=count+1
#     n=n//10
# print(count)

#find the largest digit from give number
# n=452
# lar=0
# while(n!=0):
#     ld=n%10
#     if(ld>lar):
#         lar=ld
#     n=n//10
# print(lar)

#find the smallest digit from given number
# n=45213
# small=9
# while(n!=0):
#     ld=n%10
#     if(ld<small):
#         small=ld
#     n=n//10
# print(small)

# while loop task
#1.Find the sum of digits in a given number.
    #Example: 738 → 7 + 3 + 8 = 18
# n=738
# sum=0
# new=n
# while n!=0:
#     ld=n%10
#     sum=sum+ld
#     n=n//10
# print(f"sum of digits {new} is = {sum}")

#2.Find the average of digits in a given number.
   #  Example: 624 → (6 + 2 + 4) / 3 = 4
# n=624
# new=n
# sum=0
# count=0
# while n!=0:
#     ld=n%10
#     sum=sum+ld
#     count=count+1
#     n=n//10
# avg=sum/count
# print(f"avg of digits {new} is = {avg}")

#3.Find the sum of the first digit and the last digit of a given number.
    # Example: 936 → 9 + 6 = 15
# n=936
# ld=n%10
# while n>=10:
#     n=n//10
# first=n
# print(f"first and last digit sum is {ld+first}")

#4.Find the average of digits that are divisible by 5 in a given number.
     #Example: 12575 → Divisible by 5 digits: 5, 5, 5 → Average = (5 + 5 + 5) / 3 = 5
# n=int(input("enter the number:"))
# sum=0
# count=0
# while n>0:
#     ld=n%10
#     if(ld%5==0):
#         sum=sum+ld
#         count=count+1
#     n=n//10
# avg=sum/count
# print(f"Average of digits that divisible by 5 is ={avg}")


#5.Find the difference between the largest digit and the smallest digit in a given number.
     #Example: 58321 → Largest = 8, Smallest = 1 → Difference = 8 - 1 = 7
# n=int(input("Enter the number:"))
# diff=0
# lar=0
# small=9
# while n!=0:
#     ld=n%10
#     if(ld>lar):
#         lar=ld
#     if(ld<small):
#         small=ld
#     n=n//10    
# print("largest=",lar)
# print("smallest =",small)
# print(f"the difference detween the largest and smallest digit is = {lar-small}")

#end
print("hello",end="")
print("hero")