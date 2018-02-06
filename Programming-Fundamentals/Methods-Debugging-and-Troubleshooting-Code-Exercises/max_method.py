def get_max(a, b):
    return a if a > b else b


first = int(input())
second = int(input())
third = int(input())

biggest = get_max(first, get_max(second, third))
print(biggest)
