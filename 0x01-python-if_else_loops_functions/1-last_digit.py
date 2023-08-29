#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
str_n = str(abs(number))
last_dig = int(str_n[-1])
str_s = "and is 0,and is greater than 5,and is less than 6 and not 0"
str_s = str_s.split(",")
if number < 0:
    last_dig *= -1
if last_dig == 0:
    str_s = str_s[0]
elif last_dig > 5:
    str_s = str_s[1]
else:
    str_s = str_s[2]
print(f"Last digit of {number} is {last_dig} {str_s}")
