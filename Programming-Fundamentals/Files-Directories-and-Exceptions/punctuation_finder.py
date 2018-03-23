import re

path = './sample_text.txt'

text = open(f'{path}', 'r').read()
punctuation = re.findall('[.,:!?]', text)
print(', '.join(punctuation))
