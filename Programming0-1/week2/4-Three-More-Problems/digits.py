__author__ = 'Боян'

n_str = input("Enter a number")
num = int(n_str)

n_digits = []
while num > 1:
    n_digits = [int(num % 10)] + n_digits
    num /= 10
print(n_digits)
print(type(n_digits))
print(type(n_digits[0]))
new_num = 0
for d in n_digits:
    new_num = new_num * 10 + d
print(new_num)
print(type(new_num))