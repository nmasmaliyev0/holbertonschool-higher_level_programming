#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
last_digit = int(str(number)[-1]) if number > 0 else int("-" + str(number)[-1])
result = f"Last digit of {number} is {last_digit} and"
if last_digit > 5:
    result += " is greater than 5"
elif last_digit < 6 and last_digit != 0:
    result += " and is less than 6 and not 0"
else:
    result += " is 0"
print(result)
