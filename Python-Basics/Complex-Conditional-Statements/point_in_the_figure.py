# Напишете програма, която въвежда цяло число h и координатите на дадена точка {x, y} (цели числа)
# и отпечатва дали точката е вътре във фигурата (inside),
# вън от фигурата (outside)
# или на някоя от стените на фигурата (border).

size = int(input())
x = int(input())
y = int(input())

is_inside = ((0 < x < 3 * size) and (0 < y < 1 * size)) \
            or ((1 * size < x < 2 * size) and (1 * size < y < 4 * size))
is_outside = ((0 > x or x > 3 * size) or (0 > y or y > 1 * size)) \
             and ((1 * size > x or x > 2 * size) or (1 * size > y or y > 4 * size))
is_on_common = (1 * size < x < 2 * size) and (y == 1 * size)

result = ''
if is_inside or is_on_common:
    result = 'inside'
elif is_outside:
    result = 'outside'
else:
    result = 'border'

print(result)
