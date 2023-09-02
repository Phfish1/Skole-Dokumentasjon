import random

def random_password_list(amount_of_passwords):
    availible_characters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ123456789!?#$-'*\\%&/()="
    password_list = []

    for i in range(0, amount_of_passwords):
        password_length = 10 # MAKE RANDOMINT
        current_password = ""

        for j in range(0, password_length):
            random_character = random.choice(availible_characters)
            current_password += random_character

        password_list.append(current_password)

    return password_list