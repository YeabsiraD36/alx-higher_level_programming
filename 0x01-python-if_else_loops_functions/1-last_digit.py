#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
last_digit = nummber % 10
if number > 5:
    print(f'Last digit of {number} is {last_digit} and greater than 5\n')
elif number == 0:
    print(f'Last digit of {number} is {last_digit} and is 0\n')
else:
    print(f'Last digit of {number} is {last_digit} and is less than 6 and not 0\n')
