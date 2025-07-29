'''25/07/2025'''

# |///////////////////////////////////| 11 BIR NECHTA SHARTLARNI TEKSHIRISH |\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\|

# m1

# yosh = int ( input ("Yoshingizni kiriting: "))
# if yosh <= 4:
#     print ("Sizga kirish bepul.")
# elif yosh <= 12:
#     print("Sizga kirish 5000 so'm. ")
# else:
#     print("Sizga kirish 10000 so'm. ")



# m2

# yosh = int ( input ("Yoshingizni kiritng: "))

# if yosh <= 4:
#     narx = 0
# elif yosh <= 12:
#     narx = 12000
# else:
#     narx = 15000

# print(f"Sizga kirish {narx} so'm")



# m3

# yosh = int ( input ("Yoshingizni kiriting: "))

# if yosh <= 4 :
#     narax = 0
# elif yosh <= 7:
#     narax = 5000
# elif yosh <= 12:
#     narax = 8000
# elif yosh <= 16:
#     narax = 10000
# else:
#     narax = 15000

# print(f"Sizga kirish narxi {narax} so'm")



# m4 # ///// else qismi  majburiy emas holati.

# yosh = int(input('Yoshingiz nechida? '))
# if yosh<=4:
#     price = 0
# elif yosh<=12:
#     price = 5000
# elif yosh<65:
#     price = 10000
# elif yosh>=65:
#     price = 8000    
# print(f"Sizga kirish {price} so'm")


# >>>--------------------->  AND, OR OPERATORLARI <----------------------<<<

# m5

# kun = input ("Bugun qanday kun: ")

# if kun.lower() == "shanba" or kun.lower() == "yakshanba":
#     print(f"Bugun {kun.title()} dam olish kuni. ")
# else:
#     print(f"Bugun {kun.title()} ish kuni. ")



# m6

# kun = input ("Bugun qanday kun: ")
# harorat = float (input ("Havo haroratini kiriting: "))

# if (kun.lower() == "shanba" or kun.lower() == "yakshanba") and harorat > 30:
#     print(f"Bugun {kun.title()} dam olish kuni, Havo harorati: {harorat} *C")
#     print("Bassenga chomilgani ketik. ")

# elif (kun.lower() == "shanba" or kun.lower() == "yakshanba") and harorat < 30:
#     print(f"Bugun {kun.title()} dam olish kuni, Havo harorati: {harorat} *C")
#     print("Bugun dam olish kuni edi ming afsuski, havo harorati past va salqin bolgani uchun, uyda qolishingiz tafsiya etiladi. ")



# >>>------------------------> BOOLEAN MA'LUMOTLAR TURI <-------------------------<<<

# m7

# narh = 15000
# choy = True
# salat= False

# if choy and salat:
#     narh = narh + 10000
# elif choy or salat:
#     narh = narh + 5000

# print(f"Jami {narh} so'm")



# m8

# narh = 15000
# choy = True
# salat = False
# non = True
# kompot = True
# assorti = False

# if choy:
#     print("Mijoz choy oldi.")
#     narh += 3000

# if salat:
#     print("Mijoz salat oldi.")
#     narh = narh + 5000

# if non:
#     print("Mijoz non oldi.")
#     narh = narh + 2000

# if kompot:
#     print("Mijoz kompot oldi.")
#     narh = narh + 5000

# if assorti:
#     print("Mijoz assorti oldi. ")


# print(f"Jami {narh} so'm")




# >>>-----------------------> RO'YXAT TARKIBINI TEKSHIRISH <----------------------<<<

# in OPERATORI

# m9 

# menu = ["osh", "qazonkabob", "shashlik", "norin", "somsa"]

# ovqat = input("Qanday taom buyurtma qilasiz: ")
# if ovqat.lower() in menu:
#     print("Buyurtma qabul qilindi. ")
# else:
#     print("Afsuski bizda bunday taom yoq. ")
    


# m10

# menu = ["osh", "qozonkabob", "shashlik", "norin", "somsa"]
# ovqat = input("Qanday taom buurtma qilasiz: ")

# if ovqat.lower() not in menu:
#     print("Afsuski bunday taombizda yoq. ")

# else:
#     print("Buyurtma qabul qilinda. ")



# >>>------------------------> IKKI RO'YXATNI SOLISHTIRISH <-----------------------<<<

# m11

# menu = ["shorva", "osh", "shashlik", "somsa", "norin", "qozonkabob"]
# byurtma = ["osh", "shashlik", "somsa", "norin", "choy", "kampot"]

# for taom in byurtma:
#     if taom in menu:
#         print(f"Menuda {taom} bor")

#     else:
#         print(f"Kechirasiz, menuda {taom} yo'q. ")


# >>>-------------------> RO'YXAT BO'SH EMASLIGINI TEKSHIRISH <-------------------<<<


# m12

# menu = ["osh", "qozonkabob", "shashlik", "norin", "somsa"]
# byurtma = ["osh", "somsa", "manti", "shashlik"]

# if byurtma:

#     for taom in byurtma:
#         if taom in menu:
#             print(f"Menuda {taom} bor. ")
#         else:
#             print(f"Kechirasiz, menuda {taom} yoq. ")
# else:
#     print("Savatchangiz bo'sh! ")


