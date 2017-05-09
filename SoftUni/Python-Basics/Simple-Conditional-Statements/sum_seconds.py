# Трима спортни състезатели финишират за някакъв брой секунди (между 1 и 50).
# Да се напише програма, която въвежда времената на състезателите
# и пресмята сумарното им време във формат "минути:секунди".
# Секундите да се изведат с водеща нула

first = int(input())
second = int(input())
third = int(input())

seconds_total = first + second + third
minutes = seconds_total / 60
seconds = seconds_total % 60

print('{0}:{1:02}'.format(int(minutes), seconds))
