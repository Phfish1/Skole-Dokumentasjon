def sum(array):
    array_sum = 0
    for number in array:
        array_sum += number
    return array_sum

def largest(array):
    current_number = 0
    for number in array:
        if number > current_number:
            current_number = number
            
    return current_number


### Large COMMENT :)), reasons why not delete = LARGE
# Tried making a function that finds smallest item in array
#def smallest(array): ### ToDo: Understand wtf you just built, why cant you block 0 the easy way. (I Refuse to use "EZ" built in python functions)
    ### Code needs uppdate, jank af
#    number = 0
    ### Removes 0
#    for i in range(0, len(array)):
#        if array[i] == 0:
#            array.pop(i)
#            break

    ### It just works ♫
#    for i in range(0, len(array)):
#        number = array[i]

#        for j in range(0, len(array)):
#            comparing_number = array[j] 

#            if number > comparing_number: ### Scary stuff... "Run in debugger"!
#                number = comparing_number
#
#    return number

def smallest(items): ### Now this is code i actually understand :), not just bullshited together
    highest_number = largest(items)

    for i in range(0, len(items) -1):
        current_item = items[i]

        if current_item < highest_number and current_item != 0:
            highest_number = current_item

    return highest_number
   #return current_item


def sorted_list(items):
    for i in range(0, len(items)):
        for j in range(0, len(items) - 1 - i):
            current_item = items[j]
            next_item = items[j + 1]

            if current_item > next_item:
                items[j], items[j+1] = items[j+1], items[j]

    return items
    

user_number_input = 1
guesed_numbers = []
#guesed_numbers = [9, 2, 4, 5, 2, 4, 10, 8, 0]

while user_number_input != 0:
    try:
        user_number_input = int(input("Choose ^~tHe RiGhT~^ Number: "))
    except ValueError:
        print("Please specify a number")
    else:
        guesed_numbers.append(user_number_input)

### User messages
print(guesed_numbers)
print(f"{sorted_list(guesed_numbers)}")
print(f"You guessed {len(guesed_numbers)} times, and got right the {len(guesed_numbers)}th time")
print(f"Sum: {sum(guesed_numbers)}")
print(f"Largest guess was: {largest(guesed_numbers)}")
print(f"Smallest guess was: {smallest(guesed_numbers)}")
