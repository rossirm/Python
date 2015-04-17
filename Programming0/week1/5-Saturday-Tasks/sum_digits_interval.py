__author__ = 'Боян'

s = input("Enter the first number")
start = int(s)
e = input("Enter the second number")
end = int(e)

greater = max(start, end)
lesser = min(start, end)
counter = lesser

while counter <= greater:
    current = counter
    total = 0
    while current > 0:
        total += current % 10
        current //= 10
    print("{0} --> {1} digit sum".format(counter, total))
    counter += 1