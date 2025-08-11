'''08/08/2025'''


# |////////////////////////| 20 QIYMAT QAYTARUVCHI FUNKSIYA |\\\\\\\\\\\\\\\\\\\\\\\\\|

# m1

# def toliq_ism_yasa(ism, familiya):
#     '''Toliq ism qaytaruvchi funksiya.'''
#     toliq_ism = f"{ism.title()} {familiya.title()}"
#     return toliq_ism # qiymat qaytarish uchun return operatorini ishlatamiz


# talaba1 = toliq_ism_yasa("olim", "hakimov")
# talaba2 = toliq_ism_yasa("kamoliddin",  "raximjonov")
# print(f"Darsga kelmagan talabalar: {talaba1} va {talaba2}")



# >>>--------------------------> IXTIYORIY ARGUMENTLAR <---------------------------<<<

# m2

# def toliq_ism_yasa(ism, familiya, otasining_ismi=""):
#     '''Toliq ism qaytaruvchi funksiya.'''
#     if otasining_ismi:
#         toliq_ism = f"{ism} {otasining_ismi} {familiya}"
#     else:
#         toliq_ism = f"{ism} {familiya}"
#     return toliq_ism.title()
    

# talaba1 = toliq_ism_yasa("kamoliddin", "raximjonov")
# talaba2 = toliq_ism_yasa("hasan", "husanov", "toxirovich")
# print(talaba1)
# print(talaba2)





# m3

# def avto_info(kompaniya, model, rang, korobka, yili, narxi= None):
#     avto = {
#         "kompaniya":kompaniya,
#         "model":model,
#         "rang":rang,
#         "yili":yili,
#         "narxi":narxi
#     }
#     return avto

# avto1 = avto_info("GM", "Malibu", "Qora", "Avtomat", 2018)
# avto2 = avto_info("GM", "Gentra", "Oq", "Mexanika", 2016, 15000)
# avtolar = [avto1, avto2]

# print("Onlay bozordagi mavjud avtomashinalar:")
# for avto in avtolar:
#     if avto["narxi"]:
#         narx = avto["narxi"]
#     else:
#         narx = "Noma'lum"
#     print(f"{avto["rang"]} {avto["model"]}. Narxi: {narx}")





# >>>-----------------------> FUNKSIYADAN RO'YXAT QAYTARAMIZ <---------------------<<<


# m4

# def oraliq(min, max):
#     sonlar = []
#     while min < max:
#         sonlar.append(min)
#         min += 1
#     return sonlar


# print(oraliq(0, 10))
# print(oraliq(10, 21))



# m4.1

# def oraliq(min, max, step= 1):
#     sonlar = []
#     while min<max:
#         sonlar.append(min)
#         min += step
#     return sonlar

# print(oraliq(0, 20, 2))







# >>>---------------------> FUNKSIYALARNI TSIKLDA ISHLATISH <---------------------<<<

# m5


# def avto_info(kompaniya, model, rangi, korobka, yili, narhi=None):
#     avto = {'kompaniya':kompaniya,
#             'model':model,
#             'rang':rangi,
#             'korobka':korobka,
#             'yil':yili,
#             'narh':narhi}
#     return avto

# print("Saytimizdagi avtolar ro'yxatini shakillantiramiz.")

# avtolar= []
# while True:
#     print("\nQuyidagi ma'lumotlarni kiriting",end='')
#     kompaniya=input("Ishlab chiqaruvchi: ")
#     model=input("Modeli: ")
#     rangi=input("Rangi: ")
#     korobka=input("Korobka: ")
#     yili=input("Ishlab chiqarilgan yili: ")
#     narhi=input("Narhi: ")
    
#     #Foydalanuvchi kiritdan ma'lumotlardan avto_info yordamida 
#     #lug'at shakllantirib, har bir lug'atni ro'yxatga qo'shamiz:
#     avtolar.append(avto_info(kompaniya, model, rangi, korobka, yili, narhi))
    
#     # Yana avto qo'shish-qo'shmaslikni so'raymiz
#     javob = input("Yana avto qo'shasizmi? (yes/no): ")
#     if javob=='no':
#         break


# print(avtolar)





'''09/08/2025'''


# |////////////////////////////////| AMALIYOT |\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\|


# M1


# def foydalanuvchi(ism, familiya, t_yil, t_joyi, email= " ", tel_raqam= " "):

