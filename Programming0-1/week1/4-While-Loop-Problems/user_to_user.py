__author__ = 'Боян'

start = input()
start = int(start)
end = input()
end = int(end)

greater = max(start, end)
lesser = min(start, end)
print("Counting from {} to {}".format(lesser, greater))
while lesser <= greater:
    print(lesser)
    lesser += 1