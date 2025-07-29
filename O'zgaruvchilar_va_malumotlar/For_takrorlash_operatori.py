''' 22/07/2025'''

# |/////////////////////////////////// 09 FOR TAKRORLASH OPERATORI \\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\|

# m1

# mehmonlar = ["ali", "vali", "hasan", "husan", "olim"]
# for mehmon in mehmonlar:
#     print(mehmon)


# m2

# mehmonlar = ["Ali", "Vali", "Hasan", "Husan", "Olim"]
# for mehmon in mehmonlar:
#     print(f"Hurmatli {mehmon}, sizni 20 Dekabr kuni oshga taklif etamiz.")
#     print("Hurmat bilan, Palonchilar oilasi")


# m3

# mehmonlar = ["Ali", "Vali", "Husan", "Hasan", "Olim", "Kozim"]
# for mehmon in mehmonlar:
#     print(f"Hurmatli {mehmon}, sizni 20 - Dekabr kuni noxorgi oshga taklif etamiz.")
# print("Hurmat bilan, Palonchiyev oilasi\n")



# |//////////////////////////// for YORDAMIDA SONLI RO'YXATLAR BILAN ISHLASH \\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\|

# m4

# sonlar = list(range(1, 11))
# for son in sonlar:
#     print(f"{son} ning kvadrati {son ** 2} ga teng.")


# m5

# sonlar = list (range (1, 11))
# sonlar_kv = []

# for son in sonlar:
#     sonlar_kv.append(son ** 2)

# print(sonlar)
# print(sonlar_kv)



# m6 ------> for va input

# doastlar = []
# print("5 ta eng yaqin do'stingiz kim? ")
# for n in range(5):
#     doastlar.append( input(f"{n + 1} - do'stingizning ismini kiriting: "))
# print(doastlar)





'''22/07/2025'''

# |/////////////////////////////////////////// AMALIYOT \\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\|

# M1

# ismlar = ["Ali", "Vali", "Hasan", "Husan", "Olim"]
# for ism in ismlar:
#     print (f"Salom mening ismim {ism}, tanishganimdan hursandman.")
# print()


# M2

# ismlar = ["Ali", "Vali", "Hasan", "Husan", "Olim"]
# n = 0
# for ism in ismlar:
#     print(f"Salom {ism}")
#     n += 1
# print(f"Kod {n} marta takrorlandi.")


# M3

# sonlar = list(range(11, 100, 2))
# for son in sonlar:
#     print(f"Son: {son} -> shu sonning kubi: {son ** 3}")



# M4

# kinolar = []
# for kino in range(5):
#     kinolar.append( input (f"{kino + 1} - kino: "))
# print(f"Eng sevimli kinolar royhati: {kinolar }")



# M5
# n = int ( input ("Bugun necha kishi bilan suhbatlashdingiz: "))
# ismlar = []
# for ism in range(n):
#     ismlar.append(input( f" {ism + 1} Ism:  ")) 
# print(f"{ismlar}")




'''23/07/2025'''
# |/////////////////////////////// QOSHIMCHA AMALIYOT \\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\|

# >>>>>>>------------------------------------> 1–5: Oson darajadagi masalalar

# M1

# ismlar = ["Ali", "Vali", "Hasan", "Husan", "Olim"]
# for ism in ismlar:
#     print(f"Salom {ism}")


# M2

# for son in range(11, 100, 2):
#     print(f"{son} shu sonning kubi -> {son ** 3}")


# M3


# kinolar = []
# for kino  in range(5):
#     kinolar.append(input (f"{kino + 1} -> Sevimli kinolar royxati: "))
# print(f"Kinolar {kinolar}")



# M4

# n = int ( input ("Bugun necht odam bilan korishdingiz: "))
# ismlar = []
# for ism in range(n):
#     ismlar.append( input ("Ismi: "))
# print(f"Ismlar royxati {ismlar}")



# M5

# ismlar = ["Ali", "Vali", "Hasan", "Husan", "Olim"]
# n = 0
# for ism in ismlar:
#     n +=1
#     print(f"Salom, mening ismim {ism}")
# print(f"Tsikl ishlash davommiligi: {n} ")


# >>>-------------------------------------------> 6–10: O‘rta darajadagi masalalar

# M6

# kvadrt = []
# ildiz = []
# for son in range(1, 20):
#     kvadrt.append(son ** 2)
#     ildiz.append(son ** (1/2))
# print(f"sonlarning kvdrati: {kvadrt}")
# print(f"sonlarning ildizi: {ildiz}")



# M7

# ismlar = ["Ali", "Vali", "Hasan", "Husan", "Olim"]
# name = input("Ism kiriting: ")

# for ism in ismlar:
#     if ism == name:
#         print(f"Ism royxatda bor: {ism}")
#         break
# else:
#     print(f"{name} degan ism ro'yxatda yoq! ")



# M8

# matinlar = input ("Matin kiriting: ")
# teskari = ""
# for matin in reversed( matinlar):
#     teskari += matin
# print(teskari)



# M9

# b = []
# for talaba in range(5):
#     b.append(int ( input ("Talabalr baxosini kiritng: ")))
#     ort = sum(b) / len(b)
# print(f"Talabalrni o'rtacha baxosi: {ort}\n")

# for baxo in b:
#     if baxo > ort:
#         print(f"O'rtacha baxodan katta bolgan baxo: {baxo}")



# M10

# import random as rd

# list = []
# sonlar = []

# for _ in range(10):
#     son = rd.randint(0,100)
#     list.append(son)
# print(list)

# print(f"Max_son: {max(list)}")
# print(f"Min_son: {min(list)}")



# >>>------------------------------------------> 11–15: Murakkab darajadagi masalalar

# M11

# matin = input ("Matin kiriting: ")
# natija = {}

# sozlar = matin.split()
# for soz in sozlar:
#     if soz in natija:
#         natija[soz] +=1
#     else:
#         natija[soz] = 1

# for soz, soni in natija.items():
#     print(f"Matindagi takroriy qatnashgan sozlar: {soz} -> soni: {soni} ta")


# \\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\


'''
11–15: Murakkab darajadagi masalalar

