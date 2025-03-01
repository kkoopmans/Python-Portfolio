def decimal_to_binary(decimal):
    binary = ""
    while decimal > 0:
        binary = str(decimal % 2) + binary
        decimal = decimal // 2
    return binary

def binary_to_decimal(binary):
    decimal = 0
    power = 0
    for digit in binary[::-1]:
        decimal += int(digit) * (2 ** power)
        power += 1
    return decimal

print("Menu: \n 1. Convert Dec to Bin \n 2. Convert Bin to Dec")
choice = input("Which conversion would you like to do? (1 or 2) ")
print("")

if choice == '1':
    value = input("Enter a decimal number to convert: ")
    print(f'{value} in binary is {decimal_to_binary(int(value))}')
if choice == '2':
    value = input("Enter a binary number to convert: ")
    print(f'{value} in decimal is {binary_to_decimal(value)}')