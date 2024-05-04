import unittest
from Expression import *
from BinaryExpression import *

class Test_BinaryExpressionExpression(unittest.TestCase):
    
    # integration test for converting expressions to binary expressions to a result
    def test_expressionToBinaryExpression(self):
        e = Expression('A+BD\'')
        be = BinaryExpression(e.toBinaryExpressionStr())
        be.eliminateInnermostParentheses()
        self.assertEqual(be.expression, '1')


if __name__ == "__main__":
    unittest.main()