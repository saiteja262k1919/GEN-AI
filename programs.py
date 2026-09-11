# # 1 reverse of a string
# for reverse we use[::-1],same we use[::1] 
# a="kandukur_123"
# print (a[::1])
# b=""
# for i in range(len(a)-1,-1,-1):
#     b+=a[i]
# print(b)

# # 2 sentence to reverse
# a="kandukur to ongole"
# # b=""
# # for i in range(len(a)-1,-1,-1):
# #     b+=a[i]
# # print(b)
# b=print(a.split())
# c=[]
# for i in range(len(a)-1,-1,-1):
#     d=b[i]
#     e=d[::-1]
#     c.append(e)
# print(c)

# # 3 palindrome or not
# a=input("enter your string  :")
# b=a[::-1]
# if a==b:
#     print("it is a palindrome")
# else:
#     print("it is not a palindrome")

# # 4 check if is a prime number or not

# a=int(input("enter your number  :"))
# if a>1:
#     for i in range(2,a):
#         if a%i==0:
#             print("it is not a prime number")
#             break
#     else:
#         print("it is a prime number")
# else:
#     print("the number is a negative so we cannot check it is a prime number or not")

# 5  factorial of a 
# a=int(input("enter your number   :"))
# fact=1
# for i in range(1,a+1):
#     fact=fact*i
# print(fact)

# or 

# a=int(input("enter your number  :"))
# fact=1
# return 1
# if a<0:
#     print("factorial is not possible for negative number ")
# else:
#     for i in range(1,a+1):
#         fact=fact*i
#         print(fact)

# def my_factorial(n):
#     if n<0:
#         print("factorial is not possible for negative number ")
#     elif n==0 or n==1:
#          return 1
#     return n*my_factorial(n-1)
# print(my_factorial(5))

# 6 fibonacci series
# a=int(input("enter your number  :"))
# b=0
# c=1
# if a<=0:
#     print("please enter a positive number ")
# else:
#     b=0
#     c=1
#     print(b)
#     print(c)
#     for i in range(2,a):
#         d=b+c
#         print(d)
#         b=c
#         c=d
# # 7 armstrong number 
# a=int(input("enter your number :"))
# p=len(str(a))
# q=a
# total=0
# while q>0:
#     r=q%10
#     total=total+r**p
#     q//=10
# if total==a:
#     print("it is a armstrong number")
# else:
#     print("it is not a armstrong number")

# a=input("enter your string   :")
# b=['a','e','i','o','u']
# count=0
# for i in a:
#     if i in b:
#         count=count+1
# print(count)

# 8 SECOND LARGEST NUMBER In a list with sorting
# a=[1,92,3,74,45,78,98,68]
# b=sorted(a)
# print(b[-2])

# without sorting
# a=[1,92,3,74,45,78,98,68]
# n=len(a)
# for i in range(n):
#     for j in range(n-i-1):
#         if a[j]<a[j+1]:     # true
#            a[j],a[j+1]=a[j+1],a[j]
# print(a)
# print("second largest number is  :",a[1])
