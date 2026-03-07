# Corrected Python Program

numbers = [10, 20, 30, 40]

total = 0

# Fix IndexError
for i in range(len(numbers)):
    total += numbers[i]

print("Total:", total)

# Fix ZeroDivisionError
x = 50
y = 1  # changed from 0 to 1
result = x / y
print("Division:", result)

# Fix NameError (count not defined)
count = len(numbers)  # define count
average = total / count
print("Average:", average)

# Fix TypeError (len on None)
data = []  # changed from None to empty list
print("Length:", len(data))

# Fix SyntaxError (missing colon)
if total > 50:
    print("Large total")

# Fix Logical error
radius = 5
area = 3.14 * radius ** 2  # correct formula for area of circle
print("Area:", area)

# Fix Blocking input (automation issue)
name = "Test User"  # replaced input() with default value
username = name  # define username
print("Hello", username)