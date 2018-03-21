text = input()
separators = [',', ';', ':', '.', '!', '(', ')', '"', "'", '\\', '/', '[', ']','?']

for s in separators:
    text = text.replace(s, ' ')
text = filter(None, text.split(' '))

lower_case = []
upper_case = []
mixed_case = []

for word in text:
    if all((c.isalpha() and not c.isdigit() and c.islower()) for c in word):
        lower_case.append(word)
    elif all((c.isalpha() and not c.isdigit() and c.isupper()) for c in word):
        upper_case.append(word)
    else:
        mixed_case.append(word)
separator = ', '
print(f'Lower-case: {separator.join(lower_case)}\n'
      f'Mixed-case: {separator.join(mixed_case)}\n'
      f'Upper-case: {separator.join(upper_case)}')
