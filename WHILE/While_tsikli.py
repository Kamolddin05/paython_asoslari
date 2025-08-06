'''05/08/2025'''

# |//////////////////////////////////| While sikli |\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\|

# m1 >>----------> input() tushunchasi.

# ism = input("Ismingiz nima: ")
# print(f"Salom {ism.title()}")


# m2

# ism = input("Ismingiz nima: ")
# savol = f"Salom {ism.title()}. Yoshingiz nechida: "
# yosh = input(savol)
# print("Rahmat")






# >>>---------------------------> Sonlar va input() <------------------------------<<<

# m3

# ism = input("Ismingiz nima: ")
# savol = f"Salom {ism.title()}. Yoshingiz nechida: "
# yosh = input(savol)
# yosh = int (yosh)
# height = input("Bo'yingiz necha metr: ")
# height = float(height)





# >>>----------------------> while TSIKLI BILAN TANISHAMIZ <-----------------------<<<


# m4

# son = 1
# while son <= 5:
#     print(son, end=" ")
#     son+=1




# m5 >>----------> while va input()

# print("Kiritlga sonning kvadratini qaytaruvchi dastur. ")
# savol = "Istalgan son kiriting "
# savol += "dastur to'xtatish uchun ' exit ' deb yoz: "
# qiymat = " "
# while qiymat != "exit":
#     qiymat = input(savol)
#     if qiymat != "exti":
#         print(float(qiymat) ** 2)





# m6 >>----------> Ishora (flag)


# print("Kiritilgan sonning kvadratini qaytaruvchi dastur.")
# savol = "Istalgan son kiriting "
# savol += "(dasturni to'xtatish uchun 'exit' deb yozing): "
# ishora = True
# while ishora:
#     qiymat = input(savol)
#     if qiymat == 'exit':
#         ishora = False
#     else:
#         print(float(qiymat)**2)




# m7 >>----------> BREAK OPERATORI


# print("Kiritlgan sonning kvadratini qaytaruvchi dastur. ")
# savol = "Istalgan son kiriting "
# savol += "(dasturni tox'tatish uchun ' exit ' yozing): "

# while True:
#     qiymat = input(savol)
#     if qiymat == "exit":
#         break
#     else:
#         print(float(qiymat) ** 2)




# m8

# sonlar = list(range(1, 11))
# for son in sonlar:
#     if son == 5:
#         break
#     print(f"{son} ning kvadrati {son ** 2} ga teng. ")



  
# ''' >> while tsikli ichida bir nechta break operatori ham bo'lishi mumkin. << '''


# m9 >>----------> CONTINUE OPERATORI

# for bo'yicha 

# sonlar = list(range(1, 11))
# for son in sonlar:
#     if son == 5:
#         continue
#     print(f"{son} ning kvadrati {son ** 2} ga teng. ")





# m10

# while bo'yicha

# son = 0 
# while son < 10:
#     son +=1
#     if son == 5:
#         continue
#     else:
#         print(f"{son} ning kvadrati {son ** 2}")


# while tsikli ichida bir nechta continue operatori ham bo'lishi mumkin.






'''05/08/2025'''


# |////////////////////////////////| AMALIYOT |\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\|


# M1

# savol = "Sevgan kitobingiz kiritng"
# savol +="(barcaha kitoblar kiritb bo'lgach 'stop' deb yozing ): "

# while True:
#     kitob = input(savol)
#     if kitob == "stop":
#         break
#     print("rahmat")




# M2 >>-----> break

# while True:
#     yosh =  (input("Yoshingizni kirting: "))
#     if yosh == "exit" or yosh == "quit":
#         break

#     yosh = int (yosh) 
#     if yosh <= 7:
#         narx = 2000
#         print(f"{yosh} yoshgacha chipta narxi {narx} so'm. ")
#     elif yosh >= 7 and yosh <18:
#         narx = 3000
#         print(f"{yosh} yoshgacha chipta narxi {narx} so'm. ")
#     elif yosh >= 18 and yosh <=65:
#         narx = 10000
#         print(f"{yosh} yoshgacha chipta narxi {narx} so'm. ")
#     else:
#         narx = 0
#         print(f"{yosh} yoshdan va unda yuqorilaga chipta narxi {narx} so'm. ")

# print("Rahmat! ")




# M2.1 >>-----> ishora


# ishora = True
# while ishora:
#     yosh =  (input("Yoshingizni kirting: "))
#     if yosh == "exit" or yosh == "quit":
#         ishora = False
#         break



#     yosh = int (yosh) 
#     if yosh <= 7:
#         narx = 2000
#         print(f"{yosh} yoshgacha chipta narxi {narx} so'm. ")
#     elif yosh > 7 and yosh <18:
#         narx = 3000
#         print(f"{yosh} yoshgacha chipta narxi {narx} so'm. ")
#     elif yosh >= 18 and yosh <=65:
#         narx = 10000
#         print(f"{yosh} yoshgacha chipta narxi {narx} so'm. ")
#     else:
#         narx = 0
#         print(f"{yosh} yoshdan va unda yuqorilaga chipta narxi {narx} so'm. ")

# print("Rahmat! ")




# M3

# savol ="Kiritilgan sonning ildizini qaytaruvchi dastur.\n"
# savol += "Musbat son kiriting "
# savol += "(dasturni to'xtatish uchun 'exit' deb yozing): "

# while True:
#     qiymat = input(savol)
#     if qiymat=='exit':
#         break
#     elif float(qiymat):
#         continue
#     else:
#         ildiz = float(qiymat)**(1/2)
#         print(f"{qiymat} ning ildizi {ildiz} ga teng")















