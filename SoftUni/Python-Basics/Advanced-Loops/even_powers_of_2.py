# Да се напише програма, която въвежда n и печата четните степени на 2 ≤ 2n: 20, 22, 24, 28, …, 2n.

count = int(input())

for number in range(0, count + 1, 2):
    print(2 ** number)
