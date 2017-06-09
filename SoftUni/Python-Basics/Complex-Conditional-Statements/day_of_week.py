# Print the day name (in English) by day number in range [1...7]
# or prints “Error” for invalid day number.

number = int(input())

day = ''
if number == 1:
    day = 'Monday'
elif number == 2:
    day = 'Tuesday'
elif number == 3:
    day = 'Wednesday'
elif number == 4:
    day = 'Thursday'
elif number == 5:
    day = 'Friday'
elif number == 6:
    day = 'Saturday'
elif number == 7:
    day = 'Sunday'
else:
    day = 'Error'

print(day)
