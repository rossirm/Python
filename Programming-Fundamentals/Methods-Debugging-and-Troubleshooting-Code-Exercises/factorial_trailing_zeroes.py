number = int(input())
factorial = 1
for i in range(2, number + 1):
    factorial *= i
zeroes = 0
while True:
    if factorial % 10 == 0:
        zeroes += 1
    else:
        break
    factorial //= 10
print(zeroes)
