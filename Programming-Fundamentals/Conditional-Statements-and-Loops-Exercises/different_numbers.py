start = int(input())
end = int(input())

result = ''
if (end - start) < 5:
    result = 'No'
else:
    for a in range(start, end + 1):
        for b in range(a, end + 1):
            for c in range(b, end + 1):
                for d in range(c, end + 1):
                    for e in range(d, end + 1):
                        if start <= a < b < c < d < e <= end:
                            result += f'{a} {b} {c} {d} {e}\n'
print(result)
