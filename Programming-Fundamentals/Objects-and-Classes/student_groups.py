from datetime import datetime


class Town:
    def __init__(self, name, capacity):
        self.name = name
        self.capacity = capacity
        self.students = []

    def register_student(self, student):
        self.students.append(student)

    def list_students(self):
        s_list = [student.mail for student in sorted(self.students, key=lambda st: (st.date, st.name, st.mail))]
        count = self.groups_count()
        gr_index = 0
        result = ''
        for g in range(count):
            group = ', '.join(s_list[gr_index:(gr_index + self.capacity)])
            result += f'{self.name} => {group}\n'
            gr_index += self.capacity
        return result

    def groups_count(self):
        return len(self.students) // self.capacity if len(self.students) % self.capacity == 0 \
            else len(self.students) // self.capacity + 1


class Student:
    def __init__(self, name, mail, date):
        self.name = name
        self.mail = mail
        self.date = date


towns = []
line = input()
while line != 'End':
    town, data = line.split('=>')
    seats_count, s = data.strip().split(' ')
    current_town = Town(town.strip(), int(seats_count))

    while True:
        line = input()
        if '=>' in line or line == 'End':
            towns.append(current_town)
            break

        s_name, s_mail, raw_date = line.split('|')
        d, m, y = raw_date.split('-')
        reg_date = datetime.strptime(raw_date.strip(), '%d-%b-%Y')
        current_student = Student(s_name.strip(), s_mail.strip(), reg_date)
        current_town.register_student(current_student)

groups = f'Created {sum([c.groups_count() for c in towns])} groups in {len(towns)} towns:\n'
for t in sorted(towns, key=lambda to: to.name):
    groups += t.list_students()
print(groups)
