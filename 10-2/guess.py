class Guess:

    def __init__(self, word):
        self.secretWord = word
        self.numTries = 0
        self.guessedChars = []
        self.currentStatus = "_" * len(word)

    def display(self):
        print("Current: %s" %(self.currentStatus))
        print("Tries: %d" %(self.numTries))


    def guess(self, character):
        self.guessedChars.append(character)

        if not(character in self.secretWord):
            self.numTries += 1
            return

        for i in range(len(self.secretWord)):
            if character == self.secretWord[i]:
                self.currentStatus = self.currentStatus[:i] + character + self.currentStatus[(i+1):]

        if self.currentStatus == self.secretWord:
            return True