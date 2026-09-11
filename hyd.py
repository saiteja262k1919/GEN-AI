# from kdkr import my_add
# my_sub(20,30)
# # import kdkr
# # kdkr.my_add(30,25)
# public encapsulation

# class kdkr:
#     def __init__(self,a,b):
#         self.a=a
#         self.b=b
# obj1=kdkr(20,30)
# print(obj1.a)
# print(obj1.b)

# private encapsulation        #      __ is private

# class kdkr:
#     def __init__(self,a,b):
#         self.a=a
#         self.__b=b     
# obj1=kdkr(20,30)
# print(obj1.a)
# print(obj1.__b)

#  class kdkr:
#     def __init__(self,a,b):
#         self.a=a
#         self.b=b
#     def my_data(self):
#         return self.__b
# obj1=kdkr(20,30)
# print(obj1.a)
# print(obj1.my_data())

# protect encapsulation    (_ is protect)
# class kdkr:
#     def __init__(self,a,b):
#         self.a=a
#         self._b=b   
#     def my_data(self):
#        return self.__b  
# obj1=kdkr(20,30)
# print(obj1.a)
# print(obj1._b)
# print(obj1.my_data())

# class kdkr:
#     def __init__(self,a,b):
#         self.a=a
#         self._b=b
# obj1=kdkr(20,30)
# x=obj1._b
# print(x)
# print(x*2)

# decorators

def kdkr(func):
    def ong(a, b):
        if a>100:
            print("start the process")
            result = func(a, b)
            print("completed")
            return result
        else:
            print("enter a value is more than 100")
    return ong
@kdkr
def my_add(a, b):
    return a + b
print(my_add(120, 30))