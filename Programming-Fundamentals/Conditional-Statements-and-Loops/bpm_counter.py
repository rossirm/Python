beats_per_minute = int(input())
number_of_beats = int(input())

bars = number_of_beats / 4
time = number_of_beats / beats_per_minute * 60
minutes = int(time / 60)
seconds = int(time % 60)

result = f'{round(bars , 1):g} bars - {minutes:g}m {seconds:g}s'
print(result)
