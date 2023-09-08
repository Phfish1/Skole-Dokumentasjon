import datetime

def base_to_date_converter(db_base):
    db_dates = db_base["dates"]
    date_format = "%Y-%m-%d"

    for key in db_dates:

        ### Handles the arrays
        if isinstance(db_dates[key], list):
            for i in range(0, len(db_dates[key])):
                db_dates[key][i] = datetime.datetime.strptime(db_dates[key][i], date_format)
                #print(datetime.datetime.strptime(item, date_format))
        else:

            try:
                db_dates[key] = datetime.datetime.strptime(db_dates[key], date_format)

            except:
                print("dates.json has an invalid format")

    return db_dates
