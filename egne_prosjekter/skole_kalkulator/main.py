import json
import datetime
import date_handler
import date_calculator
import vacation_timer

def get_db_base(municipality, years):
    dates_db_file = open("egne_prosjekter/skole_kalkulator/dates.json")
    dates_db = json.load(dates_db_file)

    db_base = dates_db[municipality][years]
    return db_base


def main():
    viken_db_base = get_db_base("viken", "2023-2024")
    viken_dates = date_handler.base_to_date_converter(viken_db_base)
    viken_hours = date_handler.base_to_hour_converter(viken_db_base, "mailandvgs", "2it")

    now = datetime.datetime.now()
    #now = datetime.datetime(2023, 9, 29, 10, 30, 15)

    days_left_of_semester = date_calculator.days_left_of_semester(now, viken_dates)
    hours_left_of_schoolday = date_calculator.hours_left_of_day(now, viken_hours, viken_dates)
    schooldays_left = date_calculator.days_left_of_school(now, viken_dates, viken_hours)

    days_till_springbreak = vacation_timer.time_till_vacation(now, viken_dates["høstferie"])
    schooldays_till_springbreak = vacation_timer.schooldays_till_vacation(now, viken_dates["høstferie"], viken_dates, viken_hours)

    print(days_till_springbreak)
    print(schooldays_till_springbreak)

    print()
    
    print(days_left_of_semester)
    print(hours_left_of_schoolday)
    print(schooldays_left)
main()
