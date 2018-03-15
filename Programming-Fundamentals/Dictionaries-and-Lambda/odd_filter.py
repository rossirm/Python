numbers = list(map(int, input().split(' ')))

evens = [x for x in numbers if x % 2 == 0]
avg = sum(evens) / len(evens)

odds = []
for e in evens:
    odds.append(e + 1 if e > avg else e - 1)
print(' '.join([str(x) for x in odds]))
