country = input()

language = ''
if country == 'USA' or country == 'England':
    language = 'English'
elif country == 'Spain' or country == 'Argentina' or country == 'Mexico':
    language = 'Spanish'
else:
    language = 'unknown'

print(language)
