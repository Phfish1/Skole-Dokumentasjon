numbers = [8, 3, 5, 10, 7]

def bubble_sort(unsorted_list):
    index_length = len(unsorted_list) - 1
    is_sorted = False

    while not is_sorted:
        is_sorted = True
        for i in range(0, index_length):
            if unsorted_list[i] > unsorted_list[i+1]:
                sorted = False
                unsorted_list[i], unsorted_list[i+1] = unsorted_list[i+1], unsorted_list[i]

    return unsorted_list


sorted_numbers = bubble_sort(numbers)
print(sorted_numbers)

