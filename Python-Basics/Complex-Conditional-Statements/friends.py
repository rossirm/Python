# Да се напише програма, която въвежда дали всеки от двамата ти приятели е навън(те се мразят един друг)
# и проверява дали ти да останеш вкъщи.

first = input().lower()
second = input().lower()
result = ''

if (first == 'out') ^ (second == 'out'):
    result = 'Go out!'
else:
    result = 'Stay at home!'

print(result)
