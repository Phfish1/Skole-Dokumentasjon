import datetime
import json
import schoolday_handler

import main

def hours_left_of_day(hours_db, dates_db):
    now_datetime = datetime.datetime.now().replace(microsecond=0)
    #now_datetime = datetime.datetime(2024, 6, 21, 8, 35, 29) ### TESTING BLOCK ALSO LINKED TO OTHER FUNCTIONS WITHIN FILE

    current_weekday = datetime.datetime.strftime(now_datetime, "%A").lower()

    if schoolday_handler.is_schoolday(now_datetime, dates_db):
        school_end_time = hours_db[current_weekday]["time_delta"][1]
        school_end_datetime = datetime.datetime(now_datetime.year, now_datetime.month, now_datetime.day, school_end_time.hour, school_end_time.minute)
    else:
        #print(ValueError(f"Today is {current_weekday}, not a school day :)"))
        return datetime.timedelta(0,0,0)

    if school_end_datetime - now_datetime < datetime.timedelta(0,0,0):
        #print(ValueError(f"Time is {now_datetime.time()}, You are no longer at school :)"))
        return datetime.timedelta(0,0,0) # Might also just return "-Day Value"
    else:
        return school_end_datetime - now_datetime
    

def days_left_of_semester(dates_db):
    now_datetime = datetime.datetime.now().replace(microsecond=0)
    #now_datetime = datetime.datetime(2024, 6 ,21) ### TEST BLOCK 
    #now_datetime = datetime.datetime(2023, 8 ,16) ### TEST BLOCK 

    school_end_datetime = dates_db["skoleslutt"]

    time_left_of_semester = school_end_datetime - now_datetime + datetime.timedelta(1) ### + timedelta 1 because last day of school is 21.st not 20.th

    return time_left_of_semester

def days_left_of_school(dates_db, hours_db):

    now_datetime = datetime.datetime.now().replace(microsecond=0)

    #now_datetime = datetime.datetime(2024, 6, 21, 0, 0, 1) ### TEST BLOCK (LINKED TO "now_datetime" IN "days_left_of_semester")
    #now_datetime = datetime.datetime(2023, 8, 16, 0, 0, 1) ### TEST BLOCK 

    semester_delta = days_left_of_semester(dates_db)

    schooldays_left = 0

    ### Loop through each day in the school year starting at tomorow through last school day
    for day in range(1, semester_delta.days + 1): ### +1 so it takes with last school day, range(1) so it does not count with today, since only hours left
        current_day = now_datetime.replace(hour=0, minute=0, second=0) + datetime.timedelta(day)

        if schoolday_handler.is_schoolday(current_day, dates_db):
            schooldays_left += 1
        else:
            pass



    ### Math here to convert seconds to hour minutes and seconds,
    time_left_of_schoolday = hours_left_of_day(hours_db, dates_db)
    till_tomorow_datetime = now_datetime = datetime.datetime.now().replace(hour=(time_left_of_schoolday.seconds // 60 // 60), minute=( (time_left_of_schoolday.seconds // 60) % 60 ), second=(time_left_of_schoolday.seconds % 60), microsecond=0)

    ### Return amount of schooldays left and the time left of the current day
    return datetime.timedelta(days=schooldays_left, hours=till_tomorow_datetime.hour, minutes=till_tomorow_datetime.minute, seconds=till_tomorow_datetime.second)