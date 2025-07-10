#A smarter Ai guessing game

import random

print("Ah yes the smarter Ai number guesser\n")

secretNumb = random.randint(1,20)

guessTaken = 0

minGuess = 1
maxGuess = 20

for guessTaken in range(6):
    guess = random.randint(minGuess, maxGuess)

    if guess < secretNumb:
        print('{} Too low\n'.format(guess))
        minGuess = guess + 1 #Need to add or subtract 1 or it keeps guessing
    elif guess > secretNumb: #the same number even if it's wrong.
        print('{} Too high\n'.format(guess))
        maxGuess = guess - 1
    elif guess == secretNumb:
        print('{} You got it!\n'.format(guess))
        break

if guess == secretNumb:
    print('Nice job you got it in {} tries'.format(guessTaken))

    if guessTaken == 0:
        print('FIRST TRY')

    elif guessTaken == 5:
        print('Got it on your last chance')

elif guess != secretNumb:
    print('I failed, how much smarter can I be??')
