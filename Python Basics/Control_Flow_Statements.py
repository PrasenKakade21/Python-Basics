# If statement
x = 10
if x > 0:
    print("x is positive")
elif x == 0:
    print("x is zero")
else:
    print("x is negative")

# For loop
print("For loop:")
for i in range(5):
    print(i, end=" ")  # Output: 0 1 2 3 4
print()  # New line

# While loop
print("While loop:")
count = 0
while count < 5:
    print(count, end=" ")  # Output: 0 1 2 3 4
    count += 1
print()  # New line

# Break statement
print("Break statement:")
for char in "Python":
    if char == "h":
        break
    print(char, end=" ")  # Output: P y t

# Continue statement
print("\nContinue statement:")
for char in "Python":
    if char == "h":
        continue
    print(char, end=" ")  # Output: P y t o n

# Pass statement
print("\nPass statement:")
for i in range(3):
    pass  # Placeholder for future code
print("Loop completed")

# Nested loops
print("Nested loops:")
for i in range(3):
    for j in range(2):
        print(i, j)  # Output: (0, 0), (0, 1), (1, 0), (1, 1), (2, 0), (2, 1)
