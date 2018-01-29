noun = input()

plural = noun
if noun[-1] == 'o' or noun[-1] == 's' or noun[-1] == 'x' or noun[-1] == 'z':
    plural += 'es'
elif (noun[-2] == 's' or noun[-2] == 'c') and noun[-1] == 'h':
    plural += 'es'
elif noun[-1] == 'y':
    plural = plural[:-1]+'ies'
else:
    plural += 's'

print(plural)
