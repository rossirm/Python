__author__ = 'Боян'

num1 = input("Enter the first number")
n = int(num1)
num2 = input("Enter the second number")
m = int(num2)

last_n = n % 10
last_m = m % 10

if last_n > last_m:
    print(last_n)
elif last_n < last_m:
    print(last_m)
else:
    print(max(n, m))