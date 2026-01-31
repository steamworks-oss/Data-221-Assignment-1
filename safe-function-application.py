# variables
pairs = [[5, 2], [3, -1], [4, 3], [2, 0]]

# recursive function that computes x^y for integers with y>=0
def safeExponentiation(x: int, y: int) -> int:
    if y == 0:
        return 1
    else:
        return x * safeExponentiation(x, y - 1)

# loop to apply function to each pair in list and storing the result in a list while skipping any pair where the exponent is negative
results = list()
for pair in pairs:
    if pair[1] >= 0:
        results.append(safeExponentiation(*pair))

# print resulting list
print(f"The exponentiation results of the pairs list (with nonnegative exponents) is:\n {results}")