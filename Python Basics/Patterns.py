def print_half_pyramid(rows):
    for i in range(1, rows + 1):
        print("* " * i)

def print_full_pyramid(rows):
    for i in range(1, rows + 1):
        print(" " * (rows - i) + "* " * i)

def print_hollow_pyramid(rows):
    for i in range(1, rows + 1):
        if i == 1 or i == rows:
            print(" " * (rows - i) + "* " * i)
        else:
            print(" " * (rows - i) + "* " + " " * ((i - 1) * 2 - 1) + "* ")

def print_fibonacci(rows):
    a, b = 0, 1
    for _ in range(rows):
        print(a, end=" ")
        a, b = b, a + b

def print_pascals_triangle(rows):
    for i in range(rows):
        coef = 1
        for j in range(1, rows-i+1):
            print(" ", end="")
        for j in range(0, i+1):
            if j == 0 or i == 0:
                coef = 1
            else:
                coef = coef * (i - j + 1) // j
            print(coef, end=" ")
        print()

def print_alphabet_pyramid(rows):
    for i in range(rows):
        for j in range(0, i + 1):
            print(chr(65 + j), end=" ")
        print()

def print_alphabet_diamond(rows):
    for i in range(rows):
        print(" " * (rows - i - 1) + " ".join(chr(65 + j) for j in range(i + 1)))
    for i in range(rows - 2, -1, -1):
        print(" " * (rows - i - 1) + " ".join(chr(65 + j) for j in range(i + 1)))

def print_menu():
    print("Pattern Menu:")
    print("1. Half Pyramid of Stars")
    print("2. Full Pyramid of Stars")
    print("3. Hollow Pyramid of Stars")
    print("4. Fibonacci Sequence")
    print("5. Pascal's Triangle")
    print("6. Alphabet Pyramid")
    print("7. Alphabet Diamond")
    print("8. Exit")

def main():
    while True:
        print_menu()
        choice = input("Enter your choice: ")

        if choice == '8':
            print("Exiting...")
            break

        if choice in ['1', '2', '3', '6', '7']:
            rows = int(input("Enter number of rows: "))

        if choice == '1':
            print("Half Pyramid of Stars:")
            print_half_pyramid(rows)
        elif choice == '2':
            print("Full Pyramid of Stars:")
            print_full_pyramid(rows)
        elif choice == '3':
            print("Hollow Pyramid of Stars:")
            print_hollow_pyramid(rows)
        elif choice == '4':
            print("Fibonacci Sequence:")
            print_fibonacci(rows)
        elif choice == '5':
            print("Pascal's Triangle:")
            print_pascals_triangle(rows)
        elif choice == '6':
            print("Alphabet Pyramid:")
            print_alphabet_pyramid(rows)
        elif choice == '7':
            print("Alphabet Diamond:")
            print_alphabet_diamond(rows)
        else:
            print("Invalid choice. Please enter a number from 1 to 8.")

        print()

if __name__ == "__main__":
    main()
