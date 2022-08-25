#!/usr/bin/python3
if __name__ == "__main__":
    from calculator_1 import sub, mul, div, add
    import sys
    arg = sys.argv
    if len(arg) != 4:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        sys.exit(1)
    a = int(arg[1])
    operator = arg[2]
    b = int(arg[3])
    if operator != '+' and operator != '-' and operator != '*' and operator != '/':
        print("Unknown operator. Available operators: +, -, * and /")
        sys.exit(1)
    elif operator == '+':
        print("{} + {} = {}".format(a, b, add(a, b)))
    elif operator == '-':
        print("{} {} {} = {}".format(a, operator, b, sub(a, b)))
    elif operator == '*':
        print("{} {} {} = {}".format(a, operator, b, mul(a, b)))
    else:
        print("{} {} {} = {}".format(a, operator, b, div(a, b)))
