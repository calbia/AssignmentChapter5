'''
Ross Young
10/8/2026
Program to convert a base-32 number to octal
'''


# Dictionary to convert base 32 to binary and binary to octal
# Each base-32 digit = 5 bits (2^5 = 32 possible values, 0-31)
# Each octal digit   = 3 bits (2^3 = 8 possible values, 0-7)
Base32ToBinary = {
    '0': '00000', '1': '00001', '2': '00010', '3': '00011',
    '4': '00100', '5': '00101', '6': '00110', '7': '00111',
    '8': '01000', '9': '01001',
    'A': '01010', 'B': '01011', 'C': '01100', 'D': '01101',
    'E': '01110', 'F': '01111',
    'G': '10000', 'H': '10001', 'I': '10010', 'J': '10011',
    'K': '10100', 'L': '10101', 'M': '10110', 'N': '10111',
    'O': '11000', 'P': '11001', 'Q': '11010', 'R': '11011',
    'S': '11100', 'T': '11101', 'U': '11110', 'V': '11111'
}
BinaryToOctal = {
    '000': '0', '001': '1', '010': '2', '011': '3',
    '100': '4', '101': '5', '110': '6', '111': '7'
}

# Read base-32 input from user, .upper to ensure consistency with dictionary keys
Base32Input = input("Enter a base-32 number (digits 0-9, A-V): ").upper()

# Convert base-32 digits to 5-bit binary representation
def ConvertBase32ToBinary(Base32Input, Base32ToBinary):
    Binary = ""
    Valid = True
    for digit in Base32Input:
        if digit not in Base32ToBinary:
            print(f"Invalid base-32 digit: {digit}")
            Valid = False
            break
        Binary = Binary + Base32ToBinary[digit]
    return Binary, Valid # Return binary and validity status

# Regroup the binary string into 3-bit groups and convert to octal
def ConvertBinaryToOctal(Binary, BinaryToOctal):
    while len(Binary) % 3 != 0: # Pad binary string to make its length a multiple of 3
        Binary = '0' + Binary
    Octal = ""
    for i in range(0, len(Binary), 3): # Each 3 bits of binary corresponds to one octal digit
        Octal += BinaryToOctal[Binary[i:i+3]]
    return Octal.lstrip('0') or '0'  # Remove leading zeros, return '0' if empty

Binary, Valid = ConvertBase32ToBinary(Base32Input, Base32ToBinary) # Convert base-32 to binary and check validity
if Valid:
    print("Octal output:", ConvertBinaryToOctal(Binary, BinaryToOctal)) # Convert binary to octal and print the result