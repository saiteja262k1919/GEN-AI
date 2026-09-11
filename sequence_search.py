# # a=[5,6,7,8,9,10]
# b=int(input("enter your number "))
# for i in range(5,11):
#     if i == b:
#         print('available')
#         break
# else:
#     print('not available')
# a=input ("enter your name  :")   # rat
# b=input ("enter your name  : ")  # art
# if len(a)==len(b):
#     if sorted(a)==sorted(b):
#         print("anagram")
#     else:
#         print("not anagram")
# else:
#     print("not anagram")
# 3
# a=input("enter your string   :")
# b=a[::-1]
# if a==b:
#     print("palindrome")
# else:
#     print("not palindrome")
# # 4
# from forex_python.converter import CurrencyRates
# c = CurrencyRates()
# amount = int(input("Enter the amount: "))
# from_currency = input("From Currency: ").upper()
# to_currency = input("To Currency: ").upper()
# print(from_currency, " To ", to_currency, amount)
# result = c.convert(from_currency, to_currency, amount)
# print(result)
# # 5
# import random
# when = ['A few years ago', 'Yesterday', 'Last night', 'A long time ago','On 20th Jan']
# who = ['a rabbit', 'an elephant', 'a mouse', 'a turtle','a cat']
# name = ['Ali', 'Miriam','daniel', 'Hoouk', 'Starwalker']
# residence = ['Barcelona','India', 'Germany', 'Venice', 'England']
# went = ['cinema', 'university','seminar', 'school', 'laundry']
# happened = ['made a lot of friends','Eats a burger', 'found a secret key', 'solved a mistery', 'wrote a book']
# print(random.choice(when) + ', ' + random.choice(who) + ' that lived in ' + random.choice(residence) + ', went to the ' + random.choice(went) + ' and ' + random.choice(happened))
# # 6
# import random
# a=1234567890
# len=4
# b="".join(random.sample(str(a),len))
# print(b)
# # 7

# Height=float(input("Enter your height in centimeters: "))
# Weight=float(input("Enter your Weight in Kg: "))
# Height = Height/100
# BMI=Weight/(Height*Height)
# print("your Body Mass Index is: ",BMI)
# if(BMI>0):
# 	if(BMI<=16):
# 		print("you are severely underweight")
# 	elif(BMI<=18.5):
# 		print("you are underweight")
# 	elif(BMI<=25):
# 		print("you are Healthy")
# 	elif(BMI<=30):
# 		print("you are overweight")
# 	else: print("you are severely overweight")
# else:("enter valid details")
while True:
    a=input("enter your string  :")
    if a.lower()=='stop':
        break
    print(a)