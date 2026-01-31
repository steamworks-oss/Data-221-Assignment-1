# Data 221 - Assignment 1

<u>controlled-multiplication-loop.py:</u>
- Takes a number and repeatedly multiplies it by consecutive integers until it exceeds a threshold value.
- Prints the final number after repeated multiplication and the integer that caused it to exceed the threshold number.
- Default variables: threshold=100, product=1, currentNumber=1

<u>nested-dictionary.py:</u>
- Creates a nested dictionary from a string where each word becomes a key and the value is a dictionary containing the length of the word and if it is even or odd.
- Default variable: string="data science"

<u>safe-function-application.py:</u>
- Applies an exponentiation function ($x^y$) to a list containing pairs of integers $[x, y]$ while skipping the pairs with negative exponents.
- Stores the powers as a list and then prints it out.
- Default variable: pairs=[[5, 2], [3, -1], [4, 3], [2, 0]]

<u>sorted-search.py:</u>
- Generates a list of random values with length 20 and another random number $x$, both from the interval $[0, 1)$. It then sorts the list and calculates all the indices where $x$ is less than the indexed list value. 
- Prints the sorted list, $x$, and the smallest index found if it exists.

<u>circle-area-comparison.py:</u>
- Operates a function on the radii of two circles, given as two positive integers, and then calculates the ratio of the smaller circle's area to the larger circle's area.
- Validates the arguments and then prints the result as a percentage of the maximum of the larger circle's area that can be covered by the smaller circle's area.
- Default variables: radiusOfCircle1=50, radiusOfCircle2=100

<u>distribution-analysis:</u>
- Maps a list of number to a dictionary where the keys are the unique numbers, and their values are the percentage of numbers that are less than or equal to the key in the list.
- Sorts the dictionary and then prints it to console.
- Default variable: numbers=[3, 1, 2, 3, 4, 2]

<u>time-conversion.py</u>
- Takes the given number of seconds since midnight and converts it to time as the appropriate number of hours, minutes, seconds and AM/PM.
- Prints the time in the format "{hours} {minutes} {seconds} AM/PM".
- Default variable: seconds=19067

<u>pandas-dataframe.py:</u>
- Converts a dictionary with list values to a pandas DataFrame, and then inserts another column operated on the values in the rows.
- Prints the updated DataFrame.
- Default variable: data = {"A": [1, 2, 2, 1], "B": [3.1, 4.2, 1.5, 6.3], "C": [800, 150, 400, 210]}
