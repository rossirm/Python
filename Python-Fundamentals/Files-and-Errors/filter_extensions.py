import os

path = './Resources/04. Filter-Extensions/input/'

extension = input()
files = '\n'.join([f'{file}' for file in os.listdir(path) if file.endswith(extension)])

with open(f'{path}Output-[{extension}].txt', 'w')as out:
    out.write(files)
