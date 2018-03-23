import os

path = './Resources/04. Filter-Extensions/input/'

extension = input()
files = '\n'.join([f'{file}' for file in os.listdir(path) if file.endswith(extension)])

open(f'{path}Output.txt', 'w').write(files)
