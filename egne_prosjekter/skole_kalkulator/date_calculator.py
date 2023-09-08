import datetime
import json
import schoolday_handler

def hours_left_of_day(hours_db):
    #now_datetime = datetime.datetime.now().replace(microsecond=0)
    now_datetime = datetime.datetime(2023, 9, 8, 8, 30, 0) ### TESTING BLOCK

    current_weekday = datetime.datetime.strftime(now_datetime, "%A").lower()

    try:
        school_end_time = hours_db[current_weekday]["time_delta"][1]
        school_end_datetime = datetime.datetime(now_datetime.year, now_datetime.month, now_datetime.day, school_end_time.hour, school_end_time.minute) 
    except:
        print(f"Today is {current_weekday}, not a school day :)")
        return datetime.timedelta(0,0,0)

    if school_end_datetime - now_datetime < datetime.timedelta(0,0,0):
        print(f"Time is {now_datetime.time()}, You are no longer at school :)")
        return datetime.timedelta(0,0,0) # Might also just return "-Day Value"
    else:
        return school_end_datetime - now_datetime
    

def days_left_of_semester(dates_db):
    now_datetime = datetime.datetime.now().replace(microsecond=0)
    #now_datetime = datetime.datetime(2023, 8 ,17) ### TEST BLOCK 

    school_end_datetime = dates_db["skoleslutt"]

    time_left_of_semester = school_end_datetime - now_datetime + datetime.timedelta(1) ### + timedelta 1 because last day of school is 21.st not 20.th

    return time_left_of_semester


def days_left_of_school(dates_db):
    now_datetime = datetime.datetime.now().replace(microsecond=0)
    #now_datetime = datetime.datetime(2023, 8, 17, 0, 0, 1) ### TEST BLOCK (CORRECT ANSWER: 189 days, 23:59:59)

    semester_delta = days_left_of_semester(dates_db)
    
    schooldays_left = 0

    ### Loop through each day in the school year starting at tomorow through last school day
    for day in range(1, semester_delta.days + 1): ### +1 so it takes with last school day, range(1) so it does not count with today, since only hours left
        current_day = now_datetime.replace(hour=0, minute=0, second=0) + datetime.timedelta(day)

        if schoolday_handler.is_schoolday(current_day, dates_db):
            schooldays_left += 1
        else:
            pass


    ### This gets the hours/minutes/seconds remaining of the current day. Probbarly a better way to do it but here i am...
    till_tomorow_delta = (now_datetime.replace(hour=0, minute=0, second=0) + datetime.timedelta(1)) - now_datetime
    till_tomorow_datetime = now_datetime.replace(hour=0, minute=0, second=0) + till_tomorow_delta


    ### Return amount of schooldays left and the time left of the current day
    return datetime.timedelta(days=schooldays_left, hours=till_tomorow_datetime.hour, minutes=till_tomorow_datetime.minute, seconds=till_tomorow_datetime.second)