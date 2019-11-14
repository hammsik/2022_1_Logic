from hangman import Hangman
from guess import Guess
from word import Word


def gameMain():
    word = Word('words.txt')
    guess = Guess(word.randFromDB())
    hangman = Hangman()
    maxTries = hangman.getLife()

    while guess.numTries < maxTries:

        display = hangman.get(maxTries - guess.numTries)
        print(display)
        guess.display()

        while True:
            guessedChar = input('Select a letter: ')
            if len(guessedChar) != 1:
                print('One character at a time!')
                continue
            elif guessedChar in guess.guessedChars:
                print('You already guessed \"' + guessedChar + '\"')
                continue
            elif not guessedChar.isalpha():
                print("Enter only alphabet!")
                continue
            elif guessedChar.isupper():
                print("Enter only lower!")
                continue
            else:
                break

        if guess.guess(guessedChar) == True:
            break

    if guess.guess(guessedChar):
        print('Success! The SecretWord is %s' %guess.secretWord)
    else:
        print(hangman.get(0))
        print('word [' + guess.secretWord + ']')
        print('guess [' + guess.currentStatus + ']')
        print('Fail')


if __name__ == '__main__':
    gameMain()