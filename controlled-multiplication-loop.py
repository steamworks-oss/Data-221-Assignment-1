threshold = 100
product = 1
currentNumber = 1

while (product <= threshold):
    product *= currentNumber
    currentNumber += 1

print(f"The final product is: {product}")
print(f"The integer that caused the product to exceed the threshold is: {currentNumber}")