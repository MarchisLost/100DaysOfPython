import art
from game_data import data
import random
import os


def printStuff(personA, personB, currentScore):
    os.system('cls||clear')
    print(art.logo)
    if currentScore != 0:
        print("You're right! Current score: ", currentScore)

    print(f"Compare A: {personA['name']}, a {personA['description']}, from {personA['country']}")
    print(art.vs)
    print(f"Against B: {personB['name']}, a {personB['description']}, from {personB['country']}")

    answer = input('Who has more followers? Type \'A\' or \'B\': ').capitalize()
    return answer


wrongAnswer = False
currentScore = 0
while wrongAnswer is False:
    nr2 = random.randint(0, len(data))
    nr1 = random.randint(0, len(data))
    while nr1 == nr2:
        nr1 = random.randint(0, len(data))
    personA = data[nr1]
    personB = data[nr2]
    answer = printStuff(personA, personB, currentScore)

    if personA['follower_count'] > personB['follower_count']:
        rightAnswer = 'A'
    else:
        rightAnswer = 'B'

    if answer != rightAnswer:
        wrongAnswer = True
        os.system('cls||clear')
        print(art.logo)
        print('Sorry, thats wrong. Final score:', currentScore)
    else:
        currentScore += 1
