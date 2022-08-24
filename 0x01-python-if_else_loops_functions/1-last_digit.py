#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
if number > 0:
    number = str(number)
    val = number[-1]
else:
    number = str(number)
    neg = number[-1]
    val = int(neg) * -1
print(f"Last digit of {number} is {val}", end = ' ')
num = int(number[-1])
if num > 5:
    print("and is greater than 5")
elif num == 0:
    print("and is zero")
else:
    print("and is less than 6 and not zero")
