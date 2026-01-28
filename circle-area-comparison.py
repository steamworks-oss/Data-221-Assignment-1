from math import pi

def circleAreaCoverage(radiusOfCircle1: int, radiusOfCircle2: int) -> float:
    # validate that both radii are positive integers
    if not isinstance(radiusOfCircle1, int) or not isinstance(radiusOfCircle2, int):
        raise TypeError("The radii of the circle areas are not both positive integers.")
    if radiusOfCircle1 <= 0 or radiusOfCircle2 <= 0:
        raise ValueError("The radii of the circle areas are not both positive integers.")

    # calculate the area of each circle using their radius
    areaOfCircle1 = pi * radiusOfCircle1 * radiusOfCircle1
    areaOfCircle2 = pi * radiusOfCircle2 * radiusOfCircle2

    # return the ratio of the smaller circles area to the larger circles area as a percentage
    if areaOfCircle1 >= areaOfCircle2:
        return (areaOfCircle2 / areaOfCircle1) * 100
    else:
        return (areaOfCircle1 / areaOfCircle2) * 100

# calculate the comparison of two circles using their radii to get a percentage and then printing it
percentage = circleAreaCoverage(50, 100)
print(f"The percentage of the larger circle's area that can be covered by the smaller circle is: {percentage}")