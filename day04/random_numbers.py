from random import randint
from collections import Counter



random_numbers = [randint(1,1000) for item in range(1_000_000)]

print(Counter(random_numbers))