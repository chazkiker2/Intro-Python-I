square_dict = {}
for num in range(1, 11):
    square_dict[num] = num * num

print(square_dict)

square_comp = {num: num * num for num in range(1, 11)}
print(square_comp)

dict_to_flip = {"a": 10, "b": 20, "c": 30}

# inverse_dict = {10: "a", 20: "b", 30: "c"}
inverse_dict = {v: k for v, k in dict_to_flip.items()}
print(inverse_dict)  # -> { 10: "a", 20: "b", 30: "c" }

# make a dictionary with key: value pairs such that
# each key is a number and each value is the cube of that key
cubed_dict = {i: i ** 3 for i in range(10)}
print(cubed_dict)  # -> {0: 0, 1: 1, 2: 8, 3: 27, 4:

nested_list = [[1, 2, 3], ["first", "second", "third"]]
joined_dict = {i: j for i, j in zip(nested_list[0], nested_list[1])}
print(joined_dict)

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
even_squared_nums = {i: i ** 2 for i in numbers if i % 2 == 0}
print(even_squared_nums)

strings = ["land", "sea", "sky"]
enumerated_dict = {i: j for i, j in enumerate(strings, 1)}
print(enumerated_dict)
