a = input("Enter your string: ")
# result = ""
# for i in a:
#     if i.islower():
#         result=result+(i.upper())
#     else:
#         result=result+(i.lower())
# print(result)
# # b=a.swapcase()
# # print(b)
# b=a.replace(" ","-")
# print(b)
b=a.split(" ")
c="-".join(b)
print(c)
