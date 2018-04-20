import re

text = input()

regex = '<\w+>'
matches = re.findall(regex, text)

result = ''
if matches:
    for match in matches:
        result += f'Found {sum(int(l) for l in match if l.isdigit())} carat diamond\n'
else:
    result = 'Better luck next time'

print(result)
