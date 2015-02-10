__author__ = 'Боян'

n = input("Enter the first number")
n = int(n)
m = input("Enter the second number")
m = int(m)

last_n = n % 10
last_m = m % 10

if last_n > last_m:
    print(last_n)
elif last_m > last_n:
    print(last_m)
else:
    print(max(n, m))