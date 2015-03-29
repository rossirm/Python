__author__ = 'Боян'


def get_people_count(activity):
    people = []

    for person in activity:
        if person not in people:
            people += [person]

    return len(people)


print(get_people_count(
    ['Anetta', 'Maria', 'Rado', 'Gergana', 'Philip', 'Gergana', 'Rado', 'Maria', 'Anetta', 'Ivo', 'Gergana', 'Maria',
     'Maria', 'Anetta', 'Gergana', 'Rado', 'Philip', 'Rado']))