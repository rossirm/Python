first = int(input())
second = int(input())
# Swap numbers to ensure first is greater
if first > second:
    second = first + second
    first = second - first
    second = second - first
# Euclidean algorithm
while second != 0:
    temp = second
    second = first % second
    first = temp

print(first)
