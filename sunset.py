import datetime
from suntime import Sun, SunTimeException

latitude = 39.653948
longitude = -104.879104

sun = Sun(latitude, longitude)

today_sunset = sun.get_local_sunset_time()
#print(type(today_sunset.hour))
with open("sunset_time.txt", 'w') as file:
    file.write(f'{today_sunset.hour}'.zfill(2) + ":" + f'{today_sunset.minute}'.zfill(2))