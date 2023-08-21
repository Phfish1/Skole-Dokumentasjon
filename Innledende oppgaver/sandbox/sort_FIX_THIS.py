unsorted_list = [5, 2, 8, 3, 1]

def working(unsorted_list):
    
    # Bubble sort implementation
    for i in range(len(unsorted_list)-1):
        for j in range(len(unsorted_list)-i-1):
            if unsorted_list[j] > unsorted_list[j+1]:
                temp = unsorted_list[j]
                unsorted_list[j] = unsorted_list[j+1]
                unsorted_list[j+1] = temp
    # Print the sorted list
    return unsorted_list # Output: [1, 2, 3, 5, 8]


#print(working(unsorted_list))


def sort(list):
    for i in range(len(list) - 1):
        
        for j in range(len(list) -i -1):
            print(list[j])



print(sort(unsorted_list))