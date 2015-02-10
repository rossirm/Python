__author__ = 'Боян'

start = input()
start = int(start)
end = input()
end = int(end)

greater = max(start, end)
lesser = min(start, end)

while lesser <= greater:
    current = lesser
    summed = 0
    while current > 1:
        summed += int(current % 10)
        current = int(current / 10)
    print("{0} --> {1} digit sum".format(lesser, summed))
    lesser += 1