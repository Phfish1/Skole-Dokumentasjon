numbers = [8, 3, 5, 10, 7]

def bubble_sort(unordered_list):
    index_length = len(unordered_list)

    for i in range(0, index_length):
        #print(unordered_list[i])

        for j in range(0, index_length):
            if unordered_list[i] < unordered_list[j]:
                print(unordered_list[i], unordered_list[j])

                unordered_list[i], unordered_list[j] = unordered_list[j], unordered_list[i]

    return unordered_list


sorted_list = bubble_sort(numbers)
print(sorted_list)