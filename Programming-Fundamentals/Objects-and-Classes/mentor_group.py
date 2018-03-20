from datetime import date


class Mentor:
    def __init__(self, name):
        self.name = name
        self.dates = []
        self.comments = []

    def add_date(self, a_date):
        self.dates.append(a_date)

    def add_comment(self, a_comment):
        self.comments.append(a_comment)

    def generate_report(self):
        comments = ''.join([f'- {c}\n' for c in self.comments]) if self.comments else ''
        dates_at = ''.join([f'-- {d.strftime("%d/%m/%Y")}\n' for d in sorted(self.dates)]) if self.dates else ''
        return f'{self.name}\nComments:\n{comments}Dates attended:\n{dates_at}'


def fill_mentors(mentors_list):
    # read dates
    line = input()
    while line != 'end of dates':
        date_line = line.split(' ')
        current_mentor = Mentor(date_line[0])
        if date_line[0] not in mentors_list:
            mentors_list[date_line[0]] = current_mentor
        if len(date_line) > 1:
            dates = filter(None, date_line[1].split(','))
            for d in dates:
                [d, m, y] = filter(None, d.split('/'))
                mentors_list[date_line[0]].add_date(date(year=int(y), month=int(m), day=int(d)))

        line = input()

    # read comments
    line = input()
    while line != 'end of comments':
        comment_line = line.split('-')
        if comment_line[0] in mentors_list:
            if comment_line[1]:
                mentors_list[comment_line[0]].add_comment(comment_line[1])

        line = input()

    return mentors_list


mentors = {}
fill_mentors(mentors)
result = ''
for me in sorted(mentors):
    result += f'{mentors[me].generate_report()}'
print(result)