11  Matndagi har bir so'z necha marta qatnashganini sanang
 Foydalanuvchidan matn kiriting. Har bir so‘z necha marta ishlatilganini aniqlang.

12 Palindrom aniqlovchi
 Foydalanuvchidan matn oling va u palindrom (teskari o‘qilganda ham bir xil) ekanini tekshiring.

13 Sonlar ro'yxatini saralash (manual)
10 ta sonli ro‘yxatni sodsir (bubble sort) algoritmi bilan o‘sish tartibida tartiblang.

14 FizzBuzz
   1 dan 100 gacha bo‘lgan sonlar orasida:

   3 ga bo‘linadigan sonlar o‘rniga “Fizz”,

   5 ga bo‘linadigan sonlar o‘rniga “Buzz”,

   Har ikkalasiga bo‘linadigan sonlar o‘rniga “FizzBuzz” chiqarilsin.

15 Tug‘ilgan yildan yosh hisoblash
   Foydalanuvchidan tug‘ilgan yilini so‘rang va hozirgi yilga qarab yoshini hisoblang.

   
##################################################################################################################################################
   
   
🔴 16–20: Ekspert darajadagi masalalar

16    Telefon kitobi (lug‘at bilan)
    Har bir inson ismi va telefon raqamini so‘rab dict (lug‘at) tuzing. Keyin foydalanuvchi ism kiritsa, unga telefon raqamini chiqaring.

17    Fibonacci sonlari
    N ta birinchi Fibonacci sonlarini ro‘yhatda qaytaring va ularni chiqarilsin.

18   Matndagi eng ko‘p ishlatilgan harfni toping
    Foydalanuvchidan matn olib, undagi eng ko‘p uchraydigan bitta harfni toping.

19    Ro‘yhatdagi elementlarni juft va toqlarga ajrating
    Berilgan sonli ro‘yxatni ikkiga ajrating: juft va toq sonlar ro‘yxatiga.

20   Mahsulotlar savati (interaktiv menyu)
    Foydalanuvchidan mahsulot nomlarini kiriting va ular bo‘yicha narxlar so‘ralib, umumiy summani hisoblang. (Lug‘at + ro‘yhatdan foydalanilsin)
'''
