import re

path = './Resources/03. Word Count/'

words = open(f'{path}words.txt', 'r').read().lower().split(' ')
text = open(f'{path}text.txt').read()
words_in_text = list(filter(None, re.findall(r'(\w*)', text.lower())))

occurrences = {}
for word in words:
    occurrences[word] = words_in_text.count(word)

result = '\n'.join([f'{w} - {c}' for w, c in sorted(occurrences.items(), key=lambda c: -c[1])])
open(f'{path}Output.txt', 'w').write(result)
