### The bubble sorting algerithm takes the largest item in the array and places it last.
# *Checks each item and its ascending item to decide if item should move upp or stay in place.


array = [5, 7, 3, 1]

for i in range(0, len(array)):

    for j in range(0, len(array) -i -1):
        current_number = array[j]
        next_number = array[j + 1]

        if current_number > next_number: # if current number is higher than next number
            array[j] = next_number # Switch places, AKA current number / higher number switches place with next number / lower number  
            array[j + 1] = current_number

print(array)