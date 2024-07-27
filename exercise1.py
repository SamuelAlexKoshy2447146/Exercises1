from random import choices
from pprint import pprint
from math import sqrt


"""1. Declare a python datatype list and do the following:
(a) Write a Python program to sum all the items of the list.
(b) Write a Python program to multiply all the items.
(c) Write a Python program to get the largest number from a list.
(d) Write a Python program to get the smallest number from a list."""

print("\nQuestion 1:\n")
list_numbers = choices(range(-100, 101), k=15)  # * Create a random list of 15 int

print("List of numbers:", list_numbers)

# * Sum
print("Sum of the list:", sum(list_numbers))

# * Product
product = 1
for item in list_numbers:
    product *= item
print("Product of items in list:", product)

# * Largest
max_value = max(list_numbers)
print("Largest value in the list:", max_value)

# * Smallest
min_value = min(list_numbers)
print("Smallest number in the list:", min_value)


"""2. Let A=['abc', 'xyz', 'aba', '1221'] be a given string, and write a Python
program that prints the string or strings and their index from the given list,
ensuring that the first and last characters of the strings to be printed are
identical."""

print("\n\nQuestion 2:\n")

A = ["abc", "xyz", "aba", "1221"]
print("Given list:", A)

print("\nStrings that have identical first and last characters: ")
# * Loop through items
for pos, item in enumerate(A):
    if item[0] == item[-1]:  # * Check first and last character
        print(f"Position: {pos} - String: {item}")


"""3. Write a python program to print an alphabetic pyramid and 
star pyramid"""

print("\n\nQuestion 3:\n")
# * Alphabet pattern
pattern = "ABCDE"
space = len(pattern) - 1
for i in range(len(pattern)):
    print(" " * space, end="")
    for j in range(i + 1):
        print(pattern[j], end=" ")
    space -= 1
    print()

# * Star pattern
length = 5
for i in range(length):
    for j in range(i + 1):
        print("*", end="")
    print()


"""4. Write a Python program to convert the given list to a list of dictionaries.
ListColour = ["Black", "Red", "Maroon", "Yellow"], 
["000000", "FF0000","800000", "FFFF00"]
Expected Output: 
[
    {'colorName': 'Black', 'colorCode': '000000'}, 
    {'color-Name': 'Red', 'colorCode': 'FF0000'}, 
    {'colorName': 'Maroon', 'colorCode':'800000'}, 
    {'colorName': 'Yellow', 'colorCode': 'FFFF00'}
]"""

print("\n\nQuestion 4:\n")
colour_name = ["Black", "Red", "Maroon", "Yellow"]
colour_code = ["000000", "FF0000", "800000", "FFFF00"]
colour_dict: list[dict] = list()
for name, code in zip(colour_name, colour_code):
    colour_dict.append({"colorName": name, "colorCode": code})

pprint(colour_dict)


"""5. Write a Python program to print all the even numbers and their squares
within the given range.
(a) range(1,50)
(b) range(1,100)
"""

print("\n\nQuestion 5:\n")
print("Part a:")
for i in range(2, 51, 2):
    print(f"{i}, {i * i}", end="; ")
print("\nPart b:")
for i in range(2, 101, 2):
    print(f"{i}, {i * i}", end="; ")

"""6. Write a Python program to read a four-digit number and find its
(a) Sum of digits
(b) Reverse"""

print("\n\nQuestion 6:\n")
inp = input("Enter a 4-digit number: ")
try:
    num = int(inp)
except ValueError:
    print("Inputed value was not an integer")
else:
    if len(str(num)) != 4:
        print("Inputed number does not have 4 digits")
    else:
        if num < 0:
            num *= -1
        num_copy = num
        sum_digits = 0
        while num > 0:
            sum_digits += num % 10
            num //= 10
        print(f"Sum of digits: {sum_digits}")
        print(f"Reverse of digits: {str(num_copy)[::-1]}")


"""7. Write a program to find the area of a triangle. Then find the area of two
arbitrary triangles by entering the three sides both using the input function
(input()). Print the total area enclosed by both triangles and each triangle's
contribution (%) towards it.
"""

print("\n\nQuestion 7:\n")


def area_of_triangle(a: float | int, b: float | int, c: float | int):
    """Calculate the area of a triangle on being given 3 sides

    Args:
        a (float | int): The first side
        b (float | int): The second side
        c (float | int): The third side

    Raises:
        ValueError: If any one side is negative

    Returns:
        float : The area of the triangle
    """

    if a <= 0 or b <= 0 or c <= 0:
        raise ValueError("Sides cannot be negative")
    s = (a + b + c) / 2
    area = sqrt(s * (s - a) * (s - b) * (s - c))
    return area


