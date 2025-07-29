''' 19/07/2025'''

#--------------------------------------------------------. 07 LIST (RO'YXAT) ----------------------------------------------------------.
#///////////////////////////////////////////////////////////////  LIST BILAN TANISHAMIZ  \\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\.

# m1

# mevalar = ["olma", "anjir", "shaftoli", "o'rik"]
# narhlar = [12000, 13000, 19000, 22000]
# sonlar = ["bir", "ikki", 2, 4, 5]
# ismlar = []
# print(mevalar)
# print(narhlar)
# print(sonlar)
# print(ismlar)


# --------------------------------------------------------------- LIST ELEMENTLARI
# m2

# mevalar = ["olma", "anjir", "shaftoli", "o'rik"]
# narhlar = [12000, 13000, 19000, 22000]
# sonlar = ["bir", "ikki", 2, 4, 5]
# ismlar = []
# print("Birnchi meva: ", mevalar[0])
# print("Ikkinchi meva: ", mevalar[1])



# m3

# mevalar = ["olma", "anjir", "shaftoli", "o'rik"]
# narhlar = [12000, 13000, 19000, 22000]
# sonlar = ["bir", "ikki", 2, 4, 5]
# ismlar = []

# print("Birinchi meva: ", mevalar[0].title())
# print("Ikkinchi meva: ", mevalar[1].upper())
# print("Uchinchi meva: ", mevalar[2].lower())



# m4

# narxlar = [12000, 200000, 230000, 450000]
# print(narxlar[0] + narxlar[1])



# m5

# car_models = ["Toyota", "GM", "Volov", "BMW", "Hyundai", "Kia", "Volkswagen"]
# print(car_models[-1])


# -----------------------------------------------------------. ELEMENTLARNI QO'SHISH, O'CHIRISH VA O'ZGARTIRISH .---------------------------------------------------------------------

# m6

# narxlar =[12000, 13000, 18000, 10800, 20000]
# narxlar[0] = 17000
# narxlar[2] = 12000
# narxlar[3] = narxlar[3] + 2000
# print(narxlar)


# m6 ///// .append(qiymat)

# mevalar = ["olma", "shaftoli", "banan", "ananas"]
# mevalar.append("nok")
# print(mevalar)


# m7

# cars = []
# cars.append("Malibu")
# cars.append("BMW")
# cars.append("Cobolt")
# print(cars)


# m8 ///// .insert(index, qiymat) birinchi qoshmoqchi bolgan joyingizni belgilaysis kiyin esa qoshadigan qiymatingizni nomini kiritasiz misol : mevalar.insert(3, olma)

# cars = ["Lacetti", "Nexia 3", "Malibu"]
# cars.insert(2, "Cobolt")
# print(cars)
# print()
# cars.insert(0, "Malibu")
# print(cars)



# m9 //////// Elementni o'chirish  del -> orqali ochirish, ochirmoqchi bolgan qiiymatimizni indexs bilish.  .remove(qiymat) faqat ochirmoqchi bolgan narsani nomi yoki qiymatini bilsak boldi.

# cars = ["Malibu", "Cobolt", "Nexia 3", "BMW", "Mers", "Gentra", "Lacetti"]
# del cars[1]  # indexs [1] bolgan royhatda cobolt turib di va uni o'chirib tashladi.
# print(cars)



# m10

# cars = ["Malibu", "Cobolt", "Nexia 3", "BMW", "Mers", "Gentra", "Lacetti"]
# cars.remove("Nexia 3")  # cars.remove(qiymatni) kiridik va qiymatimiz " Nexi 3 " edi va royxatdan Nexi 3 olib tashladi.
# print(cars)



# m11 //////// Elementni sug'urib olish

# bozorlik = ["yog'", "un", "pioz", "gosht", "tuxum", "non", "kartoshka", "pamildori"]
# mahsulotlar = bozorlik.pop(3) #  Ba'zida biror elementni butunlay o'chirib tashlash emas, balki uni ro'yxatdan sug'urib olish va undan foydalanish talab qilinishi mumkin. Buning uchun Pythonda .pop(indeks) metodidan foydalanmiz.
# print("Men " + mahsulotlar + " sotib oldim" )
# print("Olinmagan mahsulotlar: ", bozorlik)





'''21/07/2025'''

