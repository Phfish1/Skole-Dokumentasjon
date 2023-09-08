import datetime

def base_to_date_converter(db_base):
    db_dates = db_base["dates"]
    date_format = "%Y-%m-%d"

    for key in db_dates:

        ### Handles the arrays
        if isinstance(db_dates[key], list):
            for i in range(0, len(db_dates[key])):
                db_dates[key][i] = datetime.datetime.strptime(db_dates[key][i], date_format)
        else:

            try:
                db_dates[key] = datetime.datetime.strptime(db_dates[key], date_format)

            except:
                print("dates.json has an invalid format")

    return db_dates

def base_to_hour_converter(db_base):
    db_hours = db_base["timeplan"]["mailandvgs"]["2it"]
    hour_format = "%H:%M"
    
    for day in db_hours:
        ### Need to first convert str to datetime, then datetime to time...
        start_time = datetime.datetime.strptime(db_hours[day]["time_delta"][0], hour_format)
        end_time = datetime.datetime.strptime(db_hours[day]["time_delta"][1], hour_format)
   
        db_hours[day]["time_delta"][0] = datetime.time(start_time.hour, start_time.minute, start_time.second)
        db_hours[day]["time_delta"][1] = datetime.time(end_time.hour, end_time.minute, end_time.second)
    
    return db_hours

