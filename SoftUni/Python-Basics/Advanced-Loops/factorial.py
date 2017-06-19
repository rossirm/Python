# Напишете програма, която въвежда цяло число n (1 ≤ n ≤ 12) и изчислява и отпечатва n! = 1 * 2 * … * n (n факториел)

count = int(input())
factorial = 1

for i in range(1, count + 1):
    factorial *= i

print(factorial)
