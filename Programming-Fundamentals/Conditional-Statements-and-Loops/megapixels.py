width = int(input())
height = int(input())
mega_pixels = width * height / 1000000

result = f'{width}x{height} => {round(mega_pixels, 1):g}MP'
print(result)
