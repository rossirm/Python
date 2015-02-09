__author__ = 'Боян'

start = input()
start = int(start)
end = input()
end = int(end)

greater = max(start, end)
lesser = min(start, end)
print("Counting from {} to {}".format(lesser, greater))
while lesser <= greater:
    if lesser == 0:
        print("{} - zero".format(lesser))
    elif lesser % 2 == 0:
        print("{} - even".format(lesser))
    else:
        print("{} - odd".format(lesser))
    lesser += 1