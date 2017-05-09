# Да се напише програма, която въвежда цяло число в диапазона [0…10]
# и го изписва с думи на английски език.
# Ако числото е извън диапазона, изписва “number too big”.

number = int(input())

word = ''
if number == 0:
    word = 'zero'
elif number == 1:
    word = 'one'
elif number == 2:
    word = 'two'
elif number == 3:
    word = 'three'
elif number == 4:
    word = 'four'
elif number == 5:
    word = 'five'
elif number == 6:
    word = 'six'
elif number == 7:
    word = 'seven'
elif number == 8:
    word = 'eight'
elif number == 9:
    word = 'nine'
else:
    word = 'number too big'

print(word)
