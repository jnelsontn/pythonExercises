import random

random_numbers = [ random.randrange(0, 50) for x in range(50) ]

squared_random_numbers = [ x**2 for x in random_numbers ]

print(random_numbers)
print(squared_random_numbers)