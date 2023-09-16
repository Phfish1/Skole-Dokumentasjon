##### Goal: make 10 bread slices to the entire family
### Documentation:
# Family of 6
# Whole weat bread
# 10 slices
# cheese
# leverpostei
# salami
# boiled egg
# can to boil egg
# knife
# egg slices

### Breaking down the problems:
# 10 slices of bread for 6 people
#   get bread, knife, ostehøvel, can and egg slicer
#       get pålegg
#           salami
#           cheese
#           leverpostei
#           boiled egg
#               use can to boil egg

### Ordering
# First get everything ready,
# Second get pålegg
# third get pålegg ready
# fourth use tools to spread påleg out on bread
# fifth serve

### Conditioning
# IF pålegg is egg then use can
# IF pålegg is cheese then use ostehøvel
# IF pålegg is salami use hand
# IF pålegg is leverpostei use knife

### Program flow
# Get bread and amount of bread slices
# Get pålegg
# Get tools
# IF pålegg == cheese THEN use ostehøvel

### Adding loops
# For every pålegg:
#   IF pålegg equals to cheese THEN:
#       Use ostehøvel

### ...

import random

class Pålegg():
    pålegg_tools = ["knife", "ostehøvel", "hand", "egg_slicer"]

    def __init__(self, name, tool):
        self.name = name

        if tool in self.pålegg_tools:
            self.tool = tool
        else:
            raise ValueError(f"Not a valid pålegg tool, SEE: {self.pålegg_tools}, consider adding a new tool with the update_påleg_tools() function")
        

    def update_påleg_tools(self):
        update_choice = ""

        while update_choice != "e":
            print("\n(e to exit)")
            print(f"{self.pålegg_tools}")

            update_choice = input("Add or subract an item: [a/s] ").lower()
        

            if update_choice == "s":
                subtracted_sucsesfully = False

                print("Choose wich one to Subtract:")
                
                for i in range(0, len(self.pålegg_tools)):
                    print(f"{i + 1} {self.pålegg_tools[i]}")
                
                while not subtracted_sucsesfully:
                    try:
                        subtract_choice = input(f"Select pålegg_type ({1}-{len(self.pålegg_tools)}): ").lower()

                        if subtract_choice == "e":
                            update_choice = "e" 
                            break
                        else:
                            subtract_choice = int(subtract_choice) - 1

                        self.pålegg_tools.pop(subtract_choice)
                        subtracted_sucsesfully = True

                    except KeyboardInterrupt:
                        break
                    except:
                        print("Invalid number" + "Press {e} to exit")
                    

            if update_choice == "a":
                print("Choose what type to append to pålegg pålegg_tools")
                new_pålegg_type = str(input("Type: ")).lower()
                self.pålegg_tools.append(new_pålegg_type)

            
            print(self.pålegg_tools)
    
    def boil(self):
        return Pålegg(f"boiled_{self.name}", self.tool)

class BreadWithPålegg():
    def __init__(self, bread, pållegg):
        self.pålegg = pållegg.name
        self.tool = pållegg.tool
        self.bread = bread

class FamilyMember():
    def __init__(self, name):
        self.name = name


def put_pålegg_on_bread(bread, bread_slices ,pålegg_liste):
    bread_with_pålegg = []

    for i in range(0, bread_slices):
        chosen_pålegg = pålegg_liste[random.randint(0, len(pålegg_liste) - 1)]
        
        bread_with_pålegg.append(BreadWithPålegg(bread, chosen_pålegg))

    return bread_with_pålegg

def divide_bread_on_family(bread_list, family_list):

    bread_to_family_member = {}

    family_size = len(family_list)
    
    for i in range(0, family_size):
        bread_to_family_member[family_list[i]] = []


    leftover = False

    while not leftover:
        if len(bread_list) >= family_size: # Give 1 bread each
            # Remove random bread based on family size

            for member in family_list:
                random_bread_index = random.randint(0, len(bread_list) - 1)
                bread_to_family_member[member].append(bread_list[random_bread_index])
                bread_list.pop(random_bread_index)
        else:
            leftover = True

    leftover_getters_list = []
    while len(bread_list) > 0 and leftover:
        
        
        random_family_member = family_list[random.randint(0, family_size - 1)]

        if random_family_member not in leftover_getters_list:
            random_bread_index = random.randint(0, len(bread_list) - 1)


            bread_to_family_member[random_family_member].append(bread_list[random_bread_index])

            leftover_getters_list.append(random_family_member)

            bread_list.pop(random_bread_index)

    return bread_to_family_member

        


    
        


bread = "Whole wheat"
bread_slices = 8

family_list = [FamilyMember("Pappa"), FamilyMember("Mamma"), FamilyMember("Aleksander"), FamilyMember("Philip"), FamilyMember("Sophie"), FamilyMember("Henrik")]  
pålegg_liste = [Pålegg("leverpostei", "knife"), Pålegg("cheese", "ostehøvel"), Pålegg("salami", "hand"), Pålegg("egg", "egg_slicer").boil()]

finished_bread_list = put_pålegg_on_bread(bread, bread_slices, pålegg_liste)

bread_to_family_member = divide_bread_on_family(finished_bread_list, family_list)

for item in bread_to_family_member:
    print(f"{item.name}:")

    for bread in bread_to_family_member[item]:
        print(f"( {item.name} ) takes the {'{'} {bread.bread} {'}'} Bread, and uses the {'{'} {bread.tool} {'}'} to put {'{'} {bread.pålegg} {'}'} on")

    print("")


