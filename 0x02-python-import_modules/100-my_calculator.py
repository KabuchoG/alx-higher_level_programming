#!/usr/bin/python3
if __name__ == "__main__":
    from calculator_1 import sub, mul, div, add
    import sys
    arg = sys.argv
    if len(arg) < 4:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        sys.exit(1)
    a = arg[1]
    a = int(a)
    operator = arg[2]
    c = arg[3]
    c = int(c)
    if operator != '+' or operator != '-' or operator != '*' or operator != '/':
        print("Unknown operator. Available operators: +, -, * and /")
        sys.exit(1)
    elif operator == '+':
        print("{} {} {} = {}".format(a, operator, b, add(a, b)))
    elif operator == '-':
        print("{} {} {} = {}".format(a, operator, b, sub(a, b)))
    elif operator == '*':
        print("{} {} {} = {}".format(a, operator, b, mul(a, b)))
    elif operator == '/':
        print("{} {} {} = {}".format(a, operator, b, div(a, b)))
