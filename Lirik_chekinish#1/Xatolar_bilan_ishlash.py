'''29/07/2025'''

#|////////////////////| 12 XATOLAR BILAN ISHLASH |\\\\\\\\\\\\\\\\|


# m1 IndentationError 

# print("O'ngacha sanaymiz.")
# for i in range(1,11):
#print(i, end=" ") # bu codda print() hato bolgan edi yani print for loop ichida emas tashqariag chiqib ketgan edi 


# m2 IndentationError 

# son = 50
# if son >=0:
#     print("Musbat son")
# else:
# print("Manfiy")  bu codda print() xato ketgan else tashqariga chiqib ketgan aslida else tanasini tanasi bolish kerak edi.


# m3 TypeError

# son = input("Istalgan son kiriting: ")
# print(f"{son} ning kvadrati {son**2} ga teng") bu codda esa tip str berilgan lekin natijani int chiqarmoqchi bu xato.


# m4 NameError

# mevalar = ['olma','uzum','nok','anor','anjir']
# for meva in mvealar: ##### mvealar bolib qolgan sintaktik xato mevalar bolishi kerak.
#     print(meva)



# m5 ValueError


# son = int(input("Istalgan son kiriting: "))  ## bu dasturda faqat int sonlarni kirita olamiz chuki tip in qilib berilgan
# if son>=0:
#     print("Musbat son")
# else:
#     print("Manfiy son")



# m6  IndexError

# mevalar = ['olma','anor','uzum']
# print(mevalar[3]) buyerda indexta xato, to'g'ri royxatda 3 ta qiymat turib di lekin index 0 dan boshlanadi qiymat esa 1 dan.



# m7 ZeroDivisionError

# x, y = 50, 50
# z = 250/(50-50)  buyerda matetmatik xato yani hechqachon maxraj nol bolmaydi.



# m8 MANTIQIY XATOLAR

# radius = 5
# pi = 4.14   buyerda xat mantiqiy yani 4,14 emas 3,14 boladi pi ning qiyamti.
# aylana_yuzi = pi*radius**2  
# print(aylana_yuzi)


# m9

# # son = float(input("Istalgan son kiriting: "))
# ildiz = son**1/2  mantiqiy hato yana ildizda chiqrmoqchi boliyabdi lekin 2 bolib qoyabdi aslida mana bunday yozish kerak x = son ** (1/2)
# print(f"{son} ning ildizi {ildiz} ga teng")


# m10

# mevalar = ['olma','uzum','nok','anor','anjir']
# for meva in mevalar:
#     print(meva)
#     print("Dastur tugadi") dastur mantiqan togri kamchilik printda tab siljib qolganoldinga yani for ichida satur ishlay veradi hunuk natija chiqadi.






'''29/07/2025'''

# |///////////////////////////////////| AMALIYOT |\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\|


# M1

# son = float( input ("Juft son kriting: "))
# if son % 2 == 0:
#     print ("Bu son juft emas.") # 26 juft son afsuski dastur kodi bunday demayabdi chunki tipni float tipida berilgan sababi shu yani bunga 26.6 qiymat juft son deb hisoblaydi.
# else:
#     print("Rahmat.")




# M2

# yosh = int (input ("Yoshingoz nechida: ")) # buyerda int tushub qoldirilganedi
# if yosh <= 4 or yosh >= 60:
#     narx= 0
# elif yosh  < 18 : # buyerda esa  2 nuqta tushib qoldirilgan edi6
#     narx = 1000
# else:
#     narx = 20000
# print(f"Chipta {narx} so'm") # bu yerda print faqat else uchun ishlaydi va togirlandi.




# M3

# x = float( input ("Birinchi sonni kiriting: "))
# y = float( input ("Ikkinchi sonni kiriting: "))

# if x==y:
#     print(f"{x}={y}")
# elif x<y:
#     print(f"{x}<{y}") # buyerda faqat qoshtirnoqda xato bor edi.
# else:  # --------------------> buyerda 2 ta nuqta tushib qolganedi.
#     print(f"{x}>{y}")




# M4

# mahsulotlar = ["un", "yog'", "sovun", "tuxum", "piyoz", "piyoz", "kartoshka", 
#                "olma", "banan", "uzum", "qovun"]

# savat = []  # savat degan bosh royxat yasash kerak edi lekin tahslab ketilgan va bu tog'rlandi.
# for n in range(5):
#     savat.append(input(f"Savatga {n+1} - mahsulotni qo'shing. "))

# if savat:
#     for mahsulot in savat:
#         if mahsulot in mahsulotlar:
#             print(f"Do'konimizda {mahsulot} bor. ")
#         else:
#             print(f"Do'konimizda {mahsulot} yo'q. ")

# else:
#     print("Savatingiz bo'sh.")



# M5

# mahsulotlar = ['un', "yog'", "sovun", 'tuxum', 'piyoz',
#                'kartoshka', 'olma', 'banan', 'uzum', 'qovun']


# savat = []
# for n in range(5):
#     savat.append(input(f'Savatga {n+1}-mahsulotni qo\'shing: ')) # qoshtirnoqda xato bittalik qolandan qolasa boladi lekin ozek adabiyotida ayrim sozlarni belgisi bor shu halaqit qiladi lekin uniiham eplasa boladi qanday maslana: do\'kon deb yoziladi shu belgi bilan ---> \

# bor_mahsulotlar = []
# mavjud_emas = []
# for mahsulot in savat:
#     if mahsulot in mahsulotlar:
#         bor_mahsulotlar.append(mahsulot) # buyerda sintaktik hato mahsulot boladi mahslot emas.
#     else:
#         mavjud_emas.append(mahsulot)

# if mavjud_emas:
#     print("Do'konimizda quyidagi mahsulotlar yo'q:") # bu yerda tab xato ketgan edi.
#     for mahsulot in mavjud_emas:
#         print(mahsulot)
# else:
#   print("Siz so'ragan barcha mahsulotlar do'konimizda bor")
    


# M6

# users = ['alisher1983','aziza','yasina' 'umar']

# login = input("Yangi login tanlang:" ) # bir tomniga " ikktalik bir tomoniga bitali ' qosh tirnoq yozilganedi.

# if login in users:
#     print('Login band, yangi login tanalng!')
# else:
#     print("Xush kelibsiz!")