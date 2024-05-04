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
        pass

if __name__ == "__main__":
    unittest.main()