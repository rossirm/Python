__author__ = 'Боян'

num = input("Enter a number: ")
n = int(num)
dot = "."
asterisk = "*"
clock = ""
# upper part
for x in range(0, n // 2 + 1):
    dots = x
    asterisks = n - 2 * dots
    clock += dot * dots + asterisk * asterisks + dot * dots + "\n"
# lower part
for x in range(n // 2 - 1, -1, -1):
    dots = x
    asterisks = n - 2 * dots
    clock += dot * dots + asterisk * asterisks + dot * dots + "\n"

print(clock)