'''31/07/2025'''


# |/////////////////////| 15 LUG'AT ELEMENTLARI BILAN ISHLASH |\\\\\\\\\\\\\\\\\\\\\\|



# >>>----------------------------> .items() METODI <-------------------------------<<<

# m1 

# talaba_0 = {
#     "ism":"Kamoliddin",
#     "familiya":"Raximjonov",
#     "yosh":20,
#     "fakultet":"Dasturiy injiniring",
#     "kurs":4
# }

# print(talaba_0.items())




# m2

# talaba_0 = {
#     "ism":"Kamoliddin",
#     "familiya":"Raximjonov",
#     "yosh":20,
#     "fakultet":"Dasturiy injiniring",
#     "kurs":4
# }


# for key , value in talaba_0.items():
#     # print(f"Kalit: {key.capitalize()}")
#     # print(f"Value: {value}")

#     # print(f"{key.capitalize()}: {value}")



# m3

# telefonlar = {
#     "ali":"iphone x",
#     "vali":"galaxy",
#     "kamoliddin":"tecno",
#     "diyorbek":"samsung s 22",
#     "sardor":"samsung a 50",
#     "odil":"samsung s 22 ultra"

# }

# for key, value in telefonlar.items():
#     print(f"{key.title()}ning telefoni: {value.title()}")




# >>>------------------------------> .keys() METODI <------------------------------<<<

# m4

# mahsulotlar = {
#     "olma":10000,
#     "anor":20000,
#     "uzum":40000,
#     "anjir":25000,
#     "shaftoli":30000
# }

# # print(f"Kalit: {mahsulotlar.keys()}")

# print("Do'kondagi mahsulotlar: ")
# for mahsulot in mahsulotlar.keys():
#     print(f"{mahsulot.title()}")




# m5

# mahsulotlar = {
#     "olma":10000,
#     "anor":20000,
#     "uzum":40000,
#     "anjir":25000,
#     "shaftoli":30000
# }


# bozorlik = ["olma", "banan", "non", "go'sht", "uzum", "shaftoli"]
# for mahsulot in mahsulotlar:
#     if mahsulot in bozorlik:
#         print(f"{mahsulot.title()} {mahsulotlar[mahsulot]} so'm")



# for buyum in bozorlik:
#     if buyum not in mahsulotlar:
#         print(f"Iltimos, do'konigizga {buyum} ham olib keling. ")





# >>>-----------------------------> .values() METODI <-----------------------------<<<


# m6

# telefonlar = {
#     "ali":"iphone x",
#     "vali":"galaxy",
#     "kamoliddin":"tecno",
#     "diyorbek":"samsung s 22",
#     "sardor":"samsung a 50",
#     "odil":"samsung s 22 ultra"

# }

# #print(telefonlar.values())

# print("Foydalanuvchilar quydagi telefonlarni oshlatadi: ")
# for tel in telefonlar.values():
#     print(tel)



# m7

# telefonlar ={
#     "ali":"iphone x",
#     "vali":"galaxy s9",
#     "olim":"mi 10 pro",
#     "orif":"nokia 3310",
#     "hamid":"galaxy s9",
#     "maryam":"huawei p30",
#     "tohir":"iphone x",
#     "umar":"iphone x",
# }


# print("Foydalanuvchi quydagi telefonlarni ishlatishadi: ")
# for tel in telefonlar.values():
#     print(tel)





# m8

# telefonlar ={
#     "ali":"iphone x",
#     "vali":"galaxy s9",
#     "olim":"mi 10 pro",
#     "orif":"nokia 3310",
#     "hamid":"galaxy s9",
#     "maryam":"huawei p30",
#     "tohir":"iphone x",
#     "umar":"iphone x",
# }

# print("Foydalanuvchi quydagi telefonlarni ishlatishadi: ")
# for tel in set(telefonlar.values()):
#     print(tel)




# m9

# telefonlar ={
#     "ali":"iphone x",
#      "umar":"iphone x",
#     "hamid":"galaxy s9",
#     "maryam":"huawei p30",
#     "vali":"galaxy s9",
#     "olim":"mi 10 pro",
#     "orif":"nokia 3310",
#     "hamid":"galaxy s9",
#     "maryam":"huawei p30",
#     "tohir":"iphone x",
#     "umar":"iphone x",
#     "hamid":"galaxy s9",
#     "maryam":"huawei p30",
#     "tohir":"iphone x",
#     "umar":"iphone x",
# }


# print("Foydalanuvchilar ismi: ")
# for foydalanuvchi in set(telefonlar.keys()):
#     print(foydalanuvchi)



# m10

# soz = {"ali", "vali", "bobur", "ali", "sharof", "bobur", "samandar",
#        "kamoliddin", "fotima", "diyorbek", "fotima", "zuhra", "tolibjon",
#        "umar", "zubayer", "zakariyya", "zubayer", "zakariyya", "alya"}
# for i in set(sorted(soz)):

#     print(i)


'''03/08/2025'''

# |/////////////////////////////////////| AMALIYOT |\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\|

# M1

# my_dict = {"boolen":"mantiqiy", "for":"biror bir amalni qayta bajarish ",
#            "float":"O'nlik son", "print":"chop etish", "if":"shart tekshirish",
#            "int":"butun son", "break":"tsikilni toxtatish"}

# for keys, value in sorted(my_dict.items()):
#     print(f"{(keys.capitalize())} -> {value.capitalize()}")



# M2

# my_dict = {"aqsh":"washengton", "germaniya":"berlin", "rossiya": "moskwa",
#            "turkiya":"anqara", "o'zbekiston":"toshkent", "avstraliya":"sidney", 
#            "eron":"texron", "dubay":"abudabiy", "qatar":"doxa"}



# for keys, value in sorted(my_dict.items()):
#     print(f"{keys.capitalize()} -> {value.capitalize()}")

# for value in sorted(my_dict.values()):
#     print(f"{value.capitalize()}")


# M3

# my_dict = {"aqsh":"washengton", "germaniya":"berlin", "rossiya": "moskwa",
#            "turkiya":"anqara", "o'zbekiston":"toshkent", "avstraliya":"sidney", 
#            "eron":"texron", "dubay":"abudabiy", "qatar":"doxa"}


# davlat = input("Istalgan davlat nomi kiritng: ").lower()

# capital = my_dict.get(davlat)
# if capital == None:
#     print(f"{"Kechirasiz bizda bunday davlat yoq."}")
# else:
#     print(f"{davlat.upper()} ning poytaxti {capital.title()} shahri.")




# taom_dict = {"osh":20000,
#              "shashlik":25000,
#              "norin":22000,
#              "qozonkabob":32000,
#              "shorva":25000,
#              "mastava":22000,
#              "somsa":10000,
#              "honim":6000,
#              "gumma":3000,
#              "tandir":180000,
#              "gril":60000
#              }

# menu = []
# for n in range(3):
#     menu.append(input(f"{n+1} - Qanday taom buyurtma qilasiz: ").lower())


# for taom in menu:

#     if taom in taom_dict:
#         print(f"{taom.title()} {taom_dict[taom]} so'm. ")
#     else:
#         print(f"Kechirasiz bizda {taom} yo'q. ")