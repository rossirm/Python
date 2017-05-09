# Да се напише програма, която въвежда две думи и проверява дали са еднакви.
# Да не се прави разлика между главни и малки думи.

first_word = input()
second_word = input()

if first_word.lower() == second_word.lower():
    print('yes')
else:
    print('no')
