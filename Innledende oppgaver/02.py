def brus_input(choice):
    if choice == "yes":
        print("Her er en brus")
    elif choice == "no":
        print("Skuffet ;(")


choice = str(input("YES OR NO! ")).lower()

### Check if input is valid
if choice == "yes" or choice == "no":
    brus_input(choice)
else:
    print("Huh ???!?!??!, tf")