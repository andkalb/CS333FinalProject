from Expression import *
from TruthTable import *

def main():
    while(True):
        print("\nA Valid Boolean Algebra Expression contains only uppercase variables (A-Z), and operators +,',(,)")
        print("An example would be \"A + B'CD\"")
        expr = input("Enter an expression, or 'quit' to quit: ")
        if (expr == "quit"):
            break
        
        print()

        expression = Expression(expr)
        expression.removeWhiteSpace()
        if expression.checkSyntax():
            table = TruthTable(expression)
            print(table.toStr())
        else:
            print("Invalid Expression!")

if __name__ == '__main__':
    main()