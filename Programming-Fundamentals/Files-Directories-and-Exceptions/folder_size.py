import os

path = './Resources/05. Folder Size/TestFolder/'

sizes = sum([os.stat(f'{path}{f}').st_size for f in os.listdir(path) if os.path.isfile(f'{path}{f}')])

result = sizes / 1024 / 1024
open(f'{path}Output.txt', 'w').write(str(result))
