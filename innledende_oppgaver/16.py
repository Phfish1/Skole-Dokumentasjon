def temperature_reader(temp_file, temp_list):
    temp_file_lines = temp_file.readlines()

    temp_list = []
    for i in range(0, len(temp_file_lines)):
        current_temperature = float(temp_file_lines[i].split("\n")[0])
        rounded_temperature = round(current_temperature)

        temp_list.append(rounded_temperature)

    return temp_list

def find_list_average(list):
    total = 0
    for i in range(0, len(list)):
        total += list[i]

    average = total / len(list)
    return round(average)

temp_file = open("sandbox/temperatures.txt", "r") # "r" = Read Only mode
temp_list = temperature_reader(temp_file, [])
list_average = find_list_average(temp_list)

print(list_average)