'''26 - 27/07/2025'''

# |/////////////////////////////////////| AMALIYOT |\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\|

# M1

# son = int ( input ("Iltimos juft son kiritng: "))

# if son % 2 == 0:
#     natija = "Rahmat"
# else:
#     natija = "Iltimos juft son kiritng bu toq son !!! "

# print(f"Natija: {natija}")



# M2

# foydalanuvchi = int (input ("Yoshingiz nechida: "))

# if foydalanuvchi <= 4 or foydalanuvchi >= 60:
#     narx = 0
# elif foydalanuvchi <= 18 :
#     narx = 10000
# else:
#     narx = 20000

# print(f"Muzeyga kirish {narx} so'm")



# M3

# son1 = int ( input ("Son kiriting: "))
# son2 = int ( input ("Son kiriting: "))

# if son1 > son2:
#     natija = f"{son1} > {son2} "
# elif son1 < son2:
#     natija = f"{son1} < {son2} "
# else:
#     natija = f"{son1} = {son2}"

# print(f"Natija: {natija}")



# M4

# mahsulotlar = ["non", "choy", "novvot", "kolbasa", "go'sht", "makron", "un", "olma", "banan", "anor" ]
# savat = []

# for n in range(5):
#     savat.append(input(f"Savatga {n+1}-mahsulot qo'shing: "))

# for mahsulot in savat:
#     if mahsulot in mahsulotlar:
#         print(f"Do'konimizda {mahsulot} bor ")
#     else:
#         print(f"Do'konimizda {mahsulot} yo'q ")



# M5

# mahsulotlar = ["non", "go'sht", "yog'", "un", "tuxum", "olma", "banan", "shaftoli", "kolbasa", "sir"]
# savat = []

# for i in range(5):
#     savat.append(input("Mahsulot nomini kiriting: "))


# bor_mahsulotlar = []
# mavjud_emas = []

# for mahsulot in savat:
#     if mahsulot in mahsulotlar:
#         bor_mahsulotlar.append(mahsulot)
#     else:
#         mavjud_emas.append(mahsulot)


# if mavjud_emas:
#     print(f"Do'konimizda quyidagi mahsulotlar yo'q: ")
#     for mahsulot in mavjud_emas:
#         print(mahsulot)
# else:
#     print("Siz so'ragan barcha mahsulotlar do'konimizda bor. ")




# M6

# foydalanuvchi = ["kamoliddin123", "diyorbek23", "azizbek90", "sardor09", "odiljon8"]
# login = input ("Marhamat qilib login kiriting: ")
# if login in foydalanuvchi:
#     print("Bu login band!!! ")
# else:
#     print("Xush kelibsiz, foydalanuvchi! ")




# M7

# son = int ( input ("Son kriting: "))

# for i in range(2, 11):
#     if son % i == 0:
#         print(f"{son} soni {i} ga qoldiqsiz bolinadi. ")




'''28/07/2025'''

# |//////////////////////////////| Takrori Amaliyot |\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\|


# 1 Ismlar tekshiruvi:

# ismlar = ["ali", "vali", "hasan", "husan", "olim", "anvar", "kamoliddin"]

# name = []
# for n in range(5):
#     name.append(input (f"{n+1} - Ism kirting: "))

# print()
# bor_ismlar = []
# yoq_ismlar = []
# for ism in name:
#     if ism.lower() in ismlar:  
#         bor_ismlar.append(ism) 
#         print(f"{ism.title()} ismi royxatda bor. ")
#     else:
#         yoq_ismlar.append(ism)
#         print(f"{ism.title()} ismi royxatda yoq.")



# 2 Kitoblar ro'yxati:

# kitoblar = ["kimyo", "matematika", "biologiya", "geografiya", "fizika", "tarix", "huquq", "rus tili", "ona tili", "adabiyot"]
# quti = []

# for n in range(5):
#     quti.append(input (f"{n+1} - Kitoblar nomini kirting: "))

# print()
# topilganlar = []
# topilmaganlar = []
# for kitob in quti:
#     if kitob.lower() in kitoblar:
#         topilganlar.append(kitob)
#         print(f"Topilgan kitoblar: {kitob.title()}")
#     else:
#         topilmaganlar.append(kitob)
#         print(f"Topilmagan kitoblar: {kitob.title()}")





# 3 Shaharlar ro'yxati:

# mavjud_shaharlar = ["moskva", "toshkent", "madrid", "berlin", "luksinburg", "samarqand", "washington" ]
# hizmat_kor_shah = ["moskva", "toshkent", "samarqand", "berlin"]
# shah_nomi = []

# for n in range(5):
#     shah_nomi.append(input (f"{n+1} - Shahar nomini kiriting: "))


# xizmat_bor = []
# xizmat_yoq = []

# for shahar in shah_nomi:

#     if shahar.lower() in mavjud_shaharlar:
#         print(f"\nRoyhatimizda bor shaharlar {shahar.title()}")

