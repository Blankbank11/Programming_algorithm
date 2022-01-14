import random
from collections import Counter

number = random.randint(100000,1000000)
print(number)

number = str(number)
number_length = Counter(number)

for k,v in number_length.items():
    if v > 1:
        print(f"{k} is happening {v} times")