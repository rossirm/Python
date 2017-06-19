# Напишете програма, която въвежда две цели положителни числа a и b и изчислява
# и отпечатва най-големият им общ делител (НОД).

first = int(input())
second = int(input())
# Swap numbers to ensure first is greater
temp = second
if first > second:
    second = first
    first = temp
# Euclidean algorithm
while second != 0:
    temp = second
    second = first % second
    first = temp

print(first)
