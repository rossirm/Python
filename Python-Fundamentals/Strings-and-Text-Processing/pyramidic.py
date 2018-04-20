count = int(input())
strings = [''] * count

for c in range(count):
    strings[c] = input()

letter = strings[len(strings) - 1][len(strings[len(strings) - 1]) - 1:]

py = letter
for s in range(count):
    if py in strings[s]:
        print(py)
        py += letter + letter
