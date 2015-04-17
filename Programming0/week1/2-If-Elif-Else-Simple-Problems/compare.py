__author__ = 'Боян'

n1 = input("First number \'a\'")
a = int(n1)
n2 = input("Second number \'b\'")
b = int(n2)

if a > b:
    print("a={0} is bigger than b={1}".format(a, b))
elif a < b:
    print("a={0} is lesser than b={1}".format(b, a))
else:
    print("a={0} equals b={1}".format(a, b))