'''04/08/2025'''

# |///////////////////////////////////| Nesting |\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\|


# m1

# car_0 = {
#     "model":"lacetti",
#     "rang":"qora",
#     "yili":2018,
#     "narxi":13_000,
#     "km":50_000,
#     "korobka":"avtomat"
# }

# car_1 = {
#     "model":"cobalt",
#     "rang":"oq",
#     "yili":2022,
#     "narxi":10_000,
#     "km":138_000,
#     "korobka":"mexanik"
# }

# car_2 = {
#     "model":"spark",
#     "rang":"oq",
#     "yili":2018,
#     "narxi":6500,
#     "km":120_000,
#     "korobka":"mexanik"
# }


# car = car_0
# print(f"{car["model"].title()}\
#       {car["rang"]} rang,\
#         {car["yili"]} - yil, {car["narxi"]}$")


# car = car_1
# print(f"{car["model"].title()}\
#       {car["rang"]} rang,\
#         {car["yili"]} - yil, {car["narxi"]}$")



# car = car_2
# print(f"{car["model"].title()}\
#       {car["rang"]} rang,\
#         {car["yili"]} - yil, {car["narxi"]}$")



# cars = [car_0, car_1, car_2]
# for car in cars:
#     print(f" {car["model"].title()}"
#           f" {car["rang"]} rang,"
#           f" {car["yili"]} - yil, narxi: {car["narxi"]}$")

# print(cars[0])


# print(cars[0]["model"])


# print(f"{cars[2]["rang"].title()} "
#       f"{cars[2]["model"]}")





# m2

# malibus = []
# for n in range(10):
#     new_car = {
#         "model":"malibu",
#         "rang":None,
#         "narx":None,
#         "yil":2020,
#         "km":0,
#         "korobka":"avto"
#     }
#     malibus.append(new_car)


# for malibu in malibus[:3]:
#     malibu["rang"] = "qizil"


# for malibu in malibus[3:6]:
#     malibu["rang"] = "qora"


# for malibu in malibus[6:]:
#     malibu["rang"] = "qora"
#     malibu["korobka"] = "mexanika"

# for malibu in malibus:
#     if malibu["korobka"] == "avto":
#         malibu["narx"] = 40000
#     else:
#         malibu["narx"] = 35000

# for malibu in malibus:
#     print(malibu)





# >>>----------------------------> LUG'AT ICHIDA RO'YXAT <-------------------------<<<

# m3


# daturchi = {
#     "ali":["python", "c++"],
#     "vali":["html", "css", "js"],
#     "hasan":["php", "sql"],
#     "husan":["python", "php"],
#     "maryam":["c++", "c#"]
# }


# for ism, tillar in daturchi.items():
#     print(f"\n{ism.title()} quydagi dasturlash tillarini biladi:")
#     for til in tillar:
#         print(til.upper())



# for ism, tillar in daturchi.items():
#     print(f"\n{ism.title()} quydagi dasturlash tillarini biladi: ")
#     for til in tillar:
#         print(til.upper(), end=' ')




# >>>-------------------------> LUG'AT ICHIDA LUG'AT <-----------------------------<<<

# m4

# hamkasblar = {
    
#     "ali":{"familiya":"valiyev",
#            "tyil": 1995,
#            "malumot":"oliy",
#            "tillar":["python", "c++"]
#            },

#     "vali":{"familiya":"aliyev",
#             "tyil":2001,
#             "malumot":"o'rta - maxsus",
#             "tillar":["html", "css", "js"]
#             },
#     "hasan":{"familiya":"husanov",
#              "tyil":1999,
#              "malumot":"o'rta - maxsus",
#              "tillar":["python", "php"]
#     }
# }

# for ism, info in hamkasblar.items():
#     print(f"\n{ism.title()} {info["familiya"].title()}, "
#           f"{info["tyil"]} - yilda tug'ulgan. "
#           f"Ma'lumoti: {info["malumot"]}. \n"
#           "Quydagi dasturlash tillarini biladi: ")
    
#     for til in info["tillar"]:
#         print(til.upper())




# |//////////////////////////////////| AMALIYOT |\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\|



# M1


# shaxslar1 = {
#     "ism":"abdulla",
#     "familiya":"qodiriy",
#     "tyil":1894,
#     "asari":"o'tkan kunlar",
#     "millati":"o'zbek",
#     "shahri":"toshkent"
# }

# shaxslar2 = {
#     "ism":"abdulhamid",
#     "familiya":"sulaymon",
#     "tyil":1897,
#     "asari":"kecha va kunduz",
#     "millati":"o'zbek",
#     "shahri":"andijon"
# }

# shaxslar3 = {
#     "ism":"erkin",
#     "familiya":"vohidov",
#     "tyil":1936,
#     "asari":"ruhlar isyoni",
#     "millati":"o'zbek",
#     "shahri":"Farg\'ona"
# }

