'''07/08/2025'''


# |/////////////////////////////////| FUNKSIYA |\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\|

# m1

# def salom_ber():
#     print("Assalomu alaykum! ")
# salom_ber()


# m2

# def salom_ber(ism):
#     print(f"Assalomu alaykum, hurmatli {ism.title()}")
# # salom_ber(ism= "kamoliddin")
# # salom_ber("kamoliddin")





# >>----------> DOCSTRING 


# m3

# def salom_ber(ism):
#     '''Salom beruvchi funksiya. '''
#     print(f"Assalomu alaykum, hurmatli {ism.title()}")
# salom_ber(ism="kamoliddin")
# # print(salom_ber.__doc__) # ..... > Docstringni konsolga chiqarish uchun print(funksiya_nomi.__doc__) deb ham yozishimiz mumkin: Funksiyani nima amal bajarishini bilish uchun buni dastruchi tomonida ''' ''' yozilgan bolishi kerak.




# >>>-----------------> FUNKSIYAGA BIR NECHA BOR MUROJAT QILISH <------------------<<<

# m4


# def salom_ber(ism):
#     '''Salom beruvchi funksiya. '''
#     print(f"Assalomu alaykum, hurmatli {ism.title()}")

# salom_ber(ism="kamoliddin")
# salom_ber("sardor")
# salom_ber(ism="diyorbek")
# print(salom_ber.__code__)



# >>>------------------------> ARGUMENT VA PARAMETER <-----------------------------<<<


# m5


# def toliq_ism(ism, familiya):
#     '''Foydalanuvchi ism va familiyasini jamlab chiqaruvchi funksiya'''
#     print(f"Foydalanuvchi ismi: {ism.title()}\n"
#           f"Foydalanuvhi familiyasi: {familiya.title()}")
    
# toliq_ism("kamoliddin", "raximjonov")

# toliq_ism("raximjonov", "kamoliddin") bu yerda familiya va  ism joylari ozgarib qolgan dastur togri lekin matiqan xato.
 



# m6

# def yosh_hisoblash(ism, tugulgan_yil):
#     '''Foydalanuvchi ism va tug'ulgan yilini chiqaruvchi dastur. '''
#     print(f"{ism.title()} {2025 - tugulgan_yil} yoshda")

# # yosh_hisoblash(ism= "kamoliddin", tugulgan_yil= 2005) # bu kalit orqali chiqarish, yani 
# # yosh_hisoblash("kamoliddin", 2005)
# # yosh_hisoblash(2005, "kamoliddin")     # >>> ------> # AttributeError: 'int' object has no attribute 'title'




# >>>----------> STANDART QIYMAT

# m7

# def yoshni_hisobla(tugulgan_yil, joriy_yil = 2025):
#     '''Foydalanuvchini yoshini hisoblovchi dastur.'''
#     print(f"Siz {joriy_yil - tugulgan_yil} yoshdasiz")

# yoshni_hisobla(2005)






# >>>------------------> FUNKSIYAGA MUROJAT QILISHDA XATOLIKLAR <------------------<<<

# m8

# def yosh_hisobla(tugilgan_yil, joriy_yil=2020):
#     """Foydalanuvchi tug'ilgan yilidan uning yoshini hisoblaydi"""
#     print(f"Siz {joriy_yil-tugilgan_yil} yoshdasiz")
    
# tyil = input("Tug'ilgan yilingizni kiriting: ") # error >>--> buyerda int tashlab ketilgan qiymat kiritilganda ' str ' qabul qiladi boshiga ' int ' qoshish kerak
# yosh_hisobla(tyil)


#  # error
# #     yosh_hisobla(tyil)
# #     ~~~~~~~~~~~~^^^^^^
# # TypeError: unsupported operand type(s) for -: 'int' and 'str'




# m9

# def yosh_hisobla(tugilgan_yil, joriy_yil):
#     """Foydalanuvchi tug'ilgan yilidan uning yoshini hisoblaydi"""
#     print(f"Siz {joriy_yil-tugilgan_yil} yoshdasiz")

