class Person:
    def __init__(self, name, pid, age):
        self.name = name
        self.pid = pid
        self.age = age


people = {}
line = input()
while line != 'End':
    n, i, a = line.split(' ')
    people[n] = Person(n, i, int(a))
    line = input()

p_list = ''
for p, d in sorted(people.items(), key=lambda x: x[1].age):
    p_list += f'{d.name} with ID: {d.pid} is {d.age} years old.'
print(p_list)
