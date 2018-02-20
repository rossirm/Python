char = input()
vowels = 'aeiouAEIOU'

if char.isdigit():
    result = 'digit'
elif char in vowels:
    result = 'vowel'
else:
    result = 'other'
print(result)
