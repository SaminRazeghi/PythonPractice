import datetime
import time
date_entry = input("Enter a date in YYYY/MM/DD format and time in HH:MM:SS :")
date_time = date_entry.split(' - ')
print(date_time)
year, month, day = map(int, date_time[0].split('/'))
hour, minute, second = map(int, date_time[1].split(':'))
year = year - 1970
month = month - 1
day = day - 1
print(((year*365*24 + 6) + (month * 30.4375 * 24)) * 60 * 60)
