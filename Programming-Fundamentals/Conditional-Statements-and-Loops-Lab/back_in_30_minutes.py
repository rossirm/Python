hours = int(input())
minutes = int(input())
time = hours * 60 + minutes + 30

result = f'{(time//60)%24}:{time%60:02}'
print(result)
