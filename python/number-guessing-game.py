import random
counter = 0
min = int(input('Enter minimum range: '))
max = int(input('Enter maximum range: '))
answer = random.randint(min, max)

def guess():
    global counter
    global answer

    userInput = int(input('Enter your guess: '))
    counter += 1
    
    if answer > userInput:
        print('The answer is greater than your guess!')
        guess()
    elif answer < userInput:
        print('The answer is less than your guess!')
        guess()
    else:
        print('You win!, you took ' + str(counter) + ' guesses!')

guess()