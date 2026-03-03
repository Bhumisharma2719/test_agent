# Sample Buggy Program

numbers = [10, 20, 30, 40]

total = 0

for i in range(len(numbers)):
    total += numbers[i]

print("Total is:", total)

x = 10
y = 2

result = x / y
print("Division result:", result)

if total > 50:
    print("Large total")
else:
    print("Small total")

name = "Test User"

print("Hello " + name)