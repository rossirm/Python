# Да се напише програма, която въвежда текст (стринг)
# и изчислява и отпечатва сумата от стойностите на гласните букви според таблицата по-долу:
# буква	    A	e	i	o	U
# стойност	1	2	3	4	5

text = input()

total = 0
for letter in text:
    if letter == 'a':
        total += 1
    elif letter == 'e':
        total += 2
    elif letter == 'i':
        total += 3
    elif letter == 'o':
        total += 4
    elif letter == 'u':
        total += 5

print(total)
