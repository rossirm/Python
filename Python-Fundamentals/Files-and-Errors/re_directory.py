import os, shutil

path = './Resources/08. Re-Directory/'

extensions = set([os.path.splitext(f)[-1][1:] for f in os.listdir(f'{path}/input')])

if not os.path.exists(f'{path}output/'):
    os.makedirs(f'{path}output/')
for ext in extensions:
    if not os.path.exists(f'{path}{ext}s'):
        os.makedirs(f'{path}output/{ext}s')

    for f in os.listdir(f'{path}input/'):
        if os.path.splitext(f)[-1][1:] == ext:
            shutil.copy2(f'{path}input/{f}', f'{path}output/{ext}s/')
