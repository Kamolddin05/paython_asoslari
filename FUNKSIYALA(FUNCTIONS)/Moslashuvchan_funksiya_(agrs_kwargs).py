'''10/08/2025'''


# |////////////////| 22 MOSLASHUVCHAN FUNKSIYA (*args, **kwargs) |\\\\\\\\\\\\\\\\\\\|


# >>>----------------------------> *args USULI

# m1

# def summa(*sonlar):
#     yigindi = 0
#     for son in sonlar:
#         yigindi += son
#     return yigindi

# print(summa(1, 2, 3, 4, 5, 6, 7, 8 ))
# print(summa(1, 4))
# print(summa(2, 3))




# m2


# def summa(x, y, *sonlar):
#     yigindi = 0
#     for son in sonlar:
#         yigindi += son
#     return x + y + yigindi

# print(summa(1, 2, 3))
# print(summa(1, 2, 3234234, 4454))



# >>>-----------------------------> **kwargs USULI


# m3

# def avto_info(kompaniya, model, **malumotlar):

#     malumotlar["kompaniya"] = kompaniya
#     malumotlar["model"] = model
#     return malumotlar

# info = avto_info("GM", "Malibu", rangi = "qora", narxi = 1200000, yili = 2019)

# for kay, value in info.items():
#     print(f"{kay}: {value} ")
    




# |///////////////////////////////| AMALIYOT |\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\|


# M1 *agrs 

# def kopaytma(*sonlar):
#     son = 1
#     for n in sonlar:
#         son *= n
#     return son


# son1 = kopaytma(2, 3, 5, 6)
# son2 = kopaytma(5, 6, 7)
# print(son1)
# print(son2)


# M2 **kwargs

# def Talabalar_info(ism, familiya, **maluotlar):
#     maluotlar["ism"] = ism
#     maluotlar["familiya"] = familiya
#     return maluotlar

# talaba1 = Talabalar_info("Kamoliddin", "Raximjonov", kurs = 3, t_yil = 2005, yoshi = 20)
# talaba2 = Talabalar_info("Diyorbek", "Salimov", kurs = 3, t_yil = 2005, yoshi = 20)
# print()
# for key, value in talaba1.items():
#     print(f"{key.capitalize()} -> {value}")




