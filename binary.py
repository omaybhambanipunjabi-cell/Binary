
while True:
    try:
        decimal_number_str = input("Enter an integer decimal number: ")
        decimal_number = int(decimal_number_str)
        break  
    except ValueError:
        print("Invalid input")


binary = bin(decimal_number)
result = binary[2:]

print(f"The binary  of {decimal_number} is: {result}")