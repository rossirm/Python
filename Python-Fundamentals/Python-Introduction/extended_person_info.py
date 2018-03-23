def check_age(some_age):
    if some_age < 18:
        return 'teen'
    elif some_age < 70:
        return 'adult'
    else:
        return 'elder'


def check_salary(some_salary):
    if some_salary < 500:
        return 'low'
    elif some_salary < 2000:
        return 'medium'
    else:
        return 'high'


name = input()
age = int(input())
town = input()
salary = float(input())

print(f'Name: {name}\nAge: {age}\nTown: {town}\nSalary: ${salary:.2f}\n'
      f'Age range: {check_age(age)}\nSalary range: {check_salary(salary)}')
