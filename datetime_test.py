import datetime
import pytz

## Use aware dates and times!

## this is naive dates
today = datetime.date.today()
christmas = datetime.date(2023, 12, 24)

time_delta = datetime.timedelta(days=100)
in_hundred_days = today + time_delta ### What date it is in 100 days

print(in_hundred_days.isoweekday())


#print(type(time_delta))

till_christmas = christmas - today ### Returns a timedelta / difference between times in days or time

#print(till_christmas)
print(today + till_christmas)

#print(date1)
print(today.isoweekday())


date_today = datetime.datetime.today()
date_now = datetime.datetime.now()
date_utc_now = datetime.datetime.utcnow()


print(date_today)
print(date_now)
print(date_utc_now)


### Time zone AWARE datetime

aware_utc_now = datetime.datetime.now(tz=pytz.UTC)
aware_date = datetime.datetime(2023, 12, 24, tzinfo=pytz.UTC)

now = aware_utc_now.astimezone(pytz.timezone("Europe/Oslo"))

print(now.date())
print(now.isoweekday())

### Converting datetime to string and reverse

print(now.strftime("%B %D %Y"))

print(datetime.datetime.strptime("July 26, 2024", "%B %d, %Y"))