#     my_fdict = {
#         "ism": ism,
#         "familiya": familiya,
#         "t_yil": t_yil,
#         "t_joyi": t_joyi,
#         "email": email,
#         "tel_raqam": tel_raqam,
#     }
#     return my_fdict

# talaba1 = foydalanuvchi("Kamoliddin", "Raximjonov", 2005, "Namangan")
# talaba2 = foydalanuvchi("Kai", "Su", 2005, "Namangan", "kai@gmail.com", "96325871555")
# talabalar = [talaba1, talaba2]
# for talaba in talabalar:
#     print(f"{talaba["ism"]} {talaba["familiya"]}. {talaba["t_yil"]} - yilda tug'ulgan, {2025 - talaba["t_yil"]} yoshda. {talaba["t_joyi"]} shaxrida tug'ulgan. ")






# M2


# def foydalanuvchi(ism, familiya, t_yil, t_joyi, email, tel_raqam):

#     my_fdict = {
#         "ism": ism,
#         "familiya": familiya,
#         "t_yil": t_yil,
#         "t_joyi": t_joyi,
#         "email": email,
#         "tel_raqam": tel_raqam,
#     }
#     return my_fdict

# malumotlar = []

# while True:
#     print("\nMalumotlarni kirting:\n")

#     ism = input("Ismingiz: ").lower()
#     familiya = input("Familayngiz: ").lower()
#     t_yil =int (input("Tug'ulgan yilingiz: "))
#     t_joyi = input("Tu'gulgan joyingiz: ").lower()

#     javob0 = input("Email kirtasizmi? (yes/no): ")
#     if javob0 == "yes":
#         email = input("Email: ").lower()
#     else:
#         email =("Foydalanuvchi email pochtasini tag'dim etmagan.")

#     javob1 = input("Telefon raqamingizni kiritasizmi? (yes/no): ")
#     if javob1 == "yes":
#         tel_raqam = int (input("Telefon raqamingiz: "))
#     else:
#         tel_raqam = ("Foydalanuvchi telefon raqamini tag'dim etmagan.")

#     malumotlar.append(foydalanuvchi(ism, familiya, t_yil, t_joyi, email, tel_raqam))

#     javob = input("\nYana ma'lumot qoshasizmi? (yes/no): ")
#     if javob == "no":
#         break



# for malomot in malumotlar:
#     print(f"\nIsm: {malomot["ism"].capitalize()}\n"
#           f"Familiya: {malomot["familiya"].capitalize()}\n"
#           f"Tug'ulgan yili: {malomot["t_yil"]}\n"
#           f"Yoshi: {2025 - malomot["t_yil"]} ysoh\n"
#           f"Tug'ulgan joyi: {malomot["t_joyi"].capitalize()}\n"
#           f"Email: {malomot["email"]}\n"
#           f"Telefon raqami: {malomot["tel_raqam"]}")
    
# print()





# M3

# def max(son1, son2, son3):
#     if son1 >= son2 and son1 >= son3:
#         return son1
#     elif son2 >= son1 and son2 >= son3:
#         return son2
#     else:
#         return son3
    
# natijalar = max(12, 2,21)
# print(natijalar)




# M4

# def aylana(r):
#     d = 2*r
#     P = 2 * 3.14 * r
#     S = 2 * 3.14 * r ** 2

#     my_adict = {
#         "radius": r,
#         "diametr": d,
#         "perimetr": P,
#         "yuzasi": S

#     }
#     return my_adict

# aylana1 = aylana(2)
# print("Aylana haqida ma'lumot.")
# print(f"Radiusi: {aylana1["radius"]} \nDiametri: {aylana1["diametr"]} \nPerimetri: {aylana1["perimetr"]} \nYuzasi: {aylana1["yuzasi"]}")





# M5

# def tub_son(boshlanish, tugash):
#     tublar = []
#     for son in range(boshlanish, tugash + 1):
#         if son >1:
#             tub = True
#             for i in range(2, int(son ** 0.5) + 1):
#                 if son % i == 0:
#                     tub = False
#                     break

#             if tub:
#                 tublar.append(son)
#     return tublar


# natija = tub_son(10, 5000000)
# print("Tub sonlar:", natija)






# M6


# def fibonachi(n):
#     sonlar = []
#     for x in range(n):
#         if x == 0 or x == 1:
#             sonlar.append(1)
#         else:
#             sonlar.append(sonlar[x-1] + sonlar[x-2])
#     return sonlar

# print(fibonachi(10))



