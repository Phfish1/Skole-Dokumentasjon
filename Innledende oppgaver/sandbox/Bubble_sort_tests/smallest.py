numbers = [9, 2, 4, 5, 2, 4, 10, 8, 1, 3]


def get_smallest(numbers_array):
    for i in range(0, len(numbers_array)):
        checking_number = numbers_array[i]

        for j in range(0, len(numbers_array)):
            current_number = numbers_array[j]

            if checking_number > current_number:
                checking_number = current_number

    return checking_number

smallest = get_smallest(numbers)
print(smallest)