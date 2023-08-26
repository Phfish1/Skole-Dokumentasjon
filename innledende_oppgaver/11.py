def sum(tall1, tall2):
    return int(tall1) + int(tall2)

def character_counter(character, string):
    character_count = 0

    for i in range(len(string)):
        if string[i] == character:
            character_count += 1

    return character_count

print(sum(1, 3))
print(sum(50, 50))

#string_input = str(input("Enter string: ")).lower().trim()
#character_input = input("Enter single character: ").lower().trim()

string_input = "Pizza"
character_input = "z"
character_count = character_counter(character_input, string_input)

print(f"'{character_input}' was present '{character_count}' times in '{string_input}'")
