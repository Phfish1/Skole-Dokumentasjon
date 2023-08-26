def homemade_splitter(string, first_split):

    #if first_split == "\n":
    #    print("hi")

    for i in range(0, len(string) - len(first_split)):


        formated_string = ""

        current_section = ""
        if i % len(first_split) or i == 0:
            for j in range(0, len(first_split)):
                current_section += string[j + i]
        print(current_section)
    
        
        '''
        current_char = string[i]
        current_section = ""
        for i in range(0, len(first_split)):
            current_section += string[i]

        print(current_section)
        if first_split in current_section:
            print("--------------------True")
        '''
        

        #if " " in checking_section:
        #    print(checking_section)

        #print(string[i])
        #for j in range(0, len(checking_section)):
            #print(checking_section[j] == first_split)
            #print(checking_section[j])
        #    if checking_section[j] == first_split:
        #        print(string)




sales_file = open("sandbox/salesnumbers.txt", "r")
sales_lines = sales_file.readlines()


for i in range(0, len(sales_lines)):
    curent_line = sales_lines[i]

    #for j in range(0, len(curent_line)):
    homemade_splitter(curent_line, "rse")

    #print(curent_line)