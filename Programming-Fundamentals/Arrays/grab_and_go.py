numbers = list(map(int, filter(None, input().split(' '))))
seek = int(input())

try:
    last = len(numbers) - numbers[::-1].index(seek) - 1
    total = sum(numbers[:last])
    print(total)
except ValueError:
    print('No occurrences were found!')
