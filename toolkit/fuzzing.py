
import random
import string

def fuzz_string(length=10):
    return ''.join(random.choice(string.printable) for _ in range(length))
