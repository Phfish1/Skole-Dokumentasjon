class Beboer:
    def __init__(self, navn, matliste):
        self.navn = str(navn)
        
        self.måltider = {
                "frokost": matliste[0],
                "lunch": matliste[1],
                "middag": matliste[2],
        }

        self.matliste = eval(f'{"{"} "{self.navn}": {self.måltider}, {"}"}')

def nice_name(name): ### To next time, use the "capitalize()"" function
    new_name = ""
    for i in range(len(name)):
        if i == 0:
            new_name += name[i].upper()
        else:
            new_name += name[i]

    return new_name

def create_new_måltider(beboer): ### UPdate beboers måltider

    new_frokost = input("Frokost: ").lower().strip()
    new_lunch = input("Lunch: ").lower().strip()
    new_middag = input("Middag: ").lower().strip()

    mat_dictionary[beboer] = {"frokost": new_frokost, "lunch": new_lunch, "middag": new_middag}
    return mat_dictionary

mat_dictionary = {}

mat_dictionary.update(Beboer("philip", ["banan", "bacon", "pizza"]).matliste)
mat_dictionary.update(Beboer("island", ["isbjørn", "hval", "gress"]).matliste)
mat_dictionary.update(Beboer("banan", ["hånd", "arm", "overkropp"]).matliste)


print("Welcome")
beboer_choice = input("Velg din beboer: ").lower().strip()


#if beboer_choice in mat_dictionary: ### Could just use this but...
#    print("Ok")
#else:
#    print("hi is not here")


### Loops through mat_dictionary and checks if beboer is in mat_dictionary. Needed to convert mat_dictionary -> to keys then keys -> to list.
# Then if at the last beboer do elif. (might also work with "try" keyword)

for beboer in range(0, len(mat_dictionary)):
    if beboer_choice == list(mat_dictionary.keys())[beboer]:
        print("Just a second...\n----------------")
        print(f"{nice_name(beboer_choice)}'s food for today is as follow:")
        print(mat_dictionary[list(mat_dictionary.keys())[beboer]]) # Could just use beboer_choice for this specific instance 

        is_happy_input = input("Are you happy with that? [Y/n]: ").lower().strip()
        if is_happy_input == "n":
            create_new_måltider(beboer_choice)
            print(f"New foods for {nice_name(beboer_choice)}: {mat_dictionary[beboer_choice]}")
        break
    elif (beboer + 1) == len(mat_dictionary):
        print(f"Sorry '{beboer_choice}' is not here ;(")

# Janky code is gonna forget what this does tomorow Zzzzz













