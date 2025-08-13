'''11/08/2025'''

import random

while True:

    def play_pc(x):

        print("Keling Son topish o'yini oynaymiz.")
        input("O'yindi boshlash uchun istalgan tugmani bosing.\n ")
        print(" 1 dan 10 gacha son o'yladim. Topa olasizmi?: ")

        pc = random.randint(1, x)
        human_n = 0
        while True:
            
            human_n += 1
            human = int (input("Sonni kriting: "))

            if pc == human:
                print(f"TABRIKLAYMAN men oylagan sonni {human_n} urinishda topdingiz. Bu son: {pc} soni edi.")
                break
            elif pc > human:
                print(f"Xato, men oylagan son bundan kattaroq. Yana haraka qiling: ")
                
            else:
                print(f"Xato, men oylagan son bundan kichikroq. Yana harakat qiling: ")
                
        return human_n



    def play_human(x, y):

        print("\n1 dan 10 gacah son oylang. Men esa topaman. ")
        input("Son o'ylagan bo'lsangiz istalgan tugmani bosing. ")

        pc_n = 0
        while True:
            pc_n +=1 
            pc1 = random.randint(x, y)
            human_son = input(f"Siz {pc1} sonini o'yladingiz: To'gri (T), men o'ylagan son bundan kattaroq (+), yoki kichikroq bo'lsa (-)?? ")

            if human_son == "t":
                print(f"\nMen siz oylagan sonni {pc_n} urinishda topdim.")
                break
            elif human_son == "+": 
                x = pc1 +1
                
            elif human_son == "-":
                y = pc1 - 1
                
        return pc_n

    human_n = play_pc(10)
    pc_n = play_human(1, 10)

    if human_n < pc_n:
        print(f"Siz yutdingiz! Siz {human_n} urinishda topdingiz, kompyuter esa {pc_n} urinishda.")
    elif human_n > pc_n:
        print(f"Kompyuter yutdi! Kompyuter {pc_n} urinishda topdi, siz esa {human_n} urinishda.")
    else:
        print(f"Durrang! Ikkovingiz ham {human_n} urinishda topdingiz.")

    javob = input("\nYana o'ynaymizmi? (yes/no):")
    if javob == "no":
        break