areas: list[float] = list()
side: list[float] = list()
for i in range(1, 3):
    print(f"For triangle {i}:")
    for j in "abc":
        side.append(float(input(f"Enter side {j}: ")))
    areas.append(area_of_triangle(*side[-3:]))
total_area = sum(areas)
print(f"\nTotal area: {total_area}")
for i in range(2):
    print(f"Contribution of triangle {i+1}: {areas[i]/total_area*100.0:.3f}%")


"""8. Given a dictionary containing the following information about 10 different
people:
people = [
    {"name": "John Doe", "age": 30, "blood_group": "A+"},
    {"name": "Jane Smith", "age": 25, "blood_group": "B-"},
    {"name": "Emily Davis", "age": 40, "blood_group": "O+"},
    {"name": "Michael Brown", "age": 35, "blood_group": "AB-"},
    {"name": "William Johnson", "age": 28, "blood_group": "A-"},
    {"name": "Emma Wilson", "age": 22, "blood_group": "B+"},
    {"name": "Oliver Martinez", "age": 33, "blood_group": "O-"},
    {"name": "Sophia Anderson", "age": 27, "blood_group": "AB+"},
    {"name": "James Thomas", "age": 45, "blood_group": "A+"},
    {"name": "Isabella Lee", "age": 38, "blood_group": "B-"},
]
Write a Python program that prints each person's name, age, and blood
group in a formatted manner. Each person's information should be separated
by a line of dashes (-).
"""

print("\n\nQuestion 8:\n")

people = [
    {"name": "John Doe", "age": 30, "blood group": "A+"},
    {"name": "Jane Smith", "age": 25, "blood group": "B-"},
    {"name": "Emily Davis", "age": 40, "blood group": "O+"},
    {"name": "Michael Brown", "age": 35, "blood group": "AB-"},
    {"name": "William Johnson", "age": 28, "blood group": "A-"},
    {"name": "Emma Wilson", "age": 22, "blood group": "B+"},
    {"name": "Oliver Martinez", "age": 33, "blood group": "O-"},
    {"name": "Sophia Anderson", "age": 27, "blood group": "AB+"},
    {"name": "James Thomas", "age": 45, "blood group": "A+"},
    {"name": "Isabella Lee", "age": 38, "blood group": "B-"},
]

for person in people:
    for key, value in person.items():
        print(f"{key.title()}: {value}")
    print("-" * 20)


"""9. Write a Python program to extract the rear elements from a tuple string as
depicted"""

print("\n\nQuestion 9:\n")

new_string_list = list()
string_tuple = ("python", "learn", "includehelp")
for item in string_tuple:
    new_string_list.append(item[-1])
print("Original tuple:", string_tuple)
print("Output:", new_string_list)


"""10. Declare a list/tuple containing all the twelve months. Write a Python program
that converts a month name entered via the Python console to the number
of days in that month (Consider leap year as well the code):"""

print("\n\nQuestion 10:\n")

months_name = (
    "January",
    "February",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
    "October",
    "Novemeber",
    "December",
)
day_count = (
    31,
    28,
    31,
    30,
    31,
    30,
    31,
    31,
    30,
    31,
    30,
    31,
)

month_name = input("Enter the month name: ")
if month_name.title() in months_name:
    index = months_name.index(month_name.title())
    days = day_count[index]
    if index == 1:
        year = int(input("Enter the year: "))
        if year % 4 == 0 and (year % 100 != 0 or year % 400 == 0):
            days += 1
    print(f"The number of days in {month_name} is: {days}")
else:
    print("Invalid name for a month")

# * Dictionary implementation

print("\n\nQuestion 10:\n")

months_name = {
    "January": 31,
    "February": 28,
    "March": 31,
    "April": 30,
    "May": 31,
    "June": 30,
    "July": 31,
    "August": 31,
    "September": 30,
    "October": 31,
    "Novemeber": 30,
    "December": 31,
}

month_name = input("Enter the month name: ").title()
if month_name in months_name:
    days = months_name[month_name]
else:
    if len(month_name) < 3:
        print("Invalid name for a month")
    else:
        for month in months_name:
            if month_name in month:
                days = months_name[month]
                month_name = month
                break
        else:
            print("Invalid name for a month")
            days = -1
if days >= 0:
    if days == 28:
        year = int(input("Enter the year: "))
        if year % 4 == 0 and (year % 100 != 0 or year % 400 == 0):
            days += 1
    print(f"The number of days in {month_name} is: {days}")
