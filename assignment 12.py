#Q1
from datetime import date
days=['Monday','Tuesday','Wednesday','Thursday','Friday','Saturday','Sunday']
print(days[date.weekday(date.today())])

#Q2
import webbrowser
search=(input('enter to search video on youtube: '))
webbrowser.open('https://www.youtube.com/results?search_query= %s' %search)

#Q3
import os
os.rename('file.txt','file.jpg')