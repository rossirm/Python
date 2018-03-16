class Student:
    def __init__(self, name, grades):
        self.name = name
        self.grades = grades
        self.avg_grade = sum(grades) / len(grades)

    @staticmethod
    def read_student():
        name, *grades = input().split(' ')
        return Student(name, list(map(float, grades)))

    def print_grade(self):
        return f'{self.name} -> {self.avg_grade:.2f}'


students = []
n = int(input())
for i in range(n):
    students.append(Student.read_student())

scholarship = [s for s in students if s.avg_grade >= 5]
result = ''
for s in sorted(scholarship, key=lambda x: (x.name, -x.avg_grade)):
    result += f'{s.print_grade()}\n'
print(result)
