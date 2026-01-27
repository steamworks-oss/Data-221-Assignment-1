# store variables
threshold = 100
product = 1
currentNumber = 1

# repeatedly multiply product with consecutive integers until product is greater than threshold
while (product <= threshold):
    product *= currentNumber
    currentNumber += 1

# print out final product and the final integer
print(f"The final product is: {product}")
print(f"The integer that caused the product to exceed the threshold is: {currentNumber}")