# variables
seconds = 19067

# takes seconds as an input and returns a string with hours, minutes, seconds and am/pm
def convertSecondsToTime(seconds: int) -> str:
    # validate that input is a positive integer
    if not isinstance(seconds, int):
        raise TypeError("Seconds must be an integer.")
    if seconds < 0:
        raise ValueError("Seconds must be positive.")

    # calculate am/pm by calculating 12-hour cycles with modulo
    if (seconds // 43200) % 2 == 0:
        meridiem = "AM"
    else:
        meridiem = "PM"

    # calculate hours, minutes, and seconds through calculating quotient and remainder
    hours, seconds = divmod(seconds, 3600)
    minutes, seconds = divmod(seconds, 60)

    # formate and return string
    time = f"{hours} {minutes} {seconds} {meridiem}"
    return time

# print result
print(f"{seconds} seconds since midnight converted to formatted time is:\n{convertSecondsToTime(seconds)}")