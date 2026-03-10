def add_numbers(a, b):
    result = a + b
    print("The sum is: " + str(result))
    return result

x = 10
y = 5

total = add_numbers(x, y)

if total > 10:
    print("Greater than 10")
else:
    print("Less than or equal to 10")