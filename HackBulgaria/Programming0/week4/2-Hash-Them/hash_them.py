__author__ = 'Боян'

hashed = {}


def hash_them(keys, values):
    index = 0
    while index < len(keys):
        if index < len(values):
            hashed[keys[index]] = values[index]
        else:
            hashed[keys[index]] = None
        index += 1

    return hashed


print(hash_them(["Ivan", "Maria"], [1, 2]))
print(hash_them(["Ivan", "Maria"], [1]))