'''10/08/2025'''

# >>>-------------------------> MODULNI CHAQIRIB OLISH <---------------------------<<<

# m1


# import avto_info_mod

# avto1 = avto_info_mod.avto_info("GM", "Malibu", "Qora", "avtomat", 2020, 40_000)
# avto_info_mod.info_print(avto1)




# >>>------------------------> MODULGA QISQA NOM BERISH <--------------------------<<<


# m2

# import avto_info_mod as aim

# avto1 = aim.avto_info("GM", "Cobalt", "Oq", "mexanika", 2022, 10_000)
# aim.info_print(avto1)



# >>>------------> MODUL ICIHDAN MA'LUM FUNKSIYALARNI KO'CHIRIB OLISH <------------<<<

# m3

# from avto_info_mod import avto_info, info_print

# avto1 = avto_info("BMW", "M4 compitishin", "kumush", "avtomat", 2025, "250_000 ")
# info_print(avto1)




# >>>---------------------> FUNKSIYALARGA QISQA NOM BERISH <-----------------------<<<

# m4


# from avto_info_mod import avto_info as ainfo, info_print as iprint

# avto1 = ainfo("GM", "Spark", "Kumush", "avtomat", 2020, 6_500)
# iprint(avto1)





# >>>-----------> MODUL ICHIDAGI BARCHA FUNKSIYALARNI KO'CHIRIB OLISH <------------<<<



# m5

# from avto_info_mod import*

# avto1 = avto_info("GM", "Nexia 3", "Oq", "mexanika", 2020, 8_000)
# info_print(avto1)



# |||||||||||||||||||||||||||||------ MATH MODUL ------|||||||||||||||||||||||||||||||


######################################################################################


# import math

# x = 400
# print(math.sqrt(400))

# y = 0.5
# print(math.sin(y))

# z = 0.5
# print(math.asin(z))

# q= 12
# print(math.pow(q, 12))

# s = 10
# print(math.log2(s))

# d= 10
# print(math.comb(d, 2))

# print(math.pi)

# print(math.e)



# |||||||||||||||||||||\||||||------ Random MODUL ------||||||||||||\|||||||||||||||||

######################################################################################

import random as r

son= r.randint(0, 1000)
print(son)



ismlar = ["olim", "kamoliddin", "sardor", "diyorbek", "aziz"]
ism= r.choice(ismlar)
print(ism)
print(r.choice(ism))


x= list(range(11))
print(x)
r.shuffle(x)
print(x)


# x= list(range(0, 41, 5))
# print(x)
# print(r.choice(x))
