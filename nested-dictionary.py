import pprint

# variable
strings = ["data", "science"]

# function that takes a list of strings and returns a nested dictionary of the strings paired with its length and parity
def nestedDictionaryFromStrings(strings: list) -> dict:
    nestedDictionary = dict()
    # add dictionary values for each string and calculate its length and parity
    for string in strings:
        nestedDictionary[string] = {
            "length": len(string),
            "parity": "even" if len(string) % 2 == 0 else "odd"
        }
    return nestedDictionary

# apply function to string list and print the resulting dictionary
print(f"The nested dictionary is:")
pprint.pprint(nestedDictionaryFromStrings(strings))