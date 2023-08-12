def print_string(input_string):
    print("Input String:", input_string)

    print("\nCharacters:")
    for char in input_string:
        print(char, end=' ')
    print()

    print("\nHexa:")
    for char in input_string:
        print(hex(ord(char)), end=' ')
    print()

    print("\nDecimal:")
    for char in input_string:
        print(ord(char), end=' ')
    print()

input_string = input("Enter a string: ")
print_string(input_string)
