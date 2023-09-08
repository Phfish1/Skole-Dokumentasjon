import json
import datetime
import date_handler

def get_db_base(municipality, years):
    dates_db_file = open("egne_prosjekter/skole_kalkulator/dates.json")
    dates_db = json.load(dates_db_file)

    db_base = dates_db[municipality][years]
    return db_base


viken_db_base = get_db_base("viken", "2023-2024")
viken_dates = date_handler.base_to_date_converter(viken_db_base)

for key in viken_dates:
    print(viken_dates[key])

