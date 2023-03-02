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
print('answer:', answer)
def startGame():
    global stageNumber

    guessString = ' '.join(guess)
    print(stage[stageNumber])
    print(guessString)
    userInput = input('Enter your guess: ')

    for i in range(len(answer)):
        if userInput == answer[i]:
            guess[i] = userInput

    
    startGame()




startGame()
