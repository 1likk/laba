#1 Subtract five days from the current date:
from datetime import datetime, timedelta

current_date = datetime.now()
five_days_ago = current_date - timedelta(days=5)

print("Дата сейчас: ", current_date)
print("Дата 5 дней назад: ", five_days_ago)

#2 Print yesterday, today, and tomorrow:
from datetime import datetime, timedelta

today = datetime.now()
yesterday = today - timedelta(days=1)
tomorrow = today + timedelta(days=1)

print("Вчера: ", yesterday)
print("Сегодня: ", today)
print("Завтра: ", tomorrow)

#3
from datetime import datetime
def drop_microseconds(dt):

    dt_without_microseconds = dt.replace(microsecond=0)
    return dt_without_microseconds


current_datetime = datetime.now()
datetime_without_microseconds = drop_microseconds(current_datetime)
print("Дата и время без микросекунд:", datetime_without_microseconds)


#4 Python program to calculate the difference between two dates in seconds:
from datetime import datetime


def date_difference_seconds(date1, date2):
    dt1 = datetime.strptime(date1, "%Y-%m-%d %H:%M:%S")
    dt2 = datetime.strptime(date2, "%Y-%m-%d %H:%M:%S")


    difference = abs((dt2 - dt1).total_seconds())

    return difference

date1 = "2024-03-01 12:00:00"
date2 = "2024-03-02 12:00:00"

difference_seconds = date_difference_seconds(date1, date2)
print("Разница между двумя датами в секундах:", difference_seconds)
