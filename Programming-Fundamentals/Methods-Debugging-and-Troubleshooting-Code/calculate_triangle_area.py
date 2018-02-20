def triangle_area(base, height):
    return format_output(base * height / 2)


def format_output(area):
    return f'{area:.12g}'


b = float(input())
h = float(input())
print(triangle_area(b, h))
