# Sample project for GenAI bootcamp on topic : Inheritance 
# Vehicle is parent class and Car is subclass
class Vehicle:
    def __init__(self, brand , year):
        self.brand = brand
        self.year = year

    def display_details(self):
        print(f"brand of the car : {self.brand}")
        print(f"Manufacturing year of the car : {self.year}")

class Car(Vehicle):
    def __init__(self, brand, year,fuel_type):
        super().__init__(brand, year)
        self.fuel_type = fuel_type

    def display_details(self):
        super().display_details()
        print(f"fule type of the car : {self.fuel_type}")

vehicle = Vehicle("BMW","2026")
vehicle.display_details()

car = Car("Mahindra","2023","Petro")
car.display_details()
