# store variables
threshold = 100
product = 1
currentNumber = 0

# repeatedly multiply product with consecutive integers until product is greater than threshold
while (product <= threshold):
    currentNumber += 1
    product *= currentNumber

# print out final product and the final integer
print(f"The final product is: {product}")
print(f"The integer that caused the product to exceed the threshold is: {currentNumber}")
