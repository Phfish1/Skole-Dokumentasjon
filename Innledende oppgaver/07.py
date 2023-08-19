numbers = [10, 20, 30, 40, 50]
numbers.append(60)

def addition(array):
    count = 0
    for item in array:
        count += item

    return count

def multiplication(array):
    product = 1
    for item in array:
        product = product * item

    return product


number_results = [addition(numbers), multiplication(numbers)]

numbers.extend(number_results)
print(numbers)

for i in range(0, 2):
    numbers.pop(len(numbers) - 1)

print(numbers)


name_list = []
for i in range(0, 2):
    name = str(input("Name: ")).lower()
    name_list.append(name)

print(name_list)

#if "Philip" in name_list:
#    print("Du husket meg")
#else:
#    print("Du husket meg ikke")

for i in range(0, len(name_list)):
    if "philip" == name_list[i]:
        print("Du husket meg")
        break
    elif len(name_list) - 1 == i:
        print("Du glemte meg ;(")
    