text = input()
# TODO regex splitting
words = filter(None, text.split())
print(words)
lower_case = []
upper_case = []
mixed_case = []
for word in words:
    are_lower = True
    are_upper = True
    # print(words)
    for char in word:
        if char.islower() or char.isdigit():
            are_upper = False
        elif char.isupper() or char.isdigit():
            are_lower = False
    if are_lower:
        lower_case.append(word)
    elif are_upper:
        upper_case.append(word)
    else:
        mixed_case.append(word)
separator = ', '
print(f'Lower-case: {separator.join(lower_case)}\n'
      f'Mixed-case: {separator.join(mixed_case)}\n'
      f'Upper-case: {separator.join(upper_case)}')
