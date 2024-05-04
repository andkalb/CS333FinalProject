
class BinaryExpression:

    def __init__(self, expression):
        self.reset(expression)

    def reset(self, expression):
        self.expression = expression
    
    def eliminateNots(self):
        expr = self.expression
        newExpr = ''
        # remove unnecessary nots
        i = 0
        while i < len(expr):
            if i == len(expr) - 1:
                newExpr += expr[i]
                break
            if expr[i] == '\'' and expr[i + 1] == '\'':
                i += 1
            else:
                newExpr += expr[i]
            i += 1

        newNewExpr = ''
        # now flip 1's and 0's
        i = 0
        while i < len(newExpr):
            if i == len(newExpr) - 1:
                newNewExpr += newExpr[i]
                break
            if newExpr[i + 1] == '\'':
                newNewExpr += chr(ord('0') + ((ord(newExpr[i]) - ord('0')) + 1) % 2)
                i += 1
            else:
                newNewExpr += newExpr[i]
            i += 1
        self.expression = newNewExpr

    def eliminateAnds(self):
        splitExpr = self.expression.split('+')
        result = ''
        for string in splitExpr:
            booleanResult = 1
            for char in string:
                booleanResult = booleanResult and (ord(char) - ord('0'))
            result += chr(booleanResult + ord('0'))
            result += '+'
        result = result[:-1]
        self.expression = result
    
    def eliminateOrs(self):
        exprSplit = self.expression.split('+')
        booleanResult = False
        for string in exprSplit:
            booleanResult = booleanResult or bool(ord(string[0]) - ord('0'))

        self.expression = chr(booleanResult + ord('0'))

    def eliminateInnermostParentheses(self):
        startIndex = self.expression.rfind('(')
        endIndex = -1
        if startIndex == -1:
            startIndex = 0

        i = startIndex
        while i < len(self.expression):
            if self.expression[i] == ')':
                endIndex = i
                break
            i += 1

        if endIndex == -1:
            endIndex = len(self.expression)
        
        b = BinaryExpression(self.expression[startIndex:endIndex])
        b.eliminateNots()
        b.eliminateAnds()
        b.eliminateOrs()

        if endIndex == len(self.expression):
            self.expression = self.expression[0:startIndex] + b.expression
        else:
            self.expression = self.expression[0:startIndex] + b.expression + self.expression[endIndex + 1:]
