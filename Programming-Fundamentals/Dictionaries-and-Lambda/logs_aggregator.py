logs = {}

count = int(input())
for i in range(count):
    ip, user, time = input().split(' ')
    if user not in logs:
        logs[user] = {'duration': int(time), 'ip_list': [ip]}
    else:
        logs[user]['duration'] += int(time)
        logs[user]['ip_list'].append(ip)

result = ''
for user in sorted(logs):
    ip_list = ", ".join([str(x) for x in sorted(set(logs[user]["ip_list"]))])
    result += f'{user}: {logs[user]["duration"]} [{ip_list}]\n'
print(result)
