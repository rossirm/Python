__author__ = 'Боян'

n1 = input("First number")
a = int(n1)
n2 = input("Second number")
b = int(n2)
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