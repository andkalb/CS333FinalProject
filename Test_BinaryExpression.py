import unittest
from BinaryExpression import *

class Test_BinaryExpression(unittest.TestCase):

    def test_reset(self):
        e = BinaryExpression('0+1')
        e.reset('')
        self.assertEqual(e.expression, '')

    def test_eliminateNots(self):
        e = BinaryExpression('0+0\'\'\'0\'\'+0\'')
        e.eliminateNots()
        self.assertEqual(e.expression, '0+10+1')
        
        e.reset('0+0+0+0+0+0')
        e.eliminateNots()
        self.assertEqual(e.expression, '0+0+0+0+0+0')
        
        e.reset('1\'+0\'+1\'\'')
        e.eliminateNots()
        self.assertEqual(e.expression, '0+1+1')

    def test_eliminateAnds(self):
        e = BinaryExpression('10+1+0+010')
        e.eliminateAnds()
        self.assertEqual(e.expression, '0+1+0+0')

        e.reset('111+1110+0')
        e.eliminateAnds()
        self.assertEqual(e.expression, '1+0+0')

    def test_eliminateOrs(self):
        e = BinaryExpression('0+1+0+0')
        e.eliminateOrs()
        self.assertEqual(e.expression, '1')

        e.reset('1+0+0')
        e.eliminateOrs()
        self.assertEqual(e.expression, '1')

        e.reset('0+0')
        e.eliminateOrs()
        self.assertEqual(e.expression, '0')

        e.reset('0')
        e.eliminateOrs()
        self.assertEqual(e.expression, '0')

    def test_eliminateInnermostParentheses(self):
        e = BinaryExpression('10\'1+1\'\'+0\'+0\'')
        e.eliminateInnermostParentheses()
        self.assertEqual(e.expression, '1')

        # e.reset('()')
        # e.eliminateInnermostParentheses()
        # self.assertEqual(e.expression, '')

        e.reset('(0)')
        e.eliminateInnermostParentheses()
        self.assertEqual(e.expression, '0')

        e.reset('(1+(0))')
        e.eliminateInnermostParentheses()
        self.assertEqual(e.expression, '(1+0)')

        e.reset('(1+(0)1(0+0))')
        e.eliminateInnermostParentheses()
        self.assertEqual(e.expression, '(1+(0)10)')

if __name__ == '__main__':
    unittest.main()
