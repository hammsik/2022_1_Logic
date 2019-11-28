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
        self.assertEqual(self.g1.currentStatus, '_e____t')
        self.assertEqual(self.g1.guess('p'), False)
        self.assertTrue(
            (self.g1.guess('a'), self.g1.guess('d'), self.g1.guess('d'), self.g1.guess('f'), self.g1.guess('u'), self.g1.guess('l'))
        )
        self.assertEqual(self.g1.currentStatus, 'default')


    def testDisplayCurrent(self):
        self.assertEqual(self.g1.displayCurrent(), '_ e _ _ _ _ _ ')
        self.g1.guess('a')
        self.assertEqual(self.g1.displayCurrent(), '_ e _ a _ _ _ ')
        self.g1.guess('t')
        self.assertEqual(self.g1.displayCurrent(), '_ e _ a _ _ t ')
        self.g1.guess('u')
        self.assertEqual(self.g1.displayCurrent(), '_ e _ a u _ t ')
        self.g1.guess('p')
        self.assertEqual(self.g1.displayCurrent(), '_ e _ a u _ t ')

    def testDisplayGuessed(self):
        self.assertEqual(self.g1.displayGuessed(), ' e n ')
        self.g1.guess('a')
        self.assertEqual(self.g1.displayGuessed(), ' a e n ')
        self.g1.guess('t')
        self.assertEqual(self.g1.displayGuessed(), ' a e n t ')
        self.g1.guess('u')
        self.assertEqual(self.g1.displayGuessed(), ' a e n t u ')
        self.g1.guess('@')
        self.assertEqual(self.g1.displayGuessed(), ' @ a e n t u ')

if __name__ == '__main__':
    unittest.main()

