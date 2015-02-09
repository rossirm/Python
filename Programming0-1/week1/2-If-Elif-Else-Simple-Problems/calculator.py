__author__ = 'Боян'

a = input("First number")
a = int(a)
b = input("Second number")
b = int(b)
operator = input("Operator")

if operator == "+":
    result = a + b
    print("{0} {1} {2} = {3}".format(a, operator, b, result))
elif operator == "-":
    result = a - b
    print("{0} {1} {2} = {3}".format(a, operator, b, result))
elif operator == "*":
    result = a * b
    print("{0} {1} {2} = {3}".format(a, operator, b, result))
elif operator == "/":
    result = a / b
    print("{0} {1} {2} = {3}".format(a, operator, b, result))
else:
    print("{0} is invalid operator".format(operator))