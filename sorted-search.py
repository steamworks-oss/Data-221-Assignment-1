from random import random
from pprint import pprint

# variables
values = [random() for i in range(20)]
x = random()

# sort list
values.sort()

# loop through list and store each index where the list value is greater or equal to x
indices = list()
for i in range(20):
    if values[i] >= x:
        indices.append(i)

# print the sorted values and x
print(f"The sorted list is:")
pprint(values)
print(f"The random value x is: {x}")
# print the first index in the list unless none exist
try:
    print(f"The first matching index is: {indices[0]}")
except IndexError:
    print(f"There are no matching indices.")