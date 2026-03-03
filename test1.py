# Advanced Buggy Program

numbers = [5, 10, 15]

total = 0

for i in range(5):  # ❌ IndexError (range too large)
    total += numbers[i]

print("Total:", total)

x = "20"
y = 0

result = int(x) / y  # ❌ ZeroDivisionError
print("Division:", result)

if total > 20
    print("Big total")  # ❌ SyntaxError (missing colon)

print("Average:", total / count)  # ❌ NameError (count not defined)

name = input("Enter name: ")  # ❌ Will block execution

print("Hello " + namee)  # ❌ NameError (typo)
