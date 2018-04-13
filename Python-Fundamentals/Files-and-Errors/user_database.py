import json


def fill_base(database):
    result = ''
    line = input()
    while line != 'exit':
        command, *rest = line.split(' ', 1)
        if command == 'register':
            command, username, password, confirm = line.split(' ')
            if username in database:
                result += f'The given username already exists.\n'
            elif password != confirm:
                result += f'The two passwords must match.\n'
            else:
                database[username] = password

        elif command == 'login':
            command, username, password = line.split(' ')
            if database['logged']:
                result += f'There is already a logged in user.\n'
            elif username not in database:
                result += f'There is no user with the given username.\n'
            elif password != database[username]:
                result += f'The password you entered is incorrect.\n'
            else:
                database['logged'].append(username)

        elif command == 'logout':
            if not database['logged']:
                result += f'There is no currently logged in user.\n'
            else:
                database['logged'].pop()

        line = input()

    print(result)


db = {'logged': []}
fill_base(db)
# print(f'{db.items()} {db["logged"]}')
with open('users.txt', 'w') as u:
    u.write(json.dumps(db))

with open('users.txt', 'r') as b:
    db = json.loads(b.read())

fill_base(db)
# print(f'{db.items()} {db["logged"]}')
