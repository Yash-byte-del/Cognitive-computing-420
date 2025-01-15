#11.1
import math
def calculate_square_root(number):
    return math.sqrt(number)
number=float(input("Enter a number:"))
square_root=calculate_square_root(number)
print(f"The square root of {number} is {square_root}")

#11.2
import datetime
current_datetime = datetime.datetime.now()
print(f"The current date and time is: {current_datetime}")

#11.3
import os
print(os.listdir())