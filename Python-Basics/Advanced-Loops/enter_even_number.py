# Напишете програма, която въвежда четно число.
# Ако потребителят въведе грешно число (нечетно число или стринг, който не е цяло число),
# трябва да му излиза съобщение за грешка и да въвежда отново.

is_even = False
number = 1

while not is_even:
    try:
        number = int(input())
        is_even = number % 2 == 0
    except:
        print('Invalid number!')

print(number)
