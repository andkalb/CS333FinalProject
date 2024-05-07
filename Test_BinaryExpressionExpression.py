import unittest
from Expression import *
from BinaryExpression import *

class Test_BinaryExpressionExpression(unittest.TestCase):
    
    def test_expressionToBinaryExpression(self):
        # integration test for converting an expression to a binary expression to a result
        e = Expression('A+BD\'')
        be = BinaryExpression(e.toBinaryExpressionStr())
        be.eliminateInnermostParentheses()
        self.assertEqual(be.expression, '1')

        # integration test for converting an empty expression to a binary expression to a result
        e = Expression('()')
        be = BinaryExpression(e.toBinaryExpressionStr())
        be.eliminateInnermostParentheses()
        self.assertEqual(be.expression, '1')


if __name__ == "__main__":
    unittest.main()