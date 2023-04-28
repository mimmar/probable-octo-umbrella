### Exercise 1.5 | Triangle area
'''
Write a program that will ask a user for the lengths of the sides of a triangle.
Check if it's possible to create a triangle from those lengths and if so,
calculate the area of the triangle.

To calculate square root use:
```
import math

x = math.sqrt(10)
'''

import math

# Prompt the user for the lengths of the sides of the triangle
a = float(input("Enter the length of side a: "))
b = float(input("Enter the length of side b: "))
c = float(input("Enter the length of side c: "))

# Check if it is possible to create a triangle from these lengths using the triangle inequality theorem
if a + b > c and a + c > b and b + c > a:
    # Calculate the semi-perimeter of the triangle
    s = (a + b + c) / 2

    # Calculate the area of the triangle using Heron's formula
    area = math.sqrt(s * (s - a) * (s - b) * (s - c))

    print(f'The area of the triangle is: {area})
else:
    print("The lengths entered do not form a valid triangle.")
