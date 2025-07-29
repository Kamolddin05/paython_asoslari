''' 21/07/2025 '''

#08 RO'YXATLAR BILAN ISHLASH

# m1

# cars = ["Mers", "BMW", "Audi", "GM", "Tesla", "Cobalt"]
# cars.sort()
# print(cars)


# m2

# cars = ["Bmw", "audi", "mers", "gm", "tesla", "Volga"]
# cars.sort()
# print(cars)



# m3    /// Ro'yxatni teskari tartibda saqlash uchun .sort() metodi ichida reverse=True argumentini ham kiritamiz.
# cars = ["bmw", "audi", "mers", "tesla", "gm", "volga"]
# cars.sort(reverse = True)
# print(cars)



# m4
#Ba'zida asl ro'yxat ichidagi elementlarning ketma-ketligini buzmagan holda ro'yxatni tartiblash talab qilinishi mumkin. Buning uchun sorted() funktsiyasidan foydalanamiz:

# mehmonlar = ["Odil", "Diyorbek", "Azizibek", "Sardor", "Yusufjon", "Tolibjon", "Azimjon"]
# print("Sorlangan mehmonlar: ",sorted(mehmonlar))
# print("Asl mehmonlar roy'xati: ", mehmonlar)



# m5

# ages = [12, 34, 56, 15, 78, 21]
# ages.sort()
# print(ages)
# print(sorted(ages, reverse= True))



# |////////////  RO'YXATNI AYLANTIRISH \\\\\\\\\\|

# m6

# mevalar = ["olma", "banan", "ananas", "nok", "shaftoli"]
# mevalar.reverse()
# print(mevalar)


# |////////// RO'YXATNING UZUNLIGINI BILISH \\\\\\\\\\\\|

# m7

# mevalar = ["olma", "nok", "uzum", "o'rik", "shaftoli", "gilos", "banan", "ananas"]
# mev_roy_uzunligi = len(mevalar)
# print(mevalar)
# print(mev_roy_uzunligi)



# |///////////////////////// range() FUNKTSIYASI \\\\\\\\\\\\\\\\\\\\\\\\\|

# m8

# nums_list = list(range(1, 10))
# print(nums_list)



# m9

# juft_soonlar = list(range (0, 10, 2))
# toq_sonlar = list(range (1, 10 , 2))
# print(f"toq sonlar: {juft_soonlar}")
# print(f"juft sonlar: {toq_sonlar}")



# |//////////////////////// SONLI RO'YXAT USTIDA SODDA AMALLAR \\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\|

# m10

# narhlar = [12000, 15000, 65000, 950, 4801]
# max_qiymati = max(narhlar)
# min_qiymati = min(narhlar)
# summa = sum(narhlar)
# print(max_qiymati)
# print(min_qiymati)
# print(summa)



# |///////////////////////// RO'YXATNI KESISH \\\\\\\\\\\\\\\\\\\\\\\\\\\|

# m11

# cars = ["bmw", "moto", "gm", "tesla", "mers", "volvo", "audi"]
# my_cars = cars[0 : 3]
# print(my_cars)
# print()

# my_cars2 = cars[3:]
# print(my_cars2)

# my_cars3 = cars[2 : 4]
# print(my_cars3)




# |/////////////////////////////// RO'YXATDAN NUSXA OLISH \\\\\\\\\\\\\\\\\\\\\\\\\\\\\|

# m12

# sonlar = [1, 2, 3, 4, 5]
# sonlar2 = sonlar
# sonlar2.append(6)
# sonlar2.append(7)
# print(sonlar2) #---------------->> \\\\ NUSXA OLINMADI ////


# m13 \\\\ NUSXA OLINADI QANDAY <<< sonlar2 = sonlar[:] >>>> shu amla bilan.

