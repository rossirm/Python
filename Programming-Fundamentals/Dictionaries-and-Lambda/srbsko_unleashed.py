srbsko = {}
line = input()
while line != 'End':
    try:
        singer, data = line.split(' @')
        venue, tickets_price, tickets_count = data.rsplit(' ', 2)
        income = int(tickets_count) * int(tickets_price)
    except ValueError:
        continue

    if venue not in srbsko:
        srbsko[venue] = {singer: income}
    else:
        if singer in srbsko[venue]:
            srbsko[venue][singer] += income
        else:
            srbsko[venue][singer] = income

    line = input()

result = ''
for place in srbsko:
    result += f'{place}\n'
    sorted_singers = sorted(srbsko[place].items(), key=lambda x: x[1], reverse=True)
    for singer, money in sorted_singers:
        result += f'#  {singer} -> {money}\n'

print(result)
