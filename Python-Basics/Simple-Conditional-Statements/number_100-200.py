# Да се напише програма, която въвежда цяло число и проверява дали е под 100, между 100 и 200 или над 200.

number = int(input())

if number < 100:
    print('Less than 100')
elif 100 <= number <= 200:
    print('Between 100 and 200')
elif number > 200:
    print('Greater than 200')
