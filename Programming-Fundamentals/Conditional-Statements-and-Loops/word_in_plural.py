noun = input()

last_letter = noun[-1]
plural = noun
if last_letter == 'o' or last_letter == 's' or last_letter == 'x' or last_letter == 'z':
    plural += 'es'
elif (noun[-2] == 's' or noun[-2] == 'c') and last_letter == 'h':
    plural += 'es'
elif last_letter == 'y':
    plural = plural[:-1] + 'ies'
else:
    plural += 's'

print(plural)
