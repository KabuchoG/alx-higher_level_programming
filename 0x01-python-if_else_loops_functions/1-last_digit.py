#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
if number > 0:
    number = str(number)
    val = int(number[-1])
else:
    number = str(number)
    neg = number[-1]
    val = int(neg) * -1
print(f"Last digit of {number} is {val}", end=' ')
if val > 5:
    print("and is greater than 5")
elif val == 0:
    print("and is 0")
else:
    print("and is less than 6 and not 0")
