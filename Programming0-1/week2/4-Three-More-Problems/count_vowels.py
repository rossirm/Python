__author__ = 'Боян'

user = input("Write something")

vowels = ['a', 'e', 'i', 'o', 'u', 'y', 'A', 'E', 'I', 'O', 'U', 'Y']

counter = 0
# vowels_found = []
for v in user:
    if v in vowels:
        # vowels_found += v
        counter += 1
# if len(vowels_found) > 0:
# print(vowels_found)
# print(len(vowels_found))
# else:
# print("No vowels are found")
print(counter)