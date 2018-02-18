plant = input()

result = ''
if plant == 'banana' or plant == 'apple' or plant == 'kiwi' \
        or plant == 'cherry' or plant == 'lemon' or plant == 'grapes':
    result = 'fruit'
elif plant == plant == 'tomato' or plant == 'cucumber' or plant == 'pepper' or plant == 'carrot':
    result = 'vegetable'
else:
    result = 'unknown'

print(result)
