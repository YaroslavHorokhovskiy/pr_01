"""Task #1. Construct these numeric values:"""

# Integer zero
0

# Floating point zero
0.0

# Integer one hundred and one
101

# Floating point one thousand
1000.0

# Floating point one thousand using scientific notation
1e+3

# Create a positive integer, a negative integer, and zero.
# Assign them to variables
a = 42
b = 77
c = 0

# Write several arithmetic expressions. Bind the values to variables.
# Use a variety of operators, e.g. +, -, /, *, etc. Use parentheses
# to control operator scope.
x = (2 * 3 + 16) // 2
y = (2 ** 4 - 101 % 2) * 43
z = x / y

# Create several floats and assign them to variables.
x = 166.667
y = -9.81
z = 2.99792458e+8

# Write several arithmetic expressions containing your float variables.
(x + y + z) ** 2
(x ** 2 + y ** 2 + z **2) / (x * y)
(x - y) ** 0.5 / z

# Write several expressions using mixed arithmetic (integers and floats).
(2 * 3.14 + 9.81 / 16) / 14
1.5 ** 4 + 15 // 5 - 8 % 3
(199.0 - 1 / 85 + 3.67e-12) ** 0.33


# Obtain a float as a result of division of one integer by another;
# do so by explicitly converting one integer to a float.
float(550) / 10

"""Task #2 Type Conversation"""

# Construct an integer from the string '123'
str('123')

# Construct a float from the integer 123
float(123)

# Construct an integer from the float 12.345
int(12.345)

"""Task #3: Digits of a Number"""

# Write a Python-script that detects the last 4 digits of a credit card.
CARD_NUMBER = 9384349532974526
LAST_4_DIGITS = CARD_NUMBER % 10000

# Find the sum of the digits of a three-digit number
NUMBER = 123
SUM = NUMBER % 10 + (NUMBER // 10) % 10 + (NUMBER // 100) % 10
