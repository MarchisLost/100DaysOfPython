from typing import Text
import art
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']


def caesar(text, shift, direction):
    encodedText = ''
    for letter in text:
        if not letter.isalpha():
            encodedText = encodedText + letter
            continue
        indexold = alphabet.index(letter)
        if direction == 'encode':
            indexnew = indexold + shift
        elif direction == 'decode':
            indexnew = indexold - shift
        encodedText += alphabet[indexnew]
    return encodedText


print(art.logo)
bol = 'yes'
while bol == 'yes':
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    while direction not in ['encode', 'decode', 'yes']:
        print('Write either encode or decode, try again dumbass!')
        direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")

    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))
    shift = shift % 26
    
    finalWord = caesar(text, shift, direction)
    print('The', direction, 'text is', finalWord, '\n')

    bol = input("Type 'yes' if you want to go again, type 'no' otherwise\n").lower()
    if bol == 'no':
        print('Thank you for playing!')
