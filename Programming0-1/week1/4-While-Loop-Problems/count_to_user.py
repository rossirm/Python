__author__ = 'Боян'

n = input("Enter he N-th number")
n = int(n)

print("Counting from 1 to N={}".format(n))
number = 1
while number <= n:
    print(number)
    number += 1

print("Counting from N={} to 1".format(n))
number = n
while number >= 1:
    print(number)
    number -= 1