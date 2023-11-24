def decimalToBinary(value):
    if value == 0:
        return '0'
    elif value == 1:
        return '1'
    else:
        # Recursive call to convert the quotient to binary + remainder as the last digit
        return decimalToBinary(value // 2) + str(value % 2)


def main():
    while True:
        decimal_number = int(input("Enter a decimal number: "))

        # Ensure the input is non-negative
        if decimal_number < 0:
            print("Please enter a non-negative decimal number.")
        else:
            binary_number = decimalToBinary(decimal_number)
            print(
                f"The binary equivalent of {decimal_number} is: {binary_number}")

        play_again = input("Do you want to convert more? (y/n): ").lower()
        if play_again == 'n':
            print("Thank you. Good Bye!")
            break


# Run the test program
if __name__ == "__main__":
    main()
