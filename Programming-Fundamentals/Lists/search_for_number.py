integers = list(map(int, filter(None, input().split(' '))))
count, remove, number = list(map(int, filter(None, input().split(' '))))

has_number = number in integers[remove:count]
print('YES!' if has_number else 'NO!')
