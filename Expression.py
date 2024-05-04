
class Expression:
    
    def __init__(self, expression):
        self.reset(expression)

    def reset(self, expression):
        self.variables = ['?'] * 26
        self.digitValueBinary = 0
        self.expression = expression

    def removeWhiteSpace(self):
        self.expression = self.expression.replace(' ', '')

    def checkSyntax(self):
        # check that parentheses are matching
        count = 0
        for char in self.expression:
            if char == '(':
                count += 1
            elif char == ')':
                count -=1
            
            if (count < 0):
                return False
        
        if count != 0:
            return False
        
        # check that all symbols are A-Z or +,',(,)
        for char in self.expression:
            if char != '+' and char != '\'' and char != '(' and char != ')':
                if not char.isalpha() or not char.isupper():
                    return False

        # check that there are no contiguous + symbols
        for i in range(len(self.expression) - 1):
            if self.expression[i] == self.expression[i + 1] == '+':
                return False

        # check that ' symbols are only after variables or other ' (not +,( or out of index)
        for i in range(len(self.expression)):
            if self.expression[i] == '\'':
                if (i == 0):
                    return False
                if self.expression[i-1] == '+' or self.expression[i-1] == '(':
                    return False

        # check that the first/last character is not a +
        if self.expression[0] == '+' or self.expression[-1] == '+':
            return False

        return True

    def fillVariablesList(self):
        for char in self.expression:
            if char != '+' and char != '\'' and char != '(' and char != ')':
                self.variables[ord(char) - ord('A')] = '0'

    def convertExpressionVariablesToBinary(self):
        expr = self.expression
        i = 0
        for char in self.variables:
            if char != '?':
                expr = expr.replace(chr(i + ord('A')), char)
            i += 1
        
        return expr

    def nextBinaryValueForVariables(self):
        self.digitValueBinary += 1
        if self.digitValueBinary >= (2 ** (26 - self.variables.count('?'))):
            self.digitValueBinary = 0

        binaryString = bin(self.digitValueBinary)[2:] # remove the 0b

        i = 1
        for index in range(len(self.variables)):
            if self.variables[len(self.variables) - index - 1] != '?':
                if len(binaryString) - i < 0:
                    self.variables[len(self.variables) - index - 1] = '0'
                else:
                    self.variables[len(self.variables) - index - 1] = binaryString[len(binaryString) - i]
                    i += 1

    def toBinaryExpressionStr(self):
        ret = ''
        for char in self.expression:
            if ord(char) - ord('A') < len(self.variables) and ord(char) - ord('A') >= 0:
                ret += self.variables[ord(char) - ord('A')]
            else:
                ret += char
        return ret