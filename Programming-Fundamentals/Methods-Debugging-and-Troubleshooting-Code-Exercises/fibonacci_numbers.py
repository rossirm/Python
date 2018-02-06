def get_fibonacci(n):
    first = 1
    second = 1
    third = first + second
    for i in range(n):
        first = second
        second = third
        third = first + second

    return first


number = int(input())
print(get_fibonacci(number))
