'''30/072025'''

#|///////////////////////////| #14 LUG'AT BILAN TANISHUV |\\\\\\\\\\\\\\\\\\\\\\\\\\\|

# m1

# cars_0 = {"model":"saprk", "rangi":"kulrang"}
# print(cars_0["model"])
# print(cars_0["rangi"])



# m2

# talaba_0 = {"ism":"Kamoliddin", "familiya":"Raximjonov", "kurs": 3,
#              "tug'ulgan yili": 2005}

# # print(f"{talaba_0["ism"].title()} \n{talaba_0["tug'ulgan yili"]} - tug'ulgan \n{talaba_0["kurs"]} - kurs")


# yangi juftlik qoshish

# talaba_0["kurs"] = 4
# talaba_0["tug'ulgan yili"] = 2002
# print(talaba_0)



# m3

# talaba_1 = {}

# talaba_1["ism"] = "Kamoliddin Raximjonov"
# talaba_1["kurs"] = 3
# talaba_1["yosh"] = 20
# print(talaba_1)

# #print(f"Talaba: {talaba_1["ism"].title()} {talaba_1["kurs"]} - kurs")

# # qiymatni ozgartirish

# talaba_1["kurs"] = 4
# print(f"Talaba: {talaba_1["ism"].title()} {talaba_1["kurs"]} - kurs.")



# >>>------------------> KALIT SO'Z-QIYMAT JUFTLIGINI O'CHIRISH <------------------<<<

# m4

# talaba_0 = {"ism":"Kamoliddin Raximjonov", "yosh":20, "t_yil": 2005}
# print(talaba_0)
# del talaba_0["yosh"]
# print(talaba_0)



# >>>-------------------> LUG'ATNI QATORLARGA BO'LIB YOZISH <----------------------<<<



# m5

# telefon = {
#     "Ali":"Samsung",
#     "Vali":"iPhone",
#     "Olim":"Xiomi",
#     "Orif":"nokia 1202"
# }
# print(telefon)




# >>>----------------------------> get() METODI <---------------------------------<<<

# m6


# telefonlar = {
#     "Ali":"Samsung",
#     "Vali":"iPhone",
#     "Olim":"Xiomi",
#     "Orif":"nokia 1202"
# }


# # phone = telefonlar["Ali"]
# # print(f"Alining telefoni {phone}")

# phone = telefonlar.get("Hasan", "Bunday ism mavjud emas.")
# print(phone)







'''31/07/2025'''
# |///////////////////////////////////| AMALIYOT |\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\|


# M1

# mom = {"ismi":"Alya", "tug'ulgan yili": 1980, "shahar":"lododn"}
# akam = {"ismi":"ali", "tug'ulgan yili": 2000, "shahar":"berlin"}
# dad = {"ismi":"ibrohim", "tug'ulgan yili":1978, "shahar":"luksinburg"}

# print(f"Mom: {mom["ismi"].title()} {mom["tug'ulgan yili"]} - yilda tug'ulgan {mom["shahar"].title()} shahrida.")
# print(f"akam: {akam["ismi"].title()} {akam["tug'ulgan yili"]} - yilda tug'ulgan {akam["shahar"].title()} shahrida.")
# print(f"Dad: {dad["ismi"].title()} {dad["tug'ulgan yili"]} - yilda tug'ulgan {dad["shahar"].title()} shahrida.")


# M2

# taomlar = {"Dad":"qozonkabob", "Mom":"shashlik", 
#            "Me":"Samsa", "brother": "shashlik"}

# print(f"\nDad favorite food: {taomlar["Dad"].title()}\n"
#     f"Mom favorite food: {taomlar["Mom"].title()}\n"
#     f"Brother favorite food: {taomlar["brother"].title()}\n" 
#     f"Me favorite food: {taomlar["Me"].title()}")



# M3

