size = int(input())
x = 'x'
space = ' '

figure = ''
# upper part
for u in range(size // 2):
    figure += f'{space * u}{x}{space*(size - 2 - u * 2)}{x}{space * u}\n'
# middle part
figure += f'{space*(size//2)}{x}{space*(size//2)}\n'
# lower part
for l in range(size // 2 - 1, -1, -1):
    figure += f'{space * l}{x}{space*(size - 2 - l * 2)}{x}{space * l}\n'
print(figure)
