def check_special(n):
    digits_sum = sum(list(map(int, n)))
    is_special = digits_sum == 5 or digits_sum == 7 or digits_sum == 11
    return is_special


number = input()
start = 1
end = int(number) + 1

result = ''
for i in range(start, end):
    result += f'{i} -> {check_special(str(i))}\n'
print(result)
