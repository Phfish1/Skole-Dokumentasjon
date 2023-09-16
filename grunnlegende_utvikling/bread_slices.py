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

    ## How to you find (2) The amount of family members not getting another bread
    ## Find 6, the amounts of bread given out


    #leftover_bread = len(bread_list) % family_size # Amount of bread left that does not go up
    #bread_given_out = len(bread_list) - leftover_bread
    #amount_net_getting_another_bread = bread_given_out - leftover_bread
    #ensured_bread_amount = len(bread_list) // family_size



    bread_left = len(bread_list)


    if bread_left > len(family_list):
        # Gi en brød til hver
        bread_left -= len(family_list)
    
    while bread_left > 0:
        
        print(f"bread fiven to family member {family_list[random.randint(0, len(family_list) - 1)]}") 
        # Random does not work, DIVIDED needs to still be fair
        # Maybe a FOR loop!
        bread_left -= 1
        




  

# 10 / 6 = 1.6
# 5 4

bread = "Whole wheat"
bread_slices = 10

family_list = [FamilyMember("Åse"), {}, {}, {}, {}, {}]  
pålegg_liste = [Pålegg("leverpostei", "knife"), Pålegg("cheese", "ostehøvel"), Pålegg("salami", "hand"), Pålegg("egg", "egg_slicer").boil()]

finished_bread_list = put_pålegg_on_bread(bread, bread_slices, pålegg_liste)

divide_bread_on_family(finished_bread_list, family_list)



