__author__ = 'Боян'


# Square
def square(n):
    return int(n * n)


# Factorial
def factorial(n):
    f = 1
    s = 1
    while s <= n:
        f *= s
        s += 1
    return f


# Count list elements
def count_elements(items):
    count = 0
    for item in items:
        count += 1

    return count


# Find matching element in list
def member(x, xs):
    is_found = False

    for index in range(len(xs)):
        if index == x:
            is_found = True
            break
    return is_found


# Student with grades above a certain limit
def grades_that_pass(students, grades, limit):
    passed = []

    for index in range(len(students)):
        student = students[index]

        if grades[index] >= limit:
            passed += [student]

    return passed


# sq = int(input("Enter a number, that will be squared:"))
# print(square(sq))

# fact = int(input("Enter a number, which factorial will be returned:"))
# print(factorial(fact))

# l = []
# print("The list, which elements will be counted: is: " + str(l))
# print(count_elements(l))
# l = [1, 2, 3]
# print("The list, which elements will be counted: is: " + str(l))
# print(count_elements(l))

# print("The  element, that You will search for is: " + str(1))
# print("The list, where You will search for that element is: " + str([1, 2, 3]))
# print(member(1, [1, 2, 3]))
# print("The  element, that You will search for is: " + "Python")
# print("The list, where You will search for that element is: " + str(["Django", "Rails"]))
# print(member("Python", ["Django", "Rails"]))

# students = ["Rado", "Ivo", "Maria", "Nina"]
# grades = [3, 4.5, 5.5, 6]
# l = 4.0
# print("The list of the students: " + str(students))
# print("The list of the grades: " + str(grades))
# print("The limit: " + str(l))
# print(str(grades_that_pass(students, grades, l)))
