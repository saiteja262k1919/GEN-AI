# # class grandparents:
# #     def __init__(self,a,b):
# #         self.a=a
# #         self.b=b
# #     def land(self):
# #         print("i have a land property")
# #     def building(self):
# #         print("i have a building property")
# # class father:
# #     def __init__(self,a,b):
# #         self.a=a
# #         self.b=b
# #     def gold(self):
# #         print("i have gold property")
# #     def bike(self):
# #         print("i have a bike property")
# # class child(father,grandparents):
# #     def __init__(self,a,b,c):
# #         super().__init__(a,b)
# #         self.c=c
# #     def car(self):
# #         print("i have a car property")
# # obj1=child(10,20,30)
# # obj1.land()
# # obj1.building()
# # obj1.gold()
# # obj1.bike()
# # obj1.car()
# class grandfather:
#     def __init__(self,a):
#         self.a=a
#     def land(self):
#             print(f"i have a land in {self.a}")
# class mother:
#     def __init__(self,e):
#         self.e=e
#     def flat(self):
#         print(f" i have a flat in {self.e}")
# class father(grandfather):
#     def __init__(self,a,b):
#         super().__init__(a)
#         self.b=b
#     def building(self):
#             print(f" i have a {self.b} apartment in {self.a}")
# class son(father):
#     def __init__(self,a,b,c):
#         super().__init__(a,b)
#         self.c=c
#     def bike(self):
#             print(f" i have a {self.c} bike")
# class grandson(son,mother):
#     def __init__(self,a,b,c,d,e):
#         super().__init__(a,b,c,e)
#         self.d=d
#         self.e=e
#     def gold(self):
#             print(f"i have a {self.d} of gold")
#     def flat(self):
#             print(f" i have a flat in {self.e}")
# obj=grandson("vijayawada","3bhk","glamour",30,"hyderabad")
# obj.land()
# obj.building()
# obj.bike()
# obj.gold()

# class mother:
#     def __init__(self,a):
#         self.a=a
#     def gold(self):
#         print("i have a gold property")
# class father:
#     def __init__(self,b):
#         self.b=b
#     def land(self):
#         print("i have a land property")
# class son(father):
#     def __init__(self,b,c):
#         super().__init__(b)
#         self.c=c
#     def bike(self):
#         print("i have  a bike ")
# class daughter(mother):
#     def __init__(self,a,d):
#         super().__init__(a)
#         self.d=d
#     def scooty(self):
#         print("i have a scooty")
# obj=son(20,10)
# obj.land()
# obj.bike()
# obj1=daughter(30,40)
# obj1.gold()
# obj1.scooty()
