import random
import hangman_art
import hangman_words
import os

chosen_word = random.choice(hangman_words.word_list)
lives = 6

print(hangman_art.logo, "\n") #Print the hangman logo
#print('The word is:', chosen_word)

#Create blanks
display = []
for i in chosen_word:
    display.append('_')
    #OR display += '_'
print(display)

#Check if all the letters have been found
while '_' in display:
    #Check guessed word
    user_choice = (input('Choose a letter: ')).lower()
    os.system('cls||clear')
    if user_choice in display:
        print('You have already guessed the letter: ', user_choice)
        continue
    j=0
    for letter in chosen_word:
        if user_choice == letter:
            display[j] = letter
        j+=1

    if user_choice not in chosen_word:
        lives -= 1
        #print(lives)
        print(hangman_art.stages[lives])
        print('The letter', user_choice, 'is not in the word, you lose a live')
        if lives == 0:
            print('You lose, the word was', chosen_word)
            break
    
    print(display)
    if '_' not in display:
        print('You win')
