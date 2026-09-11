# # # # class kdkr():
# # # #     def __init__(self,a,b):
# # # #         self.a=a
# # # #         self.b=b
# # # #     def deposit(self):
# # # #         print(f"i have a deposit of {self.a}")
# # # # class village(kdkr):
# # # #     def __init__(self,a,b,c):
# # # #         kdkr.__init__(self,a,b)
# # # #         super().__init__(a,b)
# # # #         self.c=c
# # # #     def withdraw(self):
# # # #         print(f" i have a withdraw is {self.c}")
# # # # sai=village(1000,2000,3000)
# # # # sai.deposit()
# # # # sai.withdraw()

# # # multiple inheritance

# # # class father:
# # #     def __init__(self,a):
# # #         self.a=a
# # #     def eat(self):
# # #         print("i am eating")
# # # class mother:
# # #     def __init__(self,b):
# # #         self.b=b
# # #     def read(self):
# # #         print("i am reading")
# # # class child(father,mother):
# # #     def __init__(self,a,b,c):
# # #         father.__init__(self,a)
# # #         mother.__init__(self,b)
# # #         self.c=c
# # #     def write(self):
# # #         print("i am writing")
# # # sai=child(10,20,30)
# # # sai.eat()
# # # sai.read()
# # # sai.write()

# # # hierachical inheritance

# # class father():
# #     def __init__(self,a):
# #         self.a=a
# #     def eat(self):
# #         print("i am eating")
# # class son(father):
# #     def __init__(self,a,b):
# #         super().__init__(a)
# #         self.b=b
# #     def read(self):
# #         print("i am reading")
# # class daughter(father):
# #     def __init__(self,a,c):
# #         super().__init__(a)
# #         self.c=c
# #     def write(self):
# #         print("i am writing")
# # sai=son(10,20)
# # sai1=daughter(10,30)
# # sai.eat()
# # sai.read()
# # sai1.eat()
# # sai1.write()

# # polymorphism:

# class elementary:
#     def __init__(self,sname,slocation):
#         self.sname=sname
#         self.slocation=slocation
#     def study(self):
#         print(f"i am studying 1st class in {self.sname} at a {self.slocation}")
# class university(elementary):
#     def __init__(self,pen,pencil):
#         super().__init__(sname,slocation)
#         self.pen=pen
#         self.pencil=pencil
#     def study(self):
#         print(f"i am studying b tech")
# sai=university(10,20,30,40)
# sai.study()
