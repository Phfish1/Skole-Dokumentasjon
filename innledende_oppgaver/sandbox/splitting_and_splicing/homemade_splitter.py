inputed_splitting_character = "Hello"
inputed_main_string = "Philip Hello Bear"

### Goal 1. Find out how to check if split_char is in main_str 
# Check split_char VS every single main_str index 

def homemade_splitter(main_string, splitting_character):
    for i in range(0, len(main_string)):
        
        current_checking_string = ""
        for j in range(0, len(splitting_character)):
            if i + j < len(main_string):
                current_checking_string += main_string[i + j]
    

        if current_checking_string == splitting_character:
            start_of_split = i
            end_of_split = i + len(splitting_character)

            ### EZ GAME :)
            first_string = homemade_slicer(main_string, 0, start_of_split) #first_string = main_string[0: start_of_split]
            last_string = homemade_slicer(main_string, end_of_split, len(main_string)) #last_string = main_string[end_of_split: len(main_string)]

            return [first_string, last_string]


def homemade_slicer(main_string, slice_start, slice_end):

    sliced_string = ""
    for i in range(0, len(main_string)):
        if i >= slice_start and i < slice_end:
            sliced_string += main_string[i]

    return sliced_string


### [ UNCOMMENT THESE TO TEST! ]
#splitted_string = homemade_splitter(inputed_main_string, inputed_splitting_character)
#print(splitted_string)