# yosh_hisobla(1993) # error >>------> buyerda tugulgan yil berilgan lekin   ' joriy yil '   tashlab ketilgan.


#     yosh_hisobla(1993)
#     ~~~~~~~~~~~~^^^^^^
# TypeError: yosh_hisobla() missing 1 required positional argument: 'joriy_yil'



# m10

# def toliq_ism(ism, familiya):
#     """Foydalanuvchi ism va familiyasini jamlab chiqaruvchi funksiya"""
#     print(f"Foydalanuvchi ismi: {ism.title()}\n"
#           f"Foydalanuvchi familiyasi: {familiya.title()}")
 
# toliq_ism('olim hakimov') # >>-------> error ism argument ichiga familiya yozilgan lekin farqi yoq ammo ' familiya ' argument berilmagan yani qiyamt yoq 


# #     toliq_ism('olim hakimov')
# #     ~~~~~~~~~^^^^^^^^^^^^^^^^
# # TypeError: toliq_ism() missing 1 required positional argument: 'familiya'





'''07/08/2025'''

# |///////////////////////////////// | AMALIYOT |\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\|




# M1


# def f_info(ism, familiya, joriy_yil):
#     '''Foydalanuvchi haqida ma'lumot beruvchi funksiya. '''
#     print(f"Ism: {ism.title()} \nFamiliyasi: {familiya.title()} \nYosh: {joriy_yil - 2005 } yoshda")

# f_info(ism= "kamoliddin", familiya= "raximjonov", joriy_yil= 2025)


# M2

# def math(son):
#     '''Sondi kubi va kvadratini qaytaruvchi funksiya.'''
#     kv = son ** 2
#     kub = son ** 3
#     print(f"Sonning kvadrati qaytaradi: {son} -> kv: {kv} \n"
#           f"Sonning kubini qaytaradi: {son} -> kub: {kub}" )
    
# math(son= 5)



# M3

# def juft_toq(son):
#     '''Sonning juft yoki toq ekanligini tekshiruvchi funksiya.'''
#     if son %  2 == 0:
#         print(f"Juft son: {son}")
#     else:
#         print(f"Toq son: {son}")

# juft_toq(son= 4)
# juft_toq(son= 5)



# M4


# def max_min(son1, son2):
#     '''Foydalanuvchi ikkta son kiritadi u sonlarni kotta yoki kichik va teng ekanligini tekshiruvchi funksiya. '''
#     if son1 > son2:
#         print(f"Tengsizlik: {son1} > {son2}")
#     elif son1 < son2:
#         print(f"Tengsizlik: {son1} < {son2}")
#     else:
#         print(f"Tenglik: {son1} = {son2}")

# max_min(son1= 2, son2= 1)
# max_min(son1= 2, son2= 3 )
# max_min(son1= 4, son2= 4)

# # print(max_min.__doc__)




# M5

# def daraja(x, y):
#     '''Foydalanuvchi tomonidan kiritilgan  x va y sonlar, x ^ y qiymatni qaytarishi lozim'''
#     daraja1 = x ** y
#     print(f"X ning Y darajasi: {daraja1}")

# daraja(x= 3, y= 5)




# M6


# def daraja(x, y= 2):
#     '''Foydalanuvchi tomonidan kiritilgan  x va y sonlar, x ^ y ammo y = standart qiymat beriladi qiymatni qaytarishi lozim'''
#     daraja1 = x ** y
#     print(f"X ning Y darajasi: {daraja1}")

# daraja(x= 3, y= 5)
# daraja(x= 3, y= 4)
# daraja(x= 5)
# daraja(x= 9, y= 0)



# M7

# def qoldiqsiz(son):
#     '''Foydalanuvchi 2 dan 10 gacha bolgan sonlarni kirtadi va qoldiqsiz bolgan sonlarni qaytaruvchi funksiya.'''
#     for n in range(2, 11):
#         if son % n == 0:
#             print(f"{son} {n} ga qoldiqsiz bo'linadi.")

# qoldiqsiz(son= 13127283423648726876287455492873648723649872369820)