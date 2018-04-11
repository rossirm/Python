def check_type(text):
    try:
        if float(text) == int(float(text)):
            return {'Age': int(float(text))}
        elif float(text) != int(float(text)):
            return {'Salary': float(text)}
    except ValueError:
        return {'Position': text}


def fill_base(storage):
    line = input()
    while line != 'filter base':
        first, second = line.split(' -> ')
        storage.append({first: check_type(second)})

        line = input()
    return storage


base = []
fill_base(base)

table = input()
result = ''
separator = '=' * 20
for entry in range(len(base)):
    for name, data in base[entry].items():
        if table in data:
            result += f'Name: {name}\n{table}: {data[table]}\n{separator}\n'

print(result)
