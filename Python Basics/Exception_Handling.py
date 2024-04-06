# Example 1: Handling specific exceptions
try:
    x = 10 / 0
except ZeroDivisionError:
    print("Error: Division by zero")

# Example 2: Handling multiple exceptions
try:
    x = int("abc")
except ValueError:
    print("Error: Unable to convert to integer")
except ZeroDivisionError:
    print("Error: Division by zero")

# Example 3: Using else block
try:
    x = 10 / 2
except ZeroDivisionError:
    print("Error: Division by zero")
else:
    print("Result:", x)

# Example 4: Using finally block
try:
    x = 10 / 0
except ZeroDivisionError:
    print("Error: Division by zero")
finally:
    print("This block is always executed")

# Example 5: Raising exceptions
def divide(x, y):
    if y == 0:
        raise ValueError("Denominator cannot be zero")
    return x / y

try:
    result = divide(10, 0)
except ValueError as e:
    print("Error:", e)
