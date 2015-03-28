__author__ = 'Боян'

user = input("Write something")

vowels = ['a', 'e', 'i', 'o', 'u', 'y', 'A', 'E', 'I', 'O', 'U', 'Y']

counter = 0
vowels_found = []
for v in user:
    if v in vowels:
        vowels_found += v
        counter += 1

if len(vowels_found) > 0:
    print("{0} vowels found in {1}:\n{2}".format(len(vowels_found), user, vowels_found))
else:
    print("No vowels are found")