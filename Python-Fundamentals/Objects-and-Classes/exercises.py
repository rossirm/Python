class Exercise:
    def __init__(self, topic, course_name, judge_contest_link, problems):
        self.topic = str(topic)
        self.course_name = course_name
        self.judge_contest_link = judge_contest_link
        self.problems = [*problems]

    def get_info(self):
        info = f'Exercises: {self.topic}\n' \
               f'Problems for exercises and homework for the "{self.course_name}" course @ SoftUni.' \
               f'\nCheck your solutions here: {self.judge_contest_link}\n'
        for p in range(len(self.problems)):
            if p == len(self.problems) - 1:
                info += f'{p + 1}. {self.problems[p]}'
            else:
                info += f'{p + 1}. {self.problems[p]}\n'
        return info


def build_exercises(storage):
    line = input()
    while line != 'go go go':
        topic, course_name, judge_contest_link, problems = line.split(' -> ')
        problems = problems.split(', ')
        storage.append(Exercise(topic, course_name, judge_contest_link, problems))
        line = input()


exercises = []
build_exercises(exercises)
for exercise in exercises:
    print(exercise.get_info())
