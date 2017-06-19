__author__ = 'Боян'


def status_count(students):
    students_statuses = {
        "finalized": [],
        "not_finalized": []
    }

    for student in students:
        if student["status"] == "finalized":
            students_statuses["finalized"] += [student["name"]]
        elif student["status"] == "not_finalized":
            students_statuses["not_finalized"] += [student["name"]]

    return students_statuses


python_students = [{"name": "RadoRado", "status": "not_finalized"},
                   {"name": "Ivo", "status": "finalized"},
                   {"name": "Genadi", "status": "finalized"}]
print(status_count(python_students))