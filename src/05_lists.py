# For the exercise, look up the methods and functions that are available for use
# with Python lists.

x = [1, 2, 3]
y = [8, 9, 10]

# For the following, DO NOT USE AN ASSIGNMENT (=).

# Change x so that it is [1, 2, 3, 4]
# YOUR CODE HERE
x.append(4)
print(x)

# Using y, change x so that it is [1, 2, 3, 4, 8, 9, 10]
# YOUR CODE HERE
x.extend(y)
print(x)
# x += y
# print(x)
# print(x + y)

# Change x so that it is [1, 2, 3, 4, 9, 10]
# YOUR CODE HERE
# x.remove(8)
# print(x)
# x.pop(-3)
# x.pop(index) — remove el at index
print(f"***index of el=8 in x[] — {x.index(8)}")
# x.index(elToFind) = location of el
x.pop(x.index(8))
print(x)
# print(x[-3])

# Change x so that it is [1, 2, 3, 4, 9, 99, 10]
# YOUR CODE HERE
# x.insert(location, element)
x.insert(-1, 99)
print(x)

# Print the length of list x
# YOUR CODE HERE
print(len(x))

# Print all the values in x multiplied by 1000
# YOUR CODE HERE
for num in x:
    print(num * 1000)

print(x)

for i in range(0, len(x)):
    print(x[i])
