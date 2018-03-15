stats = {}
population_stats = {}

line = input()
while line != 'report':
    city, country, population = line.split('|')
    city, country, population = city.strip(), country.strip(), int(population.strip())

    if country not in stats:
        stats[country] = {city: population}
        population_stats[country] = population
    else:
        population_stats[country] += population
        if city in stats[country]:
            stats[country][city] += population
        else:
            stats[country][city] = population

    line = input()

result = ''
for country, population in sorted(population_stats.items(), key=lambda x: x[1], reverse=True):
    result += f'{country} (total population: {population})\n'

    for city, people in sorted(stats[country].items(), key=lambda x: x[1], reverse=True):
        result += f'=>{city}: {people}\n'

print(result)
