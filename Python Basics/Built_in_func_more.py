# Mathematical Functions
# 1. abs()
abs_value = abs(-5)
print("Absolute value:", abs_value)

# 2. pow()
power = pow(2, 3)
print("Power:", power)

# 3. max()
maximum = max(5, 8, 3, 12)
print("Maximum value:", maximum)

# 4. min()
minimum = min(5, 8, 3, 12)
print("Minimum value:", minimum)

# 5. round()
rounded_value = round(3.14159, 2)
print("Rounded value:", rounded_value)


# String Functions
# 1. str.capitalize()
string = "hello world"
capitalized_string = string.capitalize()
print("Capitalized string:", capitalized_string)

# 2. str.upper()
upper_string = string.upper()
print("Uppercase string:", upper_string)

# 3. str.lower()
lower_string = string.lower()
print("Lowercase string:", lower_string)

# 4. str.strip()
string_with_whitespace = "  hello world  "
stripped_string = string_with_whitespace.strip()
print("Stripped string:", stripped_string)

# 5. str.split()
words = string.split()
print("Split string:", words)

# 6. str.join()
separator = ", "
joined_string = separator.join(words)
print("Joined string:", joined_string)


# List Functions
# 1. list.append()
my_list = [1, 2, 3]
my_list.append(4)
print("Appended list:", my_list)

# 2. list.extend()
another_list = [5, 6, 7]
my_list.extend(another_list)
print("Extended list:", my_list)

# 3. list.pop()
popped_element = my_list.pop()
print("Popped element:", popped_element)

# 4. list.sort()
my_list.sort()
print("Sorted list:", my_list)

# 5. list.reverse()
my_list.reverse()
print("Reversed list:", my_list)


# Dictionary Functions
# 1. dict.keys()
my_dict = {'a': 1, 'b': 2, 'c': 3}
keys = my_dict.keys()
print("Dictionary keys:", keys)

# 2. dict.values()
values = my_dict.values()
print("Dictionary values:", values)

# 3. dict.items()
items = my_dict.items()
print("Dictionary items:", items)


# File Functions
# Assuming 'example.txt' exists with some content
# 1. open()
file = open('example.txt', 'r')
print("File object:", file)

# 2. file.read()
file_content = file.read()
print("File content:")
print(file_content)

# 3. file.close()
file.close()
