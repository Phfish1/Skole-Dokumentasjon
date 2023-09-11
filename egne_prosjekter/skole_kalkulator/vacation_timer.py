import datetime
import schoolday_handler
import date_calculator

#import main

### Count down to vacation or Holidays
def time_till_vacation(now, vacation):
    now_datetime = now.replace(microsecond=0)
    till_vacation = vacation[0] - now_datetime

    return till_vacation + datetime.timedelta(1)
    #return till_vacation

def schooldays_till_vacation(now, vacation, dates_db, hours_db):
    now_datetime = now.replace(microsecond=0)
    days_till_vacation = time_till_vacation(now, vacation).days

    schooldays_left = 0
    #for day in range(1, days_till_vacation + 1):
    for day in range(1, days_till_vacation): ### POTENTIAL CHANGE LINKED TO time_till_vacation | return till_vacation + datetime.timedelta(1)
        current_day = now_datetime.replace(hour=0, minute=0, second=0) + datetime.timedelta(day)

        if schoolday_handler.is_schoolday(current_day, dates_db):
            schooldays_left += 1

    
    time_left_of_schoolday = date_calculator.hours_left_of_day(now, hours_db, dates_db)
    till_tomorow_datetime = now_datetime = datetime.datetime.now().replace(hour=(time_left_of_schoolday.seconds // 60 // 60), minute=( (time_left_of_schoolday.seconds // 60) % 60 ), second=(time_left_of_schoolday.seconds % 60), microsecond=0)

    return datetime.timedelta(days=schooldays_left, hours=till_tomorow_datetime.hour, minutes=till_tomorow_datetime.minute, seconds=till_tomorow_datetime.second)


