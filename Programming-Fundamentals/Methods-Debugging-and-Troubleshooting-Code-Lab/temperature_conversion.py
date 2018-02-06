def get_celsius(temp):
    return (temp - 32) * 5 / 9


fahrenheit = float(input())
celsius = get_celsius(fahrenheit)
print(f'{celsius:.2f}')
