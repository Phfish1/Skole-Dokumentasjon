def hilsen():
    navn = input("Navn: ")
    bosted = input("Bosted: ")

    print(f"Hei {navn}, du er fra {bosted}")
    return

for i in range(0, 3):
    hilsen()