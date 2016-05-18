#How many tries will it take to roll two sixes on a pair of six-sided dice?
import random

numbers = list(range(1,7))

found_two_6s = False
rolls = 0

while not found_two_6s:
    num1 = random.choice(numbers)
    num2 = random.choice(numbers)
    print("%d, %d" % (num1, num2))

    if num1 == 6 and num2 == 6:
        found_two_6s = True
    else:
        rolls += 1

print("It took you %d tries to roll double sixes" % (rolls))