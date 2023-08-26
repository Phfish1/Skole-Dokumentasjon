class Person():
    def __init__(self, name, age):
        self.name = name
        self.age = age

def inngang_melding(person):
    name = person.name
    price = bilet_pris_kalkulator(person.age)
    return f"Welcome {name}, billet pris blir: {price}kr"

def bilet_pris_kalkulator(age):
    if age <= 17:
        return 30
    elif age >= 63:
        return 35
    else:
        return 50

person1 = Person("Philip", 15)
person2 = Person("Arne", 31)
person3 = Person("Olga", 63)

print(inngang_melding(person1))
print(inngang_melding(person2))
print(inngang_melding(person3))