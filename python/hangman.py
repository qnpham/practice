import random
stage = [
'   _____ \n'
'  |      \n'
'  |      \n'
'  |      \n'
'  |      \n'
'  |      \n'
'__|__\n',
'   _____ \n'
'  |  |   \n'
'  |      \n'
'  |      \n'
'  |      \n'
'  |      \n'
'__|__\n',
'   _____ \n'
'  |  |   \n'
'  |  O   \n'
'  |      \n'
'  |      \n'
'  |      \n'
'__|__\n',
'   _____ \n'
'  |  |   \n'
'  |  O   \n'
'  |  |   \n'
'  |      \n'
'  |      \n'
'__|__\n',
'   _____ \n'
'  |  |   \n'
'  |  O   \n'
'  | /|   \n'
'  |      \n'
'  |      \n'
'__|__\n',
'   _____ \n'
'  |  |   \n'
'  |  O   \n'
'  | /|\  \n'
'  |      \n'
'  |      \n'
'__|__\n',
'   _____ \n'
'  |  |   \n'
'  |  O   \n'
'  | /|\  \n'
'  | /    \n'
'  |      \n'
'__|__\n',
'   _____ \n'
'  |  |   \n'
'  |  O   \n'
'  | /|\  \n'
'  | / \  \n'
'  |      \n'
'__|__\n'
'\n'
'GAME OVER \n'
]

words = ['pear', 'food', 'board', 'pizza', 'screen', 'sleep', 'shower', 'apple',
         'banana', 'grape', 'juice', 'stop', 'watch', 'play', 'clean', 'rest']

answer = words[random.randint(0, len(words) - 1)]
guess = []
stageNumber = 0
for i in range(len(answer)):
    guess.append('_')
def startGame():
    global stageNumber
    levelFail = True

    guessString = ' '.join(guess)
    print(stage[stageNumber])
    if stageNumber == 7:
        exit()
    print(guessString)

    userAnswer = ''.join(guess)
    if userAnswer == answer:
        print('You win!')
        exit()

    userInput = input('Enter your guess: ')
    if len(userInput) > 1:
        print('Only 1 character inputs allowed!')
        levelFail = False
    else:
        for i in range(len(answer)):
            if userInput == answer[i]:
                guess[i] = userInput
                levelFail = False

    if levelFail == True:
        stageNumber += 1
    
    startGame()

startGame()
