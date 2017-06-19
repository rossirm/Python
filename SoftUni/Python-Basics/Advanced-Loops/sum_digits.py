# Напишете програма, която въвежда цяло число num и отпечатва сумата от цифрите му.

number = input()

digit_sum = 0
for digit in number:
    digit_sum += int(digit)

print(digit_sum)
