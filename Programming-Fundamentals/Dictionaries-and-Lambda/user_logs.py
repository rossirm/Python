users = {}
line = input()
while line != 'end':
    ip, message, user = line.split(' ')
    i, ip_address = ip.split('=')
    u, name = user.split('=')

    if name not in users:
        users[name] = {ip_address: 1}
    else:
        if ip_address in users[name]:
            users[name][ip_address] += 1
        else:
            users[name][ip_address] = 1

    line = input()

report = ''
for name, ip in sorted(users.items()):
    ip_list = []
    for address, count in ip.items():
        ip_list.append(f'{address} => {count}')

    report += f'{name}:\n{", ".join(ip_list)}.\n'
print(report)
