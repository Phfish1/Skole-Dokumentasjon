editing_plan = True

while editing_plan:
    try:
        edit_choice = input("Which Holiday would you like to edit? [0-5]: ")
        edit_choice = int(edit_choice)

        if edit_choice < 0 or edit_choice > 5:
            print("Please select between 0 and 5")
        else:
            # Perform the editing based on the user's choice
            pass
            # Your editing logic here

    except KeyboardInterrupt:
        print("\nCtrl-C Detected, Exiting process")
        break

    except ValueError:
        print("Invalid input. Please enter a number between 0 and 5.")

    except Exception as e:
        print("An error occurred:", str(e))  # Print the exception details for debugging
