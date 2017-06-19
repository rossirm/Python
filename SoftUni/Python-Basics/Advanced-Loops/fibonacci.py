# Напишете програма, която въвежда цяло число n и пресмята n-тото число на Фибоначи.
# Нулевото число на Фибоначи е 1, първото е също 1, а всяко следващо е сумата от предходните две.

count = int(input())

first = 1
second = 1
third = first + second
for i in range(count):
    first = second
    second = third
    third = first + second

print(first)
