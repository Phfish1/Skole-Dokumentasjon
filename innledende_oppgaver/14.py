def add_together(string1, string2):
    return f"{string1}{string2}"




user_choice_message = f"[i]: Insert strings\n[p]: Print Strings\n[e]: Exit Program"
running_program = True
my_string = ""

print("Welcome")
print(user_choice_message)
while running_program:
    try:
        user_choice = str(input("Choose option: ")).lower()

        if user_choice == "i":
            string1 = str(input("Enter String-1: "))
            string2 = str(input("Enter String-2: "))
            
            my_string += add_together(string1, string2)
        elif user_choice == "p":
            print(my_string)
        elif user_choice == "e":
            print("Exiting Program...")
            running_program = False
        else:
            raise ValueError

    except KeyboardInterrupt:
        print("\nCTRL-C Detected, exiting program")
        quit()
    except:
        print("Please specify a valid option:")
        print(user_choice_message)

print("Goodbye :)")