import unittest

from guess import Guess

class TestGuess(unittest.TestCase):

    def setUp(self):
        self.g1 = Guess('default')

    def tearDown(self):
        pass

    def testguess(self):

        self.assertTrue(self.g1.guess('t'))
        self.assertIn('t', self.g1.guessedChars)
        self.assertEqual(self.g1.currentStatus, '______t')
        self.assertEqual(self.g1.guess('p'), False)
        self.assertTrue(
            (self.g1.guess('d'), self.g1.guess('e'), self.g1.guess('f'),
             self.g1.guess('a'), self.g1.guess('u'), self.g1.guess('l'),
             self.g1.guess(''))
        )
        self.assertTrue(self.g1.finished()) #단어를 완성했을 때 finished 메소드 체크

    def testDisplayCurrent(self):
        self.assertEqual(self.g1.displayCurrent(), '_ _ _ _ _ _ _ ')
        self.g1.guess('a')
        self.assertEqual(self.g1.displayCurrent(), '_ _ _ a _ _ _ ')
        self.g1.guess('e')
        self.assertEqual(self.g1.displayCurrent(), '_ e _ a _ _ _ ')
        self.g1.guess('t')
        self.assertEqual(self.g1.displayCurrent(), '_ e _ a _ _ t ')
        self.g1.guess('u')
        self.assertEqual(self.g1.displayCurrent(), '_ e _ a u _ t ')
        self.g1.guess('p')
        self.assertEqual(self.g1.displayCurrent(), '_ e _ a u _ t ')

    def testDisplayGuessed(self):
        self.assertEqual(self.g1.displayGuessed(), ' ')
        self.g1.guess('a')
        self.assertEqual(self.g1.displayGuessed(), ' a ')
        self.g1.guess('t')
        self.assertEqual(self.g1.displayGuessed(), ' a t ')
        self.g1.guess('u')
        self.assertEqual(self.g1.displayGuessed(), ' a t u ')
        self.g1.guess('@')
        self.assertEqual(self.g1.displayGuessed(), ' @ a t u ')

if __name__ == '__main__':
    unittest.main()
