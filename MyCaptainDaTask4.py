import numpy as np 
import matplotlib.pyplot as plt
data = {'00:00 - 01:00' : 0, '01:00 - 02:00' : 0, '02:00 - 03:00' : 0, '03:00 - 04:00' : 0, '04:00 - 05:00' : 0, '05:00 - 06:00' : 0, '06:00 - 07:00' : 1, '07:00 - 08:00' : 4, '08:00 - 09:00' : 4, '09:00 - 10:00' : 5, '10:00 - 11:00' : 2, '11:00 - 12:00' : 3, '12:00 - 13:00' : 1, '13:00 - 14:00' : 0, '14:00 - 15:00' : 5, '15:00 - 16:00' : 1, '16:00 - 17:00' : 5, '17:00 - 18:00' : 0, '18:00 - 19:00' : 1, '19:00 - 20:00' : 1, '20:00 - 21:00' : 2, '21:00 - 22:00' : 5, '22:00 - 23:00' : 5, '23:00 - 00:00' : 0}
StartTime_EndTime = list(data.keys())
Productivity_Level = list(data.values())
fig = plt.figure(figsize = (10, 5))
plt.bar(StartTime_EndTime, Productivity_Level, color = 'red', width = 0.5)
plt.xlabel = ("Start Time - End Time")
plt.ylabel = ("Productivity Level")
plt.title = ("Daily Routine Productivity Level")
plt.xticks(rotation = 30, ha = 'right')
plt.tight_layout
plt.show()