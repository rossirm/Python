count = int(input())

first = 1
second = 1
third = first + second
for i in range(count):
    first = second
    second = third
    third = first + second

print(first)
