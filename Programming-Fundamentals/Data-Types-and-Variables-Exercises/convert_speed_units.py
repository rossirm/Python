distance = float(input())
hours = int(input())
minutes = int(input())
seconds = int(input())

time = hours * 3600 + minutes * 60 + seconds
mile = 1609
ms = distance / time
kms = (distance / 1000) / (time / 3600)
mls = (distance / mile) / (time / 3600)

print(f'{ms:.7g}\n{kms:.7g}\n{mls:.7g}')
