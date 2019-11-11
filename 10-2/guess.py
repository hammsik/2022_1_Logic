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
        fail = 1
        self.guessedChars.append(character)
	
        for i in range(len(self.secretWord)):
            if character == self.secretWord[i]:
                self.currentStatus = self.currentStatus[:i] + character + self.currentStatus[(i+1):]
                fail = 0

        self.numTries += fail