# sonlar = [1, 2, 3, 4, 5, 6]
# sonlar2 = sonlar[:]
# sonlar2.append(8)
# sonlar2.append(7)
# print("Bu sonlar ro'yxati: ", sonlar) 
# print("Bu sonlar2 ro'yxati: ", sonlar2)




# |////////////////////////////// TUPLES - O'ZGARMAS RO'YXAT \\\\\\\\\\\\\\\\\\\\\\\\\\|

# m14

# tomonlar = (10, 20, 30)
# print(tomonlar)
# print(type(tomonlar))


# m15

# toys = ["bus", "car", "bear", "dino", "snake", "lizard"]
# print(toys[0])
# print(toys[-1])
# print(toys[2:5])



# m16 

# toys = ('bus','car','bear','dino','snake','lizard')
# toys = list(toys)
# toys.append("dragon")
# toys.remove("bus")
# toys.insert(0, "avto")
# toys[1] = "mcqueen"
# toys = tuple(toys)
# print(toys)




# /////////////////////////////////////////////////// AMALIYOT \\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\.

''' 21/07/2025'''

# M1
# royxat = ["Turkiya", "AQSH", "UK", "Argintina", "O'zbekiston", "Shivitsariya", "Filandiya"]
# print(royxat)


# M2

# royxat = ["Turkiya", "AQSH", "UK", "Argintina", "O'zbekiston", "Shivitsariya", "Filandiya"]
# print(len(royxat))


# M3

# royxat = ["Turkiya", "AQSH", "UK", "Argintina", "O'zbekiston", "Shivitsariya", "Filandiya"]
# print(sorted(royxat))


# M4

# royxat = ["Turkiya", "AQSH", "UK", "Argintina", "O'zbekiston", "Shivitsariya", "Filandiya"]
# print(sorted(royxat, reverse= True))



# M5

# royxat = ["Turkiya", "AQSH", "UK", "Argintina", "O'zbekiston", "Shivitsariya", "Filandiya"]
# print(royxat)


# M6

# royxat = ["Turkiya", "AQSH", "UK", "Argintina", "O'zbekiston", "Shivitsariya", "Filandiya"]
# royxat.reverse()
# print(royxat)



# M7

# royxat = ["Turkiya", "AQSH", "UK", "Argintina", "O'zbekiston", "Shivitsariya", "Filandiya"]
# royxat.sort(reverse= True)
# print(royxat)


# M8 - 9 - 10 - 11 - 12

# sonlar = list(range(120, 1200, 2))
# print(sonlar)
# print("\nSumma: ",sum(sonlar))
# print()
# max_son = max(sonlar)
# min_son = min(sonlar)
# summa = max_son + min_son
# print(f"Max son: {max_son}")
# print(f"Min son: {min_son}")
# print(f"Summa: {summa}")
# print(len(sonlar))
# print()
# bsoshidagi= sonlar[0: 20]
# print(bsoshidagi)
# print()
# oxiridagi = sonlar[:20]
# print(oxiridagi)
# ortadagi = sonlar[260 : 281]
# print(ortadagi)


# M 13 - 14 - 15 - 16

# taomlar = ["Shorva", "Manti", "Chuchvar", "Makron palov", "Osh" ]

# # 14
# nonushta =  taomlar[:]
# nonushta.append("Tuxum")
# nonushta.append("Non")
# nonushta.append("Sir")
# # print("Bu taomlar ro'yxati: ",taomlar)
# # print("Bu nonushta ro'yxati: ", nonushta)

# # 15
# nonushta1 = []
# n = nonushta[5:]
# nonushta1.append(n)
# nonushta1.append("Qizil ikra")
# nonushta1.append("Qora")
# #print(nonushta1)

# # 16
# print(taomlar)
# print(nonushta1)


# M18

# nonushta = ["tuxum", "sir", "murobbo", "choy", "koffey"]
# nonushta = tuple(nonushta)
# # nonushta.apppend("tuxum")
# # nonushta.append("non")
# print(type(nonushta))
# print(nonushta)





