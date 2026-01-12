#!/usr/bin/python3
import sys

# Default code: https://github.com/hs-hq-service/3156/blob/main/factorial_recursive.py
# ChatGPT chat: https://chatgpt.com/share/6964cb21-c434-8008-9680-a47c6eded55b

# Function Description:
# This function calculates the factorial of a given non-negative integer using recursion.

# Parameters:
# n (int): A non-negative integer whose factorial is to be calculated.

# Returns:
# int: The factorial of the input integer n.

def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)

f = factorial(int(sys.argv[1]))
print(f)
