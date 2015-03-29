__author__ = 'Боян'

s = input("Enter the first number")
start = int(s)
e = input("Enter the second number")
end = int(e)

greater = max(start, end)
lesser = min(start, end)
counter = lesser

print("Counting from {0} to {1}".format(lesser, greater))
while counter <= greater:
    if counter == 0:
        print("{} - zero".format(counter))
    elif counter % 2 == 0:
        print("{} - even".format(counter))
    elif counter % 2 != 0:
        print("{} - odd".format(counter))
    counter += 1