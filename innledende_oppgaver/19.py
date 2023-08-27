class Motorcycle():
    def __init__(self, brand, registration_number, km_wheel):
        self.brand = brand
        self.registration_number = registration_number
        self.km_wheel = km_wheel

    def drive(self, km_to_drive):
        self.km_wheel += km_to_drive
        return self.km_wheel

    def get_status(self):
        return f"Brand: {self.brand},\nRegistered number: {self.registration_number},\nKilometers Traveled: {self.km_wheel}"

