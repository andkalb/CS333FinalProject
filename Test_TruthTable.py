import unittest
from TruthTable import *
from Expression import *
from BinaryExpression import *

class Test_TruthTable(unittest.TestCase):
    
    # integration test between expression and truthtable
    def test_generateTable(self):
        e = Expression('A+B')
        tt = TruthTable(e) # generateTable is called
        self.assertEqual(tt.table, [['A', 'B', 'Out'],
                                    ['0', '0', '0'],
                                    ['0', '1', '1'],
                                    ['1', '0', '1'],
                                    ['1', '1', '1']])
        
        e.reset('A\'F')
        tt = TruthTable(e) # generateTable is called
        self.assertEqual(tt.table, [['A', 'F', 'Out'],
                                    ['0', '0', '0'],
                                    ['0', '1', '1'],
                                    ['1', '0', '0'],
                                    ['1', '1', '0']])
        
        e.reset('A+(A\'F)')
        tt = TruthTable(e) # generateTable is called
        self.assertEqual(tt.table, [['A', 'F', 'Out'],
                                    ['0', '0', '0'],
                                    ['0', '1', '1'],
                                    ['1', '0', '1'],
                                    ['1', '1', '1']])
        
        e.reset('Z')
        tt = TruthTable(e) # generateTable is called
        self.assertEqual(tt.table, [['Z', 'Out'],
                                    ['0', '0'],
                                    ['1', '1']])
        
        e.reset('(Z\')\'')
        tt = TruthTable(e) # generateTable is called
        self.assertEqual(tt.table, [['Z', 'Out'],
                                    ['0', '0'],
                                    ['1', '1']])
        
        e.reset('((Z))')
        tt = TruthTable(e) # generateTable is called
        self.assertEqual(tt.table, [['Z', 'Out'],
                                    ['0', '0'],
                                    ['1', '1']])
        
        e.reset('Z()')
        tt = TruthTable(e) # generateTable is called
        self.assertEqual(tt.table, [['Z', 'Out'],
                                    ['0', '0'],
                                    ['1', '1']])

    def test_toStr(self):
        e = Expression('A+B')
        tt = TruthTable(e)
        self.assertEqual(tt.toStr(), '|   A   |   B   |  Out  |\n|   0   |   0   |   0   |\n|   0   |   1   |   1   |\n|   1   |   0   |   1   |\n|   1   |   1   |   1   |\n')

    def test_expressionIsUntouched(self):
        e = Expression('A+B+C')
        tt = TruthTable(e)

        # integration test to make sure expression string is untouched
        self.assertEqual(e.expression, 'A+B+C')

        # integration test to make sure expression class is left on the first binary value (0)
        self.assertEqual(e.digitValueBinary, 1)

if __name__ == "__main__":
    unittest.main()