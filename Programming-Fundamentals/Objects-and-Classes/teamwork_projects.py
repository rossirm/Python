class Team:
    def __init__(self, creator, name):
        self.name = name
        self.creator = creator
        self.members = {}

    def add_member(self, member):
        self.members[member] = True

    def print_info(self):
        members_list = ''.join([f'-- {m}\n' for m in sorted(self.members)]) if self.members else ''
        return f'{self.name}\n- {self.creator}\n{members_list}'


def create_teams():
    # creator : Team
    teams = {}

    # team_name : creator
    creators = {}

    all_members = {}
    message = ''

    count = int(input())
    for c in range(count):
        creator, team_name = input().split('-')
        if team_name in creators:
            message += f'Team {team_name} was already created!\n'
        elif creator in teams:
            message += f'{creator} cannot create another team!\n'
        else:
            teams[creator] = Team(creator, team_name)
            creators[team_name] = creator
            all_members[creator] = True
            message += f'Team {team_name} has been created by {creator}!\n'

    line = input()
    while line != 'end of assignment':
        member, team_name = line.split('->')
        if team_name not in creators:
            message += f'Team {team_name} does not exist!\n'
        elif member in teams or member in all_members:
            message += f'Member {member} cannot join team {team_name}!\n'
        else:
            teams[creators[team_name]].add_member(member)
            all_members[member] = True
        line = input()

    active = [t.creator for t in sorted(teams.values(), key=lambda n: (n.name, len(n.members))) if t.members]
    for t in active:
        message += teams[t].print_info()

    disband = [t.creator for t in sorted(teams.values(), key=lambda n: n.name) if not t.members]
    message += 'Teams to disband:\n'
    for d in disband:
        message += f'{teams[d].name}\n'

    return message


result = ''
print(create_teams())
# //TODO last 2 tests