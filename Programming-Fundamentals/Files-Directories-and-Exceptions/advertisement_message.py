import random
def generate_message(count):
    phrases = ['Excellent product.', 'Such a great product.', 'I always use that product.', 'Best product of its category.',
               'Exceptional product.', 'I can’t live without this product.']
    events = ['Now I feel good.', 'I have succeeded with this product.', 'Makes miracles. I am happy of the results!',
              'I cannot believe but now I feel awesome.', 'Try it yourself, I am very satisfied.', 'I feel great!']
    authors = ['Diana', 'Petya', 'Stella', 'Elena', 'Katya', 'Iva', 'Annie', 'Eva']
    cities = ['Burgas', 'Sofia', 'Plovdiv', 'Varna', 'Ruse']


    messages = ''
    for m in range(count):
        messages += f'{phrases[random.randint(0, len(phrases) - 1)]} {events[random.randint(0, len(events) - 1)]} ' \
                    f'{authors[random.randint(0, len(authors) - 1)]} – {cities[random.randint(0, len(cities) - 1)]}.\n'
    return messages


n = int(input())
result = generate_message(n)

path = './Resources-Exercises/'



with open(f'{path}advertisement.txt', 'w') as output:
    output.write(result)

