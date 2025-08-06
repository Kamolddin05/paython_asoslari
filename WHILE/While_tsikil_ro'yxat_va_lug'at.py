'''06/08/2025''' 
 
# |/////////////////////| While sikli, roʻyxatlar va lugʻatlar |\\\\\\\\\\\\\\\\\\\\\|


# m1

# ismlar = []

# print ("Taqin dostlaringiz ro'yxatini tuzamiz: ")
# n=1
# while True:
#     savol = f"{n} - do'stingizni ismini kiriting: "
#     ism = input(savol)
#     ismlar.append(ism)
#     javob = input("Yama ism qoshasizmi? (ha/yo'q): ")
#     if javob == "ha":
#         n+=1
#         continue
#     else:
#         break
# # print("Do'stlaringiz ro'yxati:")
# for ism in ismlar:
#     print(ism.title())



# m2


# print ("Do'stlaringiz yoshini saqlaymiz.")
# dostlar = {}
# ishora = True
# while ishora:
#     ism = input("Do'stingizni ismini kiriting: ")
#     yosh = input(f"{ism.title()}ning yoshini kiriting: ")
#     dostlar[ism] = int(yosh)

#     javob = input("Yana ma'lumot qo'shamizmi? (ha/yo'q): ")
#     if javob =="yo'q":
#         ishora = False

# for ism, yosh in dostlar.items():
#     print(f"{ism.title()} {yosh} yoshda. ")





# >>>--------------------> RO'YXAT ELEMENTLARINI O'CHIRISH <-----------------------<<<

# m3


# cars = ["lacetti", "nexia", "cobalt", "nexia", "malibu", "volga", "nexia"]

# while "nexia" in cars:
#     cars.remove("nexia")
# print(cars)




# >>>-----------------> RO'YXATDAN RO'YXATGA ELEMENT KO'CHIRISH <------------------<<<


# m4

# talabalar = ["hasan", "husan", "olim", "botir"]
# baholangan_talabalar = {}
# while talabalar:
#     talaba = talabalar.pop()
#     baho = input(f"{talaba.title()}ning baholash kiriting: ")
#     print(f"{talaba.title()} baholandi. ")
#     baholangan_talabalar[talaba] = baho







'''06/08/2025'''


# |////////////////////////////////////| AMALIYOT |\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\|

# M1


# print("Buyurtma qilgan mahsulotlaringizni tekshirib koring!!! ")
# mahsulotlar = []
# n = 1
# while True:
#     mahsulot_nomi = input(f"{n} - Mahsulot nomi: ")
#     mahsulotlar.append(mahsulot_nomi)
#     n+=1

#     javob = input("Yana mahsulotingiz qoldimi: (ha/yo'q): ")
#     if javob == "ha":
#         continue
#     else:
#         break

# print("\nSizning mahsulotingiz: ")
# for mahsulot in mahsulotlar:
#     print(f"{mahsulot.title()}")





# M2


# madaniyat = "Assalomu alaykum bizning tashkilotga xush kelibsiz. "
# firma = "E-bozor uchun qanday mahsulotlar buyurtma qilmoqchisiz."
# print(f"{madaniyat.upper()} \n{firma.capitalize()}")

# mahsulotlar = {}
# ishora = True
# while ishora:
#     mahsulot_nomi = input("Mahsulot nomi: ").lower()
#     mahsulot_narxi = int( input ("Mahsulot narxi: "))
#     mahsulotlar[mahsulot_nomi] = mahsulot_narxi

#     javob = input("Yana mahsulot burtma qilasizimi: (ha/yo'q): ")
#     if javob == "yo'q":
#         ishora = False
#     else:
#         continue

# print("\nOlib kelinga mahsulotlar va ularning narxlari: ")
# for nomi, narx in mahsulotlar.items():
#     print(f"Mahasulot nomi: {nomi.title()} -> Narxi: {narx} so'm")




# M3

# madaniyat = "assalomu alaykum bizning  'E-bozor' ning elektron plat formasiga hush kelibsiz. "
# mahsulot0 = "Bizdan qanday masulotlar buyurtma qilomchisiz. "
# print(f"{madaniyat.capitalize()} \n{mahsulot0.capitalize()}")

# foydalanuvchi_mahsulotlari = []

# while True:
#     mahsulot_nomi = input("Mahsulot nomi: ").lower()
#     foydalanuvchi_mahsulotlari.append(mahsulot_nomi)

#     javob = input("Yana mahsulot buyurtma qilasizmi: (ha/yo'q) : ")
#     if javob == "ha":
#         continue
#     else:
#         break
# # print(foydalanuvchi_mahsulotlari)

# my_edict = {

#     "olma":12_000,
#     "banan":15_000,
#     "go'sht":100_000,
#     "o'simlik yog'":80_000,
#     "suzma":10_000,
#     "pamidor":10_000,
#     "bodiring":8_000,
#     "sabzi":3_000,
#     "kartoshka":5_000,
#     "makron":12_000,
#     "lapsha":6_000,
#     "muzqaymoq":10_000,
#     "chuchvara":32_000,
#     "chesnok":32_000,
#     "qalampir":5_00,
#     "tushunka":45_000,

# }

# for mahsulot in foydalanuvchi_mahsulotlari:

#     if mahsulot in my_edict :
#         narx = my_edict[mahsulot]
#         print(f"Mahsulot nomi: {mahsulot.title()} -> {narx} so'm.")
#     else:
#         print(f"Bizda ' {mahsulot.title()} ' mahsulot yoq.")
















