name_list = []
first_name = str(input("Name: "))
name_list.append(first_name)

final_name_string = "Welcome "

another_name_loop_choice = input("Another name [N/y]? ").lower()

def name_adder(another_name_loop_choice):
    final_name_string = "Welcome "
    ### Loop for adding more names
    while another_name_loop_choice == "y":
        current_name = str(input("Name: "))
        name_list.append(current_name)

        another_name_loop_choice = input("Another name [N/y]? ")


    ### add names to "final_name_string"

    for name in name_list:
        final_name_string += name
        if name != name_list[len(name_list) - 1]:
            final_name_string += " og "

    return final_name_string



if another_name_loop_choice == "y":
    final_name_string = name_adder("y")
else:
    final_name_string += first_name

print(f"{final_name_string}")