### This file should handle all the holidays, weekdays and vecations. etc
import datetime

def is_schoolday(day, dates_db):

    if is_weekend(day):
        return False
    
    if is_planleggingsdag(day, dates_db):
        return False

    if is_holiday(day, dates_db):
        return False
    
    spring_break = dates_db["høstferie"]
    christmas_break = dates_db["juleferie"]
    vinter_break = dates_db["vinterferie"]
    easter_break = dates_db["påskeferie"]

    ### Vacations
    if is_vacation(day, dates_db["høstferie"]):
        return False

    if is_vacation(day, dates_db["juleferie"]):
        return False

    if is_vacation(day, dates_db["vinterferie"]):
        return False
    
    if is_vacation(day, dates_db["påskeferie"]):
        return False


    return True ### If all of above is False


def is_weekend(day):
    if day.isoweekday() == 6 or day.isoweekday() == 7:
        return True
  
    return False


def is_planleggingsdag(day, dates_db):
    planleggingsdager = dates_db["planleggingsdager"]

    for planleggingsdag in planleggingsdager:
        if day == planleggingsdag:
            return True

    return False


def is_holiday(day, dates_db):
    holidays = dates_db["helligdager"]
    for holiday in holidays:
        if day == holiday:
            return True

    return False


def is_vacation(day, vacation):
    ### Takes lenght of vacation and loops through start day through last vacation day to check if current day matches vacation day
    vacation_length = vacation[1] - vacation[0]

    for i in range(0, vacation_length.days + 1):
        if day == vacation[0] + datetime.timedelta(i):
            return True
        
    return False
