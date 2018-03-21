text = input()
separators = [',', ';', ':', '.', '!', '(', ')', '"', "'", '\\', '/', '[', ']', '?']

for s in separators:
    text = text.replace(s, ' ')
words = filter(None, text.split(' '))

short = ', '.join(sorted(set([w.lower() for w in words if len(w) < 5])))
print(short)
