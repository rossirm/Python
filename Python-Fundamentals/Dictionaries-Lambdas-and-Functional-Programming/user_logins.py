users = {}
line = input()
while line != 'login':
    username, password = filter(None, line.split(' -> '))
    users[username] = password

    line = input()

result = ''
attempts = 0
line = input()
while line != 'end':
    username, password = filter(None, line.split(' -> '))
    if username in users and users[username] == password:
        result += f'{username}: logged in successfully\n'
    else:
        result += f'{username}: login failed\n'
        attempts += 1

    line = input()

result += f'unsuccessful login attempts: {attempts}\n'
print(result)
