import re

path = './sample_text.txt'

text = open(f'{path}', 'r').read()
punctuation = re.sub('[.,:!?]', '', text)
open(f'./sample_output.txt', 'w').write(punctuation)
