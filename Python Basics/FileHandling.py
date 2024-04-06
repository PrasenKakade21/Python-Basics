# Writing to a file
with open("example.txt", "w") as f:
    f.write("Hello, world!\n")
    f.write("This is a test file.\n")
    f.write("Python file handling example.\n")

# Reading from a file
with open("example.txt", "r") as f:
    content = f.read()
    print("File content:\n", content)

# Appending to a file
with open("example.txt", "a") as f:
    f.write("Appending new line to the file.\n")

# Reading lines from a file
with open("example.txt", "r") as f:
    lines = f.readlines()
    print("Lines from file:")
    for line in lines:
        print(line.strip())  # strip() to remove newline character

# Reading file line by line
with open("example.txt", "r") as f:
    print("Reading file line by line:")
    for line in f:
        print(line.strip())

# Reading and writing binary files
with open("example.bin", "wb") as f:
    f.write(b"Binary data example")

with open("example.bin", "rb") as f:
    binary_data = f.read()
    print("Binary data:", binary_data)
