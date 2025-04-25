# Form a function to check if a year is a leap year,

"""
Conditions for a leap year:
    A leap year is divisible by 4 and 400 but if divisible by 100 as well, it is not a leap year considering the .2425 constant within the solar system orbiting.

    1. The year can be evenly divided by 4, its a leap year unless:
    2. The uear can be evenly divided by 100, its not a leap year unless:
    3. The year is also evenly divided by 400, its a leap year
"""

def leapYear(year: int) -> bool:
    return True if year % 4 == 0 and year % 100 == 0 and year % 400 == 0 else True if year % 4 == 0 and year % 100 != 0 else False

print(leapYear(1904))