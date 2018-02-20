week_days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]

number = int(input())
if 1 <= number <= 7:
    print(week_days[number - 1])
else:
    print('Invalid Day!')
