numbers = [1, 10, 6, 3, 12, 7, 2, 11, 8]

            ### (for nested j: LOOP) 
            # Minus 1 to not get index error at last item, 
            # Minus "i" So we dont double check the numbers on the "right" side of the list, 
            # we already know those are the highest

def bubble_sort(items):
    for i in range(0, len(items)):
        
        for j in range(0, len(items) - 1): 
            current_item = items[j]
            next_item = items[j + 1]

            if current_item > next_item:
                items[j], items[j + 1] = items[j + 1], items[j]

    return items


sorted_list = bubble_sort(numbers)
print(sorted_list)