mails = {}
banned_domains = ['us', 'uk']
name = ''
mail = ''

line_count = 0
line = input()
while line != 'stop':
    if line_count % 2 == 0:
        name = line
    else:
        mail = line
        user, domain = line.split('@')
        service, region = domain.split('.')
        if region.lower() not in banned_domains:
            mails[name] = mail

    line_count += 1
    line = input()

result = ''
for n, m in mails.items():
    result += f'{n} -> {m}\n'
print(result)
