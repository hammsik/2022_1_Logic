import random

class Word:

    def __init__(self, filename):
        self.words = []
        f = open(filename, 'r')
        lines = f.readlines()
        f.close()

        self.count = 0
        for line in lines:
            word = line.rstrip()
            self.words.append(word)
            self.count += 1

        print('%d words in DB' % self.count)


    def test(self):
        return 'default'


    def randFromDB(self):
        #단어의 최소 or 최대 길이를 설정하고 조건을 만족하는 단어가 나올 때 까지 무한반복
        numLen = 10
        while True:
            r = random.randrange(self.count)
            if len(self.words[r]) >= numLen:
                return self.words[r]

