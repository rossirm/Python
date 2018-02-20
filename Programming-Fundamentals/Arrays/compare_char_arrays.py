first = input().split(' ')
second = input().split(' ')

first_is_before = True
are_equal = True
length = min(len(first), len(second))
have_same_length = len(first) == len(second)
if not have_same_length:
    are_equal = False
    if len(first) > len(second):
        first_is_before = False

for i in range(length):
    if first[i] > second[i]:
        first_is_before = False
        are_equal = False
        break
    if first[i] < second[i]:
        are_equal = False
        break

result = ''
if are_equal or first_is_before:
    result += ''.join(first) + '\n' + ''.join(second)
else:
    result += ''.join(second) + '\n' + ''.join(first)
print(result)
