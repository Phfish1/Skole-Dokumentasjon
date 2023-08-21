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

def smallest(array):    
    return

    

user_number_input = 1
guesed_numbers = [9, 2, 4, 5, 2, 4, 10, 8, 0]

#while user_number_input != 0:
#    try:
#        user_number_input = int(input("Choose ^~tHe RiGhT~^ Number: "))
#    except ValueError:
#        print("Please specify a number")
#    else:
#        guesed_numbers.append(user_number_input)

### User messages
print(guesed_numbers)
print(f"You guessed {len(guesed_numbers)} times, and got right the {len(guesed_numbers)}th time")
print(f"Sum: {sum(guesed_numbers)}")
print(f"Largest guess was: {largest(guesed_numbers)}")
print(f"Smallest guess was: {smallest(guesed_numbers)}")