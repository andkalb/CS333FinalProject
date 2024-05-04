import unittest
from Expression import *

class Test_Expression(unittest.TestCase):

    def test_reset(self):
        e = Expression('A+B')
        e.reset('')
        self.assertEqual(e.expression, '')
        self.assertEqual(e.digitValueBinary, 0)
        self.assertEqual(len(e.variables), 26)
        self.assertEqual(e.variables.count('?'), 26)

    def test_removeWhiteSpace(self):
        e = Expression('   A +   BC\'+ A D  ')
        e.removeWhiteSpace()
        self.assertEqual('A+BC\'+AD', e.expression)
        
        e.reset(' A ')
        e.removeWhiteSpace()
        self.assertEqual('A', e.expression)

    def test_checkSyntax(self):
        e = Expression('A+BC')
        self.assertEqual(e.checkSyntax(), True)

        e.reset('AB')
        self.assertEqual(e.checkSyntax(), True)

        e.reset('Ab')
        self.assertEqual(e.checkSyntax(), False)

        e.reset('A\'+Z')
        self.assertEqual(e.checkSyntax(), True)

        e.reset('\'A\'+Z')
        self.assertEqual(e.checkSyntax(), False)

        e.reset('A+\'Z')
        self.assertEqual(e.checkSyntax(), False)

        e.reset('AB+')
        self.assertEqual(e.checkSyntax(), False)

        e.reset('(A(B+C\'))')
        self.assertEqual(e.checkSyntax(), True)

        e.reset('((AB)+C\'')
        self.assertEqual(e.checkSyntax(), False)

        e.reset('A++B')
        self.assertEqual(e.checkSyntax(), False)

        
    def test_fillVariableList(self):
        e = Expression('A+BC\'')
        e.fillVariablesList()
        self.assertEqual(e.variables[ord('A') - ord('A')], '0')
        self.assertEqual(e.variables[ord('B') - ord('A')], '0')
        self.assertEqual(e.variables[ord('C') - ord('A')], '0')
        self.assertEqual(e.variables[7], '?')

        e.reset('AA+F+Z')
        e.fillVariablesList()
        self.assertEqual(e.variables[ord('A') - ord('A')], '0')
        self.assertEqual(e.variables[ord('F') - ord('A')], '0')
        self.assertEqual(e.variables[ord('Z') - ord('A')], '0')
        self.assertEqual(e.variables[1], '?')

    def test_convertExpressionVariablesToBinary(self):
        e = Expression('A+BC\'')
        e.fillVariablesList()
        self.assertEqual(e.convertExpressionVariablesToBinary(), '0+00\'')
        
        e = Expression('A+C\'+DF\'')
        e.fillVariablesList()
        self.assertEqual(e.convertExpressionVariablesToBinary(), '0+0\'+00\'')

    def test_nextBinaryValueForVariables(self):
        e = Expression('A+D\'')
        e.fillVariablesList()
        self.assertEqual(e.digitValueBinary, 0)
        self.assertEqual(e.variables[ord('A') - ord('A')], '0')
        self.assertEqual(e.variables[ord('D') - ord('A')], '0')
        e.nextBinaryValueForVariables()
        self.assertEqual(e.digitValueBinary, 1)
        self.assertEqual(e.variables[ord('A') - ord('A')], '0')
        self.assertEqual(e.variables[ord('D') - ord('A')], '1')
        e.nextBinaryValueForVariables()
        self.assertEqual(e.digitValueBinary, 2)
        self.assertEqual(e.variables[ord('A') - ord('A')], '1')
        self.assertEqual(e.variables[ord('D') - ord('A')], '0')
        e.nextBinaryValueForVariables()
        self.assertEqual(e.digitValueBinary, 3)
        self.assertEqual(e.variables[ord('A') - ord('A')], '1')
        self.assertEqual(e.variables[ord('D') - ord('A')], '1')
        e.nextBinaryValueForVariables()
        self.assertEqual(e.digitValueBinary, 0)
        self.assertEqual(e.variables[ord('A') - ord('A')], '0')
        self.assertEqual(e.variables[ord('D') - ord('A')], '0')

    def test_toBinaryExpressionStr(self):
        e = Expression('A+BD\'')
        e.fillVariablesList()
        self.assertEqual(e.toBinaryExpressionStr(), '0+00\'')
        e.nextBinaryValueForVariables()
        self.assertEqual(e.toBinaryExpressionStr(), '0+01\'')
        e.nextBinaryValueForVariables()
        self.assertEqual(e.toBinaryExpressionStr(), '0+10\'')

if __name__ == '__main__':
    unittest.main()
