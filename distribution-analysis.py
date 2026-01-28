from pprint import pprint

# variables
numbers = [3, 1, 2, 3, 4, 2]

# function that takes a list of integers and returns a dictionary with the weight-distribution of the numbers
def numbersToDistributionDictionary(numbers: list) -> dict:
    # sort numbers list to be able to get first occurrence of a number
    numbers.sort(reverse=True)

    # create distribution dictionary keyed by numbers from the list with its value being the percentage of elements that are less than or equal to that key
    # the percentage of each element is calculated by dividing the number of elements to the right of and including its first matching index with the length of the list
    distribution = dict()
    for n in numbers:
        distribution[n] = (len(numbers) - numbers.index(n)) / len(numbers) * 100

    # return dictionary sorted by keys
    return dict(sorted(distribution.items()))

# calculate the weight of each element and print the resulting dictionary
print("The distribution analysis of the numbers is")
pprint(numbersToDistributionDictionary(numbers))