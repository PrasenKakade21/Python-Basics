# Function definition
def greet():
    print("Hello, world!")

# Function call
greet()  # Output: Hello, world!

# Function with parameters
def add(x, y):
    return x + y

result = add(3, 5)
print("Result of addition:", result)  # Output: Result of addition: 8

# Default parameter values
def greet(name="John"):
    print("Hello,", name)

greet()          # Output: Hello, John
greet("Alice")   # Output: Hello, Alice

# Keyword arguments
def person_info(name, age):
    print("Name:", name)
    print("Age:", age)

person_info(age=30, name="Alice")

# Arbitrary number of arguments
def add(*args):
    total = 0
    for num in args:
        total += num
    return total

print("Sum:", add(1, 2, 3, 4, 5))  # Output: Sum: 15

# Keyword-only arguments
def greet(*, name):
    print("Hello,", name)

# greet("Alice")  # This would raise an error
greet(name="Alice")  # Output: Hello, Alice

# Return multiple values
def square_cube(x):
    return x ** 2, x ** 3

square, cube = square_cube(3)
print("Square:", square)  # Output: Square: 9
print("Cube:", cube)      # Output: Cube: 27

# Lambda functions
square = lambda x: x ** 2
print("Square of 5:", square(5))  # Output: Square of 5: 25

# Recursive function
def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)

print("Factorial of 5:", factorial(5))  # Output: Factorial of 5: 120
