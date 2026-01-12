# Default code: https://raw.githubusercontent.com/hs-hq-service/3156/refs/heads/main/factorial.py 
# ChatGPT chat: https://chatgpt.com/share/6964bbf9-9b28-8008-80a6-2f0af0925a0a

#!/usr/bin/python3
import sys

def factorial(n):
    result = 1
    while n > 1:
        result *= n
        n -= 1

    return result

f = factorial(int(sys.argv[1]))
print(f)
