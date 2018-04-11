class Message:
    def __init__(self, content, sender):
        self.content = content
        self.sender = sender


class User:
    def __init__(self, name, friends=None):
        self.name = name
        if friends is None:
            friends = {}
        self.friends = friends

    def receive_message(self, message):
        if message.sender not in self.friends:
            self.friends[message.sender] = []
        self.friends[message.sender].append(message)

    def count_messages(self, friend):
        if friend in self.friends and self.friends[friend]:
            return len(self.friends[friend])
        else:
            return 0

    def read_message(self, friend, index):
        if friend in self.friends:
            return self.friends[friend][index].content


users = {}
line = input()
while line != 'exit':
    command, username, *rest = line.split(' ')
    if command == 'register':
        if username not in users:
            users[username] = User(username)
    else:
        user, sends, recipient, text = line.split(' ')
        if user in users and recipient in users:
            users[recipient].receive_message(Message(text, user))

    line = input()

line = input()
first, second = line.split(' ')
f_messages = users[first].count_messages(second)
s_messages = users[second].count_messages(first)
replies = min(f_messages, s_messages)
not_replied = abs(f_messages - s_messages)

conversation = ''
if replies:
    for m in range(replies):
        conversation += f'{first}: {users[second].read_message(first, m)}\n' \
                        f'{users[first].read_message(second, m)} :{second}\n'

if not_replied:
    for m in range(replies, replies + not_replied):
        if f_messages < s_messages:
            conversation += f'{first}: {users[second].read_message(first, m)}\n'
        else:
            conversation += f'{users[first].read_message(second, m)} :{second}\n'

if not replies and not not_replied:
    conversation = 'No messages'

print(conversation)
