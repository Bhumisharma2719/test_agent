# Complex Buggy Program

numbers = [2, 4, 6, 8]

total = 0

for i in range(6):   # ❌ IndexError
    total += numbers[i]

print("Total:", total)

x = "10"
y = 0

result = int(x) / y   # ❌ ZeroDivisionError
print("Division:", result)

if total > 10         # ❌ SyntaxError (missing colon)
    print("Big total")

average = total / count   # ❌ NameError (count not defined)
print("Average:", average)

name = input("Enter name: ")   # ❌ Blocking input
print("Hello " + username)     # ❌ NameError (username not defined)

data = None
print(len(data))   # ❌ TypeError
