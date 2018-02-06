def is_float(text):
    try:
        float(text)
        return True
    except ValueError:
        return False


def is_integer(text):
    try:
        int(text)
        return True
    except ValueError:
        return False


ages = {}
salaries = {}
positions = {}

line = input()
while line != 'filter base':
    name, second = filter(None, line.split(' -> '))
    if is_integer(second):
        ages[name] = int(second)
    elif is_float(second):
        salaries[name] = float(second)
    else:
        positions[name] = second
    line = input()

result = ''
separator = '=' * 20
table = input()
if table == 'Age':
    for age in ages:
        result += f'Name: {age}\nAge: {ages[age]}\n{separator}\n'
if table == 'Salary':
    for salary in salaries:
        result += f'Name: {salary}\nSalary: {salaries[salary]}\n{separator}\n'
if table == 'Position':
    for position in positions:
        result += f'Name: {position}\nPosition: {positions[position]}\n{separator}\n'
print(result)