# /////////////////////////////////////////////////////////////////// AMALIYOT \\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\


# M1

# ism = []
# ism.append("Diyorbek")
# ism.append("Sardorbek")
# ism.append("Azizbek")
# print(ism)



# M3

# ismlar = ["Dyorbek", "Sardorbek", "Azizbek"]
# ism1 = ismlar[0]
# ism2 = ismlar[2]
# print(f"Salom {ism1}, bugun choyxona bormi? \n{ism2}, choyxonaga boramizmi? ")



# M4

# sonlar = []
# musbat_son = sonlar.append(1.2)
# manfiy_son = sonlar.append(-12)
# butun_son = sonlar.append(12)
# onlik_son = sonlar.append(20)
# print(sonlar)


# M5

# sonlar = []
# musbat_son = sonlar.append(1.2)
# manfiy_son = sonlar.append(-12)
# butun_son = sonlar.append(12)
# onlik_son = sonlar.append(20)
# onlik_son = sonlar.append(16)
# print(sonlar)
# print()

# arifmetik amallar
# print("Arimetik amallar")
# qoshish = sonlar[0] + sonlar[1]
# ayirish = sonlar[1] - sonlar[2]
# kopaytirish = sonlar [2] * sonlar[0]
# print(f"Qoshish: {qoshish} \nAyirish: {ayirish} \nKopaytirish: {kopaytirish}")

# Ro'yxatdagi sonlarni qiymatini o'zgartirish

# print("Qiyamt o'zgarishi! ")
# sonlar.remove(-12)
# sonlar.insert(1, 11)
# print(sonlar)
# print()


#  Qiyamtni almashtirsh //////////////// # sonlar[1], sonlar[3] = sonlar[3], sonlar[1]
# print("Qiymatni joyini  almashtirish. ")
# qiymat1 = sonlar.pop(3)
# qiymat2 = sonlar.pop(1)
# sonlar.insert(1, qiymat1)
# sonlar.insert(3, qiymat2)
# print(sonlar)



# M6

# friends = []
# friends.append("Diyorbek")
# friends.append("Sardorbek")
# friends.append("Azizbek")
# friends.append("Abosbek")
# friends.append("Omadbek")
# friends.append("Yusfjon")
# print(friends)


# M7

# friends = []
# friends.append("Diyorbek")
# friends.append("Sardorbek")
# friends.append("Azizbek")
# friends.append("Abosbek")
# friends.append("Omadbek")
# friends.append("Yusufjon")
# print(friends)
# print()

# # .remove(qiymat)

# friends.remove("Diyorbek")
# friends.remove("Yusufjon")
# print(friends)




# m8

# mehmonlar = []
# mehmonlar.append("Diyorbek")
# mehmonlar.append("Sardorbek")
# mehmonlar.append("Azizbek")
# mehmonlar.append("Abosbek")
# mehmonlar.append("Omadbek")
# mehmonlar.append("Yusfjon")
# print(mehmonlar)
# print()

# # Ro'yxat oxiriga qiymat qoshish
# print("Ro'yxat oxiriga qiymat qoshish!")
# friends[-1] = "Tolibjon" 
# print(friends)
# print()

# # Royxat boshiga qiymat qoshildi.
# print("Royxat boshiga qiymat qoshildi! ")
# friends[0] = "Kamoliddin"
# print(friends)
# print()

# # Ro'yxat ortasiga qiymat qoshish.
# print("Ro'yxat ortasiga qiymat qoshish! ")
# orta_indexs = len(friends) // 2
# friends.insert(orta_indexs, "Rasulbek")
# print(friends)


# M9

# mehmonlar = []
# mehmonlar.append("Diyorbek")
# mehmonlar.append("Sardorbek")
# mehmonlar.append("Azizbek")
# mehmonlar.append("Abosbek")
# mehmonlar.append("Omadbek")
# mehmonlar.append("Yusfjon")
# print(f"Mehmonga chaqirilgan mehmonlar ismi: \n{mehmonlar}")

# print()
# m1 = mehmonlar.pop(2)
# m2 = mehmonlar.pop(0)
# m3 = mehmonlar.pop(1)

# print(f"Hozircha Kelganlar royxati: {m1, m2, m3}")
# print(f"Qolganlar: {mehmonlar}")
