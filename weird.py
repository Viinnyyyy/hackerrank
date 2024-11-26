import math
import os
import random
import re
import sys
import time
from random import randrange

start = time.time()
if __name__ == '__main__':
    n = randrange(100)
    # n = int(input().strip())
    if n % 2 != 0:
        print("Weird")
    else:
        if 1 < n < 6:
            print("Not Weird")
        if 5 < n <= 20:
            print("Weird")
        if n > 20:
            print("Not Weird")
end = time.time()
print(end - start)
