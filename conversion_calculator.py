def display_menu():
    """Display the conversion menu."""
    print("Binary Conversion Calculator")
    print("1. Decimal to Binary")
    print("2. Binary to Decimal")
    print("3. Hexadecimal to Decimal")
    print("4. Decimal to Hexadecimal")
    print("5. Hexadecimal to Binary")
    print("6. Binary to Hexadecimal")
    print("7. Octal to Decimal")
    print("8. Decimal to Octal")
    print("9. Quit")

def decimal_to_binary(decimal):
    """Convert decimal to binary."""
    binary = ""
    while decimal > 0:
        binary = str(decimal % 2) + binary
        decimal //= 2
    return binary

def binary_to_decimal(binary):
    """Convert binary to decimal."""
    decimal = 0
    for digit in binary:
        if digit != '0' and digit != '1':
            return "Invalid selection"
        decimal = decimal * 2 + int(digit)
    return decimal

def main():
    """Main function to run the program."""
    print("Welcome to Binary Conversion Calculator!")
    while True:
        display_menu()
        choice = input("Enter your choice (1-9): ")

        if choice == '9':
            print("Exiting the program...")
            break

        if choice not in ['1', '2', '3', '4', '5', '6', '7', '8']:
            print("Invalid selection. Please enter a number between 1 and 9.")
            continue

        if choice == '1':
            decimal = int(input("Enter a decimal number: "))
            print(f"Decimal {decimal} is binary {decimal_to_binary(decimal)}")
        elif choice == '2':
            binary = input("Enter a binary number: ")
            print(f"Binary {binary} is decimal {binary_to_decimal(binary)}")
        # Add more conversion options here

if __name__ == "__main__":
    main()
