'''11/08/2025'''


# |/////////////////////////| 24 FUNKSIYALAR. SON'GSO'Z. |\\\\\\\\\\\\\\\\\\\\\\\\\\\|


# >>>-----------------------> lambda YOHUD NOMSIZ FUNKSIYA <-----------------------<<<

# import math

# m1

# uzunlik = lambda pi, r: 2 *pi *r
# print(uzunlik(math.pi, 10))




# m2

# product = lambda x, y: x ** y
# print(product(3, 2))



# m3

# def daraja(n):
#     return lambda x : x**n

# kvadrat = daraja(2)
# kub = daraja(3)
# print(f"3 - ning kvadrati {kvadrat(3)} ga, kub {kub(3)} ga teng")



# >>-----------------> map() funksiya


# m4

# from math import sqrt

# sonlar = list(range(11))
# ildizlar = list(map(sqrt, sonlar))
# print(ildizlar)






# m5

# sonlar = list(range(11))

# def darja2(x):
#     return x*x

# print(list(map(darja2, sonlar)))



# m6

# sonlar = list(range(10))
# kvadrat = list(map(lambda x:x*x, sonlar))
# print(kvadrat)




# m7

# a = [12, 21, 3]
# b= [21, 3, 41]
# a_plus_b = list(map(lambda x, y: x+y, a, ))
# print(a_plus_b)



# m8

# ismlar = ["hasan", "husan", "olim", "sardor", "kamoliddin"]
# print(list(map(lambda matn: matn.upper(), ismlar)))




# >>--------------------> filter() FUNKSIYASI

# m9


# import random as r

# sonlar = r.sample(range(100), 10)

# def juftmi(x):
#     return x % 2 == 0

# juf_sonlar = list (filter(juftmi, sonlar))
# print(sonlar)
# print(juf_sonlar)




# m10

# import random as r

# sonlar = r.sample(range(100), 10)
# juft_sonlar = list(filter(lambda son: son % 2 == 0, sonlar))
# print(sonlar)
# print(juft_sonlar)


# m11

# mevalar = ["olma", "nok", "anor", "banan", "shaftoli", "o'rik"]
# mevalar_b = list(filter(lambda meva: meva.startswith("a"), mevalar))
# print(mevalar_b)


# m12

# mevalar = ["olma", "nok", "anor", "banan", "shaftoli", "o'rik"]
# mevalar2 = list(filter(lambda meva: len(meva) <=5, mevalar ))
# print(mevalar2)

# mevalar3=list(filter(lambda meva:(meva.startswith('a') and meva.endswith('r')), mevalar))
# print(mevalar3)