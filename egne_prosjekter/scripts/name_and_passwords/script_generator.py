import json
import random
from random_name_list import random_name_list
from random_password_list import random_password_list

def script_generator(desired_line):
    script_file = open("egne_prosjekter/scripts/name_and_passwords/output_script", "w")

    script_length = 10
    name_list = random_name_list(script_length)
    password_list = random_password_list(script_length)

    ### MAKE PYTHON CREATE A FILE
    for i in range(0, script_length):

        line_format_map = {
            "name": name_list[i], 
            "password": password_list[i]
        }

        new_line = desired_line.format_map(line_format_map)

        script_file.write(f"{new_line}\n")
