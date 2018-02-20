first = list(filter(None, input().split(' ')))
second = list(filter(None, input().split(' ')))

length = min(len(first), len(second))
right = 0
left = 0
for i in range(length):
    if first[i] == second[i]:
        right += 1
    if first[len(first) - 1 - i] == second[len(second) - 1 - i]:
        left += 1

print(left if left > right else right)
