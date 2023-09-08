import json
import datetime
import date_handler
import date_calculator

def get_db_base(municipality, years):
    dates_db_file = open("egne_prosjekter/skole_kalkulator/dates.json")
    dates_db = json.load(dates_db_file)

    db_base = dates_db[municipality][years]
    return db_base


def main():
    viken_db_base = get_db_base("viken", "2023-2024")
    viken_dates = date_handler.base_to_date_converter(viken_db_base)
    viken_hours = date_handler.base_to_hour_converter(viken_db_base)

    hours_left_of_schoolday = date_calculator.hours_left_of_day(viken_hours)
    days_left_of_semester = date_calculator.days_left_of_semester(viken_dates)
    schooldays_left = date_calculator.days_left_of_school(viken_dates)

    #print(days_left_of_semester)
    print(schooldays_left)
main()
