integers = []
count = int(input())
for i in range(count):
    integers.append(int(input()))

result = ' '.join([str(i) for i in integers[::-1]])
print(result)