#         if shahar.lower() in hizmat_kor_shah:
#             xizmat_bor.append(shahar)
#             print(f"Xizmat bor shaharlar: {shahar.title()}\n")
#         else:
#             xizmat_yoq.append(shahar)
#             print(f"Xizmat yoq shaharlar: {shahar.title()}\n")
        
#     else:
#         print(f"\nBu shahra royxatimizda yoq: {shahar.title()}")




# 4 Filmlar ro'yxati:

# Kinolar_royxati = ["avatar", "no'vda", "asalarichi", "transformerlar", "farsaj", 
#                    "udabiron bolalar", "kelgindi kuyov", "kelgindi kelin",
#                      "salohiddin", "abdulhamid", "xalifa umar", "amerikalik snayper"]

# mavjud_kinolar = ["avatar", "asalarichi", "trasformerlar", "no'vda", "farsaj"]
# kinolar = []

# for n in range(5):
#     kinolar.append(input(f"{n+1} - Kerakli kinolar nomini kirting: "))


# mavjud = []
# mavjud_emas = []

# for kino in kinolar:

#     if kino.lower() in Kinolar_royxati:
#         print(f"\nBunday kino, kinolar ro'yhatida tastiqlangan: {kino.title()}")

#         if kino.lower() in mavjud_kinolar:
#             mavjud.append(kino)
#             print(f"Bizda mavjud bolgan kinolar oarasida topildi: {kino.title()}\n")
#         else:
#             mavjud_emas.append(kino)
#             print(f"Bizda mavjud bolgan kinolar oarasida topilmadi: {kino.title()}\n")
    
#     else:
#         print(f"\nBunday kino, kinolar ro'yhatida tastiqlanmagan: {kino.title()}")
            




# 5 O'yinlar tekshiruvi:


# Kompyuter_oyinlar = ["dota2", "cs", "generals007", "call of duty",
#                       "the witcher", "mincraft", "pubg", "fortnite", 
#                       "red dead, redemption", "legue of legends"]

# oyinlar = []
# for n in range(5):
#     oyinlar.append(input(f"{n+1} - Oyin nomini kiriting: "))

# print()
# for oyin in oyinlar:

#         if oyin.lower() in Kompyuter_oyinlar:
#             print(f"{oyin.title()} -> oyini royxatda bor.")
#         else:
#             print(f"{oyin.title()} -> oyin royxatda yoq.")




# 6  Telefon modellari:

# Tel_model = ["iphone", "galaxe", "pixel", "xiaomi", "realme", "asus", "huawei"]
# dokon = []

# for n in range(5):
#     dokon.append(input(f"{n+1} - Qanday telefon kerak: "))

# print()
# for telefon in dokon:
#     if telefon.lower() in Tel_model:
#         print(f"Bu {telefon.title()} smartphone dokonda mavjud.")
#     else:
#         print(f"Bu {telefon.title()} smartphone dokonda mavjud emas. ")




# 7 Taomlar ro'yxati:

# Taomlar =["osh", "shorva", "norin", "somsa", "shashlik", "mastava", 
#           "goja", "homnim", "qozonkabob", "dimlama"]
# menu = []

# for n in range(5):
#     menu.append(input(f"{n+1} - Qanday taom buyurtma qilasiz: "))

# print()
# for taom in menu:
#     if taom.lower() in Taomlar:
#         print(f"Sizning taomingiz: {taom.title()}")
#     else:
#         print(f"Bunday taom menuda yoq. Taom nomi: {taom.title()}")





# 8 Sport turlari ro'yxati:


# Sport_turlari = ["futbol", "basketbol", "valebol", "hokkey", "gandbol", "suzish", "gimnastika"]

# foydalanuvchi = input("Sport turinigizni yozing: ")  

# if foydalanuvchi in foydalanuvchi:
#     print(f"\nBu sport turi mavjud: {foydalanuvchi}")
# else:
#     print(f"\nBu sport turi mavjud emas: {foydalanuvchi}")
    



# 9 Dars fanlari:

# Maktab_fanlari = ["tarix", "botanika", "geogerafiya", "bologiya", "kimyo",
#                   "matematika", "fizika", "ona tili", "adabiyot", "rus tili",
#                   "tarbiya", "algebra", "geometriya", "informatika"]

# oquvchi = []
# for n in range(5):
#     oquvchi.append(input(f"{n+1} - Maktab darsliklari nomini yozing: "))

# for darslik in oquvchi:
#     if darslik.lower() in Maktab_fanlari:
#         print(f"{darslik.title()} - Bu maktab darsiligi.")
#     else:
#         print(f"{darslik.title()} - Bu maktab darsligi emas.")





# 10 Tillar ro'yxati:


# tillar_royxati = ["ingiliz tili", "rus tili", "nemis tili", "kores tili", "xitoy tili", "ispan tili", "fransuz tili"]

# oquvhi = []
# for n in range(5):
#     oquvhi.append(input(f"{n+1} - O'rgan moqchi bolgan tillarni tanlang: "))

# for til in oquvhi:
#     if til.lower() in tillar_royxati:
#         print(f"{til.title()} -> Kursimizda bor.")
#     else:
#         print(f"{til.title()} -> Kursimizda yoq.")