# shaxslar4 = {
#     "ism":"o'tkir",
#     "familiya":"hoshimov",
#     "tyil":1941,
#     "asari":"dunyoning ishlari",
#     "millati":"o'zbek",
#     "shahri":"toshkent"
# }


# shaxslar = [shaxslar1, shaxslar2, shaxslar3, shaxslar4]

# for shaxs in shaxslar:
#     print(f"\nIsm: {shaxs["ism"].title()}, "
#           f"Familiya: {shaxs["familiya"].title()}, "
#           f"Tug'ulgan yili: {shaxs["tyil"]} - yil, "
#           f"Asari: {shaxs["asari"].title()}, "
#           f"Millati: {shaxs["millati"].title()}, "
#           f"Tug'ulgan shahri: {shaxs["shahri"].title()} ")





# M2


# shaxslar1 = {
#     "ism":"abdulla",
#     "familiya":"qodiriy",
#     "tyil":1894,
#     "asari":["o'tkan kunlar", "mehrobdan chayon", "jinlar bazmi", 
#              "kalvak Mahzumning xotira daftaridan", "toshpo'lat tajang nima deydi"],
#     "millati":"o'zbek",
#     "shahri":"toshkent"
# }

# shaxslar2 = {
#     "ism":"abdulhamid",
#     "familiya":"sulaymon",
#     "tyil":1897,
#     "asari":["kecha va kunduz", "buloqlar", "tong sirlari", "chein sevgi", "zanjir",
#              "milliy ruh"],
#     "millati":"o'zbek",
#     "shahri":"andijon"
# }

# shaxslar3 = {
#     "ism":"erkin",
#     "familiya":"vohidov",
#     "tyil":1936,
#     "asari":["ruhlar isyoni", "o'zbegim", "tong nafasi", "qasamyod", "istig'for",
#             "fidoying bo'lgaymiz seni, O'zbekiston!", "nido" ],
#     "millati":"o'zbek",
#     "shahri":"farg'ona"
# }

# shaxslar4 = {
#     "ism":"o'tkir",
#     "familiya":"hoshimov",
#     "tyil":1941,
#     "asari":["dunyoning ishlari", "ikki eshik orasi", "urushning so'ngi qurboni",
#              "bahor qaytmaydi", "tushda kechgan umrlar", "daftar hoshiyasidagi bitiklar",
#              "hayotiy haqiqat"],
#     "millati":"o'zbek",
#     "shahri":"toshkent"
# }


# shaxslar = [shaxslar1, shaxslar2, shaxslar3, shaxslar4]

# for shaxs in shaxslar:
#     ism = shaxs["ism"]
#     familiya = shaxs["familiya"]
#     asarlar = shaxs["asari"]
#     print(f"\n{ism.capitalize()} {familiya.capitalize()} ning asarlari: ")
#     for asr in asarlar:
#         print(asr.capitalize())
    



# M3


# sevimli_kino = {
#     "diyorbek":["forsaj", "avatar", "don"],
#     "azizbek":["trasformerlar", "baxtsiz inson", "kelgindi kelin"],
#     "kamoliddin":["asalarichi", "himoyachi", "mexanik"],
#     "sardor":["terminator", "temir xotin", "kelgindi kuyov"],
#     "yusufjon":["ono", "taxt oyinlari", "zobilar olami"]
# }


# for ism, kinolar in sevimli_kino.items():
#     print(f"\n{ism.title()}ning sevimli kinolari:  ")
#     for kino in kinolar:
#         print(kino.capitalize())




# M4

# davlatlar ={

#     "o'zbekiston":{
#         "poytaxti":"toshkent",
#         "hududi":448_978,
#         "aholisi":35_000_000,
#         "pul birligi":"so'm"
#     },

#     "rossiya":{
#         "poytaxti":"moskva",
#         "hududi":17_098_246,
#         "aholisi":144_000_000,
#         "pul birligi":"rubl"
#     },

#     "aqsh":{
#         "poytaxti":"vashington",
#         "hududi":9_631_418,
#         "aholisi":327_000_000,
#         "pul birligi":"dollar"
#     },

#     "malayziya":{
#         "poytaxti":"Kula - Lumpur",
#         "hududi":9_631_418,
#         "aholisi":25_000_000,
#         "pul birligi":"rinngit"
#     }

# }

# for davlat, info in davlatlar.items():
#     print(f"\n{davlat.upper()}ning -> Poytaxti: {info["poytaxti"].capitalize()}")
#     print(f"Hududi: {info['hududi']} kv.km",
#           f"\nAholisi: {info["aholisi"]} ksihini tashkil etadi.",
#           f"\nPul birligi: {info["pul birligi"].capitalize()}")










