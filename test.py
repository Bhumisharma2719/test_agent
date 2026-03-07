import math

def calculate_average(numbers):
    total = 0
    for num in numbers:
        total += num
    avg = total / len(numbers)
    return avg


def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)


def divide_numbers(a, b):
    result = a / b
    print("Result is: " + str(result))


numbers = [10, 20, 30, 40]

avg = calculate_average(numbers)
print("Average:", avg)

print("Factorial:", factorial(5))

x = 10
y = 2

divide_numbers(x, y)

print("Square root:", math.sqrt(25))