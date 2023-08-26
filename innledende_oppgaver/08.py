def print_handle_liste(liste):
    for item in liste:
        print(f"{item}: {handle_liste[item]}kr")

handle_liste = {
    "melk": 14.90,
    "brød": 24.90,
    "yoghurt": 12.90,
    "pizza": 39.90
}

#print_handle_liste(handle_liste)

handle_liste["ost"] = 60.90
handle_liste["salat"] = 34.90

print_handle_liste(handle_liste)