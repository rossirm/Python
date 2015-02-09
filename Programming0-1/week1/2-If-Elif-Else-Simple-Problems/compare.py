__author__ = 'Боян'

a = input("First number")
a = int(a)
b = input("Second number")
b = int(b)

if a > b:
    print("a:{0} is bigger than b:{1}".format(a, b))
elif a < b:
    print("a:{0} is lesser than b:{1}".format(b, a))
else:
    print("a:{0} is equals b:{1}".format(a, b))