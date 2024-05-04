from Expression import *
from BinaryExpression import *

class TruthTable:

    def __init__(self, expression):
        self.expression = expression
        self.expression.fillVariablesList()
        self.table = self.generateTable()

    def generateTable(self):
        table = []
        header = []
        for i in range(len(self.expression.variables)):
            if self.expression.variables[i] != '?':
                header.append(chr(ord('A') + i))

        header.append('Out')
        table.append(header)

        # simulate do while
        entered = False
        while not entered or self.expression.digitValueBinary != 0:
            row = []
            if not entered:
                entered = True
            
            for variable in self.expression.variables:
                if variable != '?':
                    row.append(variable)
            
            be = BinaryExpression(self.expression.toBinaryExpressionStr())
            while be.expression != '0' and be.expression != '1':
                be.eliminateInnermostParentheses()

            row.append(be.expression)
            table.append(row)
            self.expression.nextBinaryValueForVariables()

        return table
    
    def toStr(self):
        ret = ''
        for row in self.table:
            ret += "|"
            for entry in row:
                if entry == "Out":
                    ret += "  " + entry + "  |"
                else:
                    ret += "   " + entry + "   |"
            ret += "\n"
        return ret
