
class Date:
    
    def __init__(self, day, month, year):

        self.day = day
        self.month = month
        self.year = year

        month_name = self.month_id_to_name()

        if month > 12 or day > 31:
            raise ValueError(f"Invalid Days or Month specified: Max 12 months, Max 31 Days")

        ### Checks if days align with months; "30 days", { 28 | 29 } Days -> based on leap years
        if month == 4 or month == 6 or month == 9 or month == 11:
            if day > 30:
                raise ValueError(f"Invalid days specified: {month_name} has '30 Days'")

        ### check if leap year, for February
        if month == 2:

            if self.is_leap_year() and day > 29:
                raise ValueError(f"invalid month specified: {month_name} has '29 Days' in '{year}")

            elif not self.is_leap_year() and day > 28:
                raise ValueError(f"Invalid days specified: {month_name} has '28 Days' in '{year}'")


        self.date = [day, month, year]

    
    def is_leap_year(self):
        if self.year % 4 == 0 and self.year % 100 != 0 or self.year % 400 == 0:
            return True
        else:
            return False
        
    def month_id_to_name(self):
        month_id_to_names_dict = {
            1: "Januar",
            2: "Februar",
            3: "Mars",
            4: "April",
            5: "Mai",
            6: "Juny",
            7: "Juli",
            8: "August",
            9: "September",
            10: "Oktober",
            11: "November",
            12: "Desember"
        }

        for month in month_id_to_names_dict:
            if month == self.month:
                month_name = month_id_to_names_dict[month]
                return month_name
            
    def format_date(self):
        return f"{self.day}/{self.month}/{self.year}"
    

def greatest_date(date1, date2):


    for i in range(0, len(date1.date)): # Asign the 0 -to- date.length on to "i"
        latest_date1_item = date1.date[len(date1.date) - i - 1] ### Reverses array
        latest_date2_item = date2.date[len(date1.date) - i - 1]

        ### Checks each date item up against each other, "2024 VS 2023...". [Returns highest date]
        if latest_date1_item > latest_date2_item:
            print(f"{latest_date1_item} is higher than {latest_date2_item}")
            return date1
        elif latest_date2_item > latest_date1_item:
            print(f"{latest_date2_item} is higher than {latest_date1_item}")
            return date2

    return date1 #Returns date_1 if both dates are equal



date_1 = Date(22, 12, 2024)
date_2 = Date(29, 12, 2024)

date_1_formated = date_1.format_date()
print(date_1_formated)

date1_vs_date2_result = greatest_date(date_1, date_2)
print(date1_vs_date2_result.date)
print(date1_vs_date2_result.format_date())

