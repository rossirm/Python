number = int(input())

text = ''
if number < 0 or number > 100:
    text = 'invalid number'
elif number == 100:
    text = 'one hundred'
elif number == 0:
    text = 'zero'
else:
    ones = number % 10
    tens = (number // 10) % 10
    # From 10 to 20
    if tens == 1:
        if ones == 0:
            text = 'ten'
        elif ones == 1:
            text = 'eleven'
        elif ones == 2:
            text = 'twelve'
        elif ones == 3:
            text = 'thirteen'
        elif ones == 4:
            text = 'fourteen'
        elif ones == 5:
            text = 'fifteen'
        elif ones == 6:
            text = 'sixteen'
        elif ones == 7:
            text = 'seventeen'
        elif ones == 8:
            text = 'eighteen'
        elif ones == 9:
            text = 'nineteen'
    # Above 20
    elif tens > 1:
        if tens == 2:
            text = 'twenty'
        elif tens == 3:
            text = 'thirty'
        elif tens == 4:
            text = 'forty'
        elif tens == 5:
            text = 'fifty'
        elif tens == 6:
            text = 'sixty'
        elif tens == 7:
            text = 'seventy'
        elif tens == 8:
            text = 'eighty'
        elif tens == 9:
            text = 'ninety'
        # Leave space in case there is ones to print
        if ones != 0:
            text += ' '
    # Set ones in cases tens are under 10 or above 19
    if tens != 1:
        if ones == 1:
            text += 'one'
        elif ones == 2:
            text += 'two'
        elif ones == 3:
            text += 'three'
        elif ones == 4:
            text += 'four'
        elif ones == 5:
            text += 'five'
        elif ones == 6:
            text += 'six'
        elif ones == 7:
            text += 'seven'
        elif ones == 8:
            text += 'eight'
        elif ones == 9:
            text += 'nine'

print(text)
