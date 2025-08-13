'''13/08/2025'''

import random
from uzwords import words

def get_word():

    word = random.choice(words)
    while "-" in words or " " in word:
        word = random.choice(words)
    return word.upper()


def display(user_letters, word):

    display_letter = ""
    for letter in word:
        if letter in user_letters:
            display_letter += letter
        else:
            display_letter +="-"
    return display_letter

def play():

    word = get_word()
    word_letters = set(word)
    user_letters = ""
    print(f"Men {len(word)} xonali so'z o'yladim. Topa olasizmi? ")

    while word_letters:
        print(display(user_letters, word))
        if user_letters:
            print(f"Shu vaqitgacha kiritgan hariflaringiz: {user_letters}")
        

        letter = input("Harf kriting: ").upper()
        if letter in user_letters:
            print("Bu harfni avval kiritgansiz. Boshqa harf kiriting. ")
            continue
        elif letter in word:
            word_letters.remove(letter)
            print(f"{letter} harfi to'g'ri. ")
        else:
            print("Bunday harf yo'q. ")
        
        user_letters += letter
    print(f"Tabriklayman! {word} so'zini {len(user_letters)} ta urinishda topdingiz. ")

play()