# dict_py = {"print":"chop etish", "int":"butun sonlar", "float":"ratsionla sonlar",
#             "string":"matin", "if":"agra", "else":"aks holda", "elif":"aks holda, agar ",
#              "boolen":"mantiqiy", "dictionary":"lug'at", "list":"ro'yhat",
#               "title()":"Matinng bosh harifini kotta qilib chiqarish",
#                "upper":"katta", "lower":"kichik", "append":"qoshish", 
#                 "insert":"index orqali qoshih", "del": "qiymat orqli o'chirish",
#                   }
# print(dict_py["append"])




# M4

# dict_py = {"print":"chop etish", "int":"butun sonlar", "float":"ratsionla sonlar",
#             "string":"matin", "if":"agra", "else":"aks holda", "elif":"aks holda, agar ",
#              "boolen":"mantiqiy", "dictionary":"lug'at", "list":"ro'yhat",
#               "title()":"Matinng bosh harifini kotta qilib chiqarish",
#                "upper":"katta", "lower":"kichik", "append":"qoshish", 
#                 "insert":"index orqali qoshih", "del": "qiymat orqali o'chirish",
#                   }

# frim = input("Lug'tni kriting: ")
# dict = dict_py.get(frim, "Bunday so'z lug'atda yoq! ")
# print(dict.capitalize())



# M5

# dict_py = {"print":"chop etish", "int":"butun sonlar", "float":"ratsionla sonlar",
#             "string":"matin", "if":"agra", "else":"aks holda", "elif":"aks holda, agar ",
#              "boolen":"mantiqiy", "dictionary":"lug'at", "list":"ro'yhat",
#               "title()":"Matinng bosh harifini kotta qilib chiqarish",
#                "upper":"katta", "lower":"kichik", "append":"qoshish", 
#                 "insert":"index orqali qoshih", "del": "qiymat orqli o'chirish",
#                   }

# my_dict = input("Lug'at so'z kiriting: ").lower()
# tarijam = dict_py.get(my_dict)
# if tarijam == None:
#     print("Bunday lug'ta so'z kritilmagan! ")
# else:
#     print(f"{my_dict.capitalize()} so'zi: {tarijam.capitalize()} -> deb tarjima qilinadi.")




'''31/07/2025'''

# |///////////////////////////////| QOSHIMCH AMALIYOT |\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\|


# 1

# hayvonlar = {"qush":"chiriq - chiriq", "it":"vov - vov", "mushuk": "miyav - miyav"}

# hayvon = input("Hayvon nomini kiritng: ").lower()

# ovoz = hayvonlar.get(hayvon)

# if ovoz == None:
#     print(f"{hayvon.capitalize()} nomi hali lug'atga kiritlmagan! ")
# else:
#     print(f"{hayvon.capitalize()} -> ovozi: {ovoz}")



# 2

# my_dict = {"uzbekistan":"tashkent", "rossiya":"moskwa", "germaniya":"berlin",
#            "USA":"Washington", "yaponiya":"tokio", "koreya": "seul"}

# print("Qaysi davlat poytaxtini bilmoqchisiz.")
# davlat_nomi = input("Davlat nomi: ").lower()

# poytaxti = my_dict.get(davlat_nomi)

# if poytaxti == None:
#     print(f"{davlat_nomi.capitalize()} nomi hali kirtilmagan shunga poytaxtini bila olmaysiz. ")
# else:
#     print(f"Davlat nomi: {davlat_nomi.capitalize()} -> Poytaxti: {poytaxti.capitalize()}")



# 3

# my_dict = {"yanvar":"qish", "fevral":"qish", "dekabr":"qish",
#            "mart":"baxor", "aprel":"baxor", "may":"baxor",
#            "iyun":"yoz", "iyul":"yoz", "avgust":"yoz",
#            "sentiyabr":"kuz", "oktiyabr":"kuz", "noyabr":"kuz",
#            }

# oy_nomi = input("OY nomini kiriting: ").lower()

# fasil = my_dict.get(oy_nomi)

# if fasil == None:
#     print(f"Bunday nomli {oy_nomi.capitalize()} mvajud emas. ")
# else:
#     print(f"Fasil nomi: {fasil.capitalize()} -> Oy nomi: {oy_nomi.capitalize()}")

