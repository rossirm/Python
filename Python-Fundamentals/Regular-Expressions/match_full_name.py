import re

pattern = '(\\b[A-Z]{1}[a-z]+)( )([A-Z]{1}[a-z]+\\b)'

names = input()
print(re.findall(pattern, names))

