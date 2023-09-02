import json
import random

def random_name_list(amount_of_names):
    names_file = open("egne_prosjekter/scripts/name_and_passwords/popular_names_2021.json")
    json_names = json.load(names_file)

    ### Homemade {for} loop and {in} checker, Used to add UNIQUE RANDOM names to "used_names"
    used_names = []
    my_i = 0

    while my_i < amount_of_names:
        is_boy = bool(random.randint(0, 1))
        is_duplicate = False

        if is_boy:
            name = json_names["boys"][random.randint(0, 999)]
        else:
            name = json_names["girls"][random.randint(0, 999)]

        for i in range(0, len(used_names)):
            if used_names[i] == name:
                is_duplicate = True

        if not is_duplicate:
            used_names.append(name)
            my_i += 1

    return used_names