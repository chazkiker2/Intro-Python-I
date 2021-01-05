"""
List comprehensions are one cool and unique feature of Python.
They essentially act as a terse and concise way of initializing
and populating a list given some expression that specifies how
the list should be populated. 

Take a look at https://docs.python.org/3/tutorial/datastructures.html#list-comprehensions
for more info regarding list comprehensions.
"""

# Write a list comprehension to produce the array [1, 2, 3, 4, 5]

# y = [i+1 for i in range(0, 5)]
y = [i for i in range(1, 6)]
print(f"line 15 — y: {y}")

x = []
for i in range(1, 6):
    x.append(i)

print(f"line 21 — x: {x}")

x.extend(i for i in range(1, 6))
print(f"line 24 — x: {x}")

# Write a list comprehension to produce the cubes of the numbers 0-9:
# [0, 1, 8, 27, 64, 125, 216, 343, 512, 729]
y = [i**3 for i in range(0, 10)]
print(f"line 29 — y: {y}")

# Write a list comprehension to produce the uppercase version of all the
# elements in array a. Hint: "foo".upper() is "FOO".

words_arr = ["foo", "bar", "baz"]
# b = ["ava", "doc"]
y = [word.upper() for word in words_arr]

print(f"line 38 — y: {y}")

# Use a list comprehension to create a list containing only the _even_ elements
# the user entered into list x.

input_arr = input("Enter comma-separated numbers: ").split(',')

print(f"input_arr: {input_arr}")
# What do you need between the square brackets to make it work?
even_numbers = [num for num in input_arr if int(num) % 2 == 0]
print(f"even_numbers: {even_numbers}")

numbers_arr = []
for num in input_arr:
    if int(num) % 2 == 0:
        numbers_arr.append(num)

print(f"numbers_arr: {numbers_arr}")
