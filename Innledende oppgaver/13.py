
class HolidayPlan():
    def __init__(self):

        self.holiday_length = 1

        self.destinations = self.selector([], 0)
        self.departures = self.selector([], 1)
        self.clothes = self.selector([], 2)

        self.holiday_plan = self.uppdate_holiday_plan()


    def uppdate_holiday_plan(self):
        holiday_plan = {}
        for i in range(0, self.holiday_length):
            holiday_plan[f"holiday_{i}"] = {
                "destination": self.destinations[i],
                "departure": self.departures[i],
                "clothes": self.clothes[i]
            }
        return holiday_plan

    def selector(self, selected_array, selector_number):

        if selector_number == 0: # Destination
            for i in range(0, self.holiday_length):
                selected_array.append(input(f"Choose Destination: "))
                #selected_array.append("Norway")

        elif selector_number == 1: # Departure
            for i in range(0, self.holiday_length):
                date_array = []
                for j in range(0, 3):
                    j_index_to_text = {
                        0: "Day",
                        1: "Month",
                        2: "Year"
                    }
                    #selected_array.append(1)
                    date_array.append(int(input(f"Choose {j_index_to_text[j]}: ")))
                    date_array.append(1)
                selected_array.append(date_array)

        elif selector_number == 2: # Clothes
            for i in range(0, self.holiday_length):
                clothes_array = []
                for j in range(0, 3):
                    clothes_array.append("T-Shirt")
                    clothes_array.append(input(f"Select Clothing number {j}: "))
                selected_array.append(clothes_array)

        return selected_array


    def edit_plan(self):

        for i in range(0, len(self.holiday_plan)): # Displays editing options
            current_holiday_plan = self.holiday_plan[list(self.holiday_plan.keys())[i]] 

            print(f'{"{"} {i + 1} {"}"}: {current_holiday_plan["destination"]} | {current_holiday_plan["departure"]} | {current_holiday_plan["clothes"]}')
            
        while True: # Handles input and errors
            try:
                edit_choice = int(input(f"Which Holiday would you like to edit? [ 1 - {self.holiday_length} ]: ")) - 1
                #edit_choice = 0
                if edit_choice not in range(0, self.holiday_length):
                    raise ValueError
                else:
                    break
            except KeyboardInterrupt:
                print("\nCtrl-C Detected, Exiting process")
                quit()
            except:
                print(f"Please select between 1 - {self.holiday_length}")

        editing_holiday_entry = self.holiday_plan[list(self.holiday_plan.keys())[edit_choice - 1]] # might not be needed
        
        while True:
            print("Select which property to edit:")
            print(f'{"{"} 1 {"}"}: Destination')
            print(f'{"{"} 2 {"}"}: Departure Time')
            print(f'{"{"} 3 {"}"}: Clothes')
            try:
                selector_number = int(input("Select: ")) - 1 
                #selector_number = 0
                if selector_number not in range(0, 3):
                    raise ValueError
                else:
                    break
            except KeyboardInterrupt:
                print("\nCtrl-C Detected, Exiting process")
                quit()
            except:
                print("------\nPlease Select a Value Between 1-3\n------")



        ### The code bellow did not work, because it assigned the value only to the self.holiday.plan, NOT the other selfs
        #self.holiday_plan[list(self.holiday_plan.keys())[edit_choice]][self.selector_number_to_property_name(selector_number)] = self.selector([], selector_number) 
        
        if selector_number == 0:
            self.destinations[edit_choice] = self.selector([], selector_number)[0]
        elif selector_number == 1:
            self.departures[edit_choice] = self.selector([], selector_number)[0]
        elif selector_number == 2:
            self.clothes[edit_choice] = self.selector([], selector_number)[0]
        
        self.holiday_plan = self.uppdate_holiday_plan()

        #print(self.[self.selector_number_to_property_name(selector_number)])

    


        #self.holiday_plan = self.uppdate_holiday_plan()

        #for i in range(0, len(self.holiday_plan)): # Useless right now! 
        #    editing_holiday_entry = self.holiday_plan[list(self.holiday_plan.keys())[edit_choice]]
        #    print(editing_holiday_entry)
    
    def selector_number_to_property_name(self, selector_number):
        number_to_name_dict = {
            0: "destinations",
            1: "departure",
            2: "clothes"
        }
        selector_name = number_to_name_dict[selector_number]

        return selector_name

    
    

first_holiday = HolidayPlan()

first_holiday.edit_plan()
print(first_holiday.holiday_plan)
#print(first_holiday.destinations)



