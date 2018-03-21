first, second = input().split(' ')

print('true' if len(set(first)) == len(set(second)) else 'false')
