#character_space = 3
inputed_spliting_character = "This"

inputed_main_string = f"Hello This string should be split up, with character space "

### Yea no this code is not gonna work ;( | But it was a lot of good ideas and i learned a lot :)
def homemande_splitter(main_string, spliting_character):
    spliting_char_length = len(spliting_character)

    section_length = 0
    for i in range(0, len(main_string) - spliting_char_length):

        if section_length + spliting_char_length <= len(main_string):
            section_string = ""
            for j in range(0, spliting_char_length):
                section_string += main_string[section_length + j]
            print(section_string)

            section_length += spliting_char_length

        elif len(main_string) - section_length == 0: # Stops when done
            break

        else: # Handles leftovers

            leftover_section_length = len(main_string) - section_length

            leftover_string = ""
            for j in range(section_length, len(main_string)):
                
                leftover_string += main_string[j]

            print(leftover_string)

        
homemande_splitter(inputed_main_string, inputed_spliting_character)

#print(main_string[0], main_string[0 + 1], main_string[0 + 2])
#print(main_string[3], main_string[3 + 1], main_string[3 + 2])