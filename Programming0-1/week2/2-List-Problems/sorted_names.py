__author__ = 'Боян'

n = input("Enter count of names: ")
count_names = int(n)

names = []

counter = 1
while counter <= count_names:
    name = input("Enter a name: ")
    names = names + [name]
    counter += 1

names.sort()
print("Sorted names :")
for name in names:
    print(name)