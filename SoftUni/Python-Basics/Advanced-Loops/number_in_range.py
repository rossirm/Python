# Напишете програма, която въвежда цяло положително число n в диапазона [1…100].
# При въвеждане на число извън посочения диапазон,
# да се отпечата съобщение за грешка и потребителят да се подкани да въведе ново число.

is_in_range = False

while not is_in_range:
    number = int(input('Еnter a number in the range [1...100]: '))
    is_in_range = 1 <= number <= 100
    if is_in_range:
        print('The number is: {}'.format(number))
        break
