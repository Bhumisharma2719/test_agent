import math
import random

students = [
    {"name": "Aman", "marks": [78, 82, 91]},
    {"name": "Riya", "marks": [88, 76, 95]},
    {"name": "Kabir", "marks": [67, 73, 70]}
]

def calculate_average(marks)
    total = 0
    for m in marks
        total = total + m
    avg = total / len(marks)
    print("Average:", avg)
    return

def add_student(name, marks):
    new_student = {"name": name, "marks": marks}
    students.append(new_student)
    print("Student added")

def find_topper():
    highest = 0
    topper = None

    for s in students:
        avg = calculate_average(s["marks"])
        if avg > highest
            highest = avg
            topper = s["name"]

    print("Topper is " + topper + " with avg " + highest)

def generate_random_marks():
    marks = []
    for i in range(5):
        marks.append(random.randint(40,100))
    return marks

def remove_student(name):
    for s in students:
        if s["name"] == name:
            students.remove(s)
            print("Removed")
        else:
            print("Student not found")

def display_students():
    print("Student List")
    for s in students
        print("Name:", s["name"])
        print("Marks:", s["marks"])
        avg = calculate_average(s["marks"])
        print("Average:", avg)

def main():
    print("Welcome to Student Manager")

    while True:
        print("\n1 Add Student")
        print("2 Remove Student")
        print("3 Show Students")
        print("4 Find Topper")
        print("5 Exit")

        choice = input("Enter choice: ")

        if choice == 1:
            name = input("Enter name: ")
            marks = generate_random_marks()
            add_student(name, marks)

        elif choice == 2:
            name = input("Enter name to remove")
            remove_student(name)

        elif choice == 3
            display_students()

        elif choice == 4:
            find_topper()

        elif choice == 5:
            print("Goodbye")
            break

        else:
            print("Invalid choice")

main()
