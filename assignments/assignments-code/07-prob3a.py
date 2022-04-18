
def ascii_shift(word, shift):
    shifted_word = ""
    for i in range(0, len(word)):
        shifted_word += chr(ord(word[i]) + shift)
    return shifted_word

ascii_shift("apple", 1)

'''        
word = "ABCDEFG"
for i in range(-5, 6):
    print ("ASCII shifting", word, "by", i, "=>", ascii_shift(word, i))
'''

def shift_right(word):
    shifted_word = word[len(word)-1]
    for i in range(0, len(word)-1):
        shifted_word += word[i]
    return shifted_word

'''
word = "hello world!"
print("Shifting right", word, "=>", shift_right(word))
'''

def shift_left(word):
    shifted_word = ""
    for i in range(1, len(word)):
        shifted_word += word[i]
    shifted_word += word[0]
    return shifted_word

'''
word = "hello world!"
print("Shifting left", word, "=>", shift_left(word))
'''

# ABCDEFG
# 0123456
# 123456
# 012345
def flip(word):
    if len(word) > 0:
        if len(word) % 2 == 0:
            flipped_word = word[len(word)//2:] + word[:len(word)//2:]
        else:
            flipped_word = word[len(word)//2 + 1:] + word[len(word)//2] + word[:len(word)//2]
        return flipped_word
    else:
        return ""

'''
word = "ABCDEFG"
print ("Flipping", word, "=>", flip(word))

word = "123456"
print ("Flipping", word, "=>", flip(word))
'''
import random

def add_letters(word, number):
    # create list of ords for A-Z [65-90]; a-z[97-122]
    ord_info = []
    for num in range(65,91):
        ord_info.append(num)
    for num in range(97, 123):
        ord_info.append(num)
    output = ""
    for i in range(0, len(word)):
        output += word[i]
        for j in range(0, number+1):
            rand_ord = random.choice(ord_info)
            output += chr(rand_ord)

    return output

'''
# define original word
original = "Hello!"

# loop to demonstrate the function
for num in range(1, 5):

    # scramble the word using 'num' extra characters
    scrambled = add_letters(original, num)

    # output
    print ("Adding", num, "random characters to", original, "->", scrambled)
'''

def delete_characters1(word, number):
    i = 0
    output = ""
    while i < len(word):
        output += word[i]
        i += 1
        i += number
    return output

def delete_characters(word, number):
    return word[::number+1]

'''       
word1 = "HdeulHlHom!t"
word2 = "HTLedklFNljioMH!bi"
word3 = "HHHZeZrflqSflzOiosNU!jBk"
word4 = "HFtRKeivFllRNlUlGTaooYwoH!JpXL"

unscrambled1 = delete_characters(word1, 1)
print ("Removing 1 characer from", word1, "->", unscrambled1)

unscrambled2 = delete_characters(word2, 2)
print ("Removing 2 characers from", word2, "->", unscrambled2)

unscrambled3 = delete_characters(word3, 3)
print ("Removing 3 characers from", word3, "->", unscrambled3)

unscrambled4 = delete_characters(word4, 4)
print ("Removing 4 characers from", word4, "->", unscrambled4)
'''

while True:
    pattern = input("Enter an encoding pattern, 'end' to end: ")
    word = input("Enter a word to encode/decode: ")
    if pattern == "end":
        break
    for c in pattern:
        if c == 'A':
            print("* Added 1 character:", end=" ")
            print(add_letters(word, 1))
            word = add_letters(word, 1)
        elif c == 'X':
            print("* Deleted 1 character:", end=" ")
            print(delete_characters(word,1))
            word = delete_characters(word,1)
        elif c == 'F':
            print("* Flipped:", end=" ")
            print(flip(word))
            word = flip(word)
        elif c == 'U':
            print("* ASCII shifted up:", end=" ")
            print(ascii_shift(word, 1))
            word = ascii_shift(word, 1)
        elif c == 'D':
            print("* ASCII shifted down:", end=" ")
            print(ascii_shift(word, -1))
            word = ascii_shift(word, -1)
        elif c == 'L':
            print("* Shifted left:", end=" ")
            print(shift_left(word))
            word = shift_left(word)
        elif c == 'R':
            print("* Shifted right:", end=" ")
            print(shift_right(word))
            word = shift_right(word)
        
        

        
