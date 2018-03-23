def add_mails(user_name, e_mail):
    banned_domains = ['us', 'uk']

    user, domain = e_mail.split('@')
    service, region = domain.split('.')
    if region.lower() not in banned_domains:
        return {user_name.strip(): e_mail.strip()}


path = './Resources-Exercises/05. Fix Emails/'
mails = {}

with open(f'{path}input.txt', 'r') as f:
    line = f.readline()
    while line != 'stop':
        name = line
        line = f.readline()
        mail = line
        mails.update(add_mails(name, mail))
        line = f.readline()

result = ''
for n, m in mails.items():
    result += f'{n} -> {m}\n'

with open(f'{path}output.txt', 'w') as output:
    output.write(result)
