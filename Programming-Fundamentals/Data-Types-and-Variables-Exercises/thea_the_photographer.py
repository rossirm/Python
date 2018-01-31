from datetime import datetime, timezone, timedelta
from math import ceil

pictures = int(input())
filtering = int(input())
percent_good = int(input())
upload_time = int(input())

filtered = ceil(pictures * percent_good / 100)
time_filter = pictures * filtering
time_to_upload = filtered * upload_time
time = time_filter + time_to_upload

days = time // 86400
time -= days * 86400
hours = time // 3600
time -= hours * 3600
minutes = time // 60
time -= minutes * 60
seconds = time % 60

print(f'{days}:{hours:02d}:{minutes:02d}:{seconds:02d}')

# d = timedelta(seconds=time)
# t = datetime.fromtimestamp(time, timezone.utc).strftime('%H:%M:%S')
# print(f'{d.days}:{t}')
