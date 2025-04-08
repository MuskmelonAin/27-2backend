class Vehicle:
    def __init__(self,brand,model,year):
        self.brand=brand
        self.model=model
        self.year=year

    def info(self):
        print(f"Brand of the vehicle: {self.brand}, model of the vehicle: {self.model}, year of the vehicle: {self.year}.")

vehicle=Vehicle("veh","meh",2009)
vehicle.info()



class Car(Vehicle):
    def __init__(self, brand, model, year,doors):
        super().__init__(brand, model, year)
        self.doors=doors

    def info(self):
        print(f"Brand of the car: {self.brand}, model of the car: {self.model}, year of the car: {self.year}, doors of the car: {self.doors}.")

    def start_engine(self):
        print(f"Двигатель машины {self.brand} {self.model} заведен")

kia=Car("KIA","Morning",2019,4)
kia.info()
kia.start_engine()




class Bike(Vehicle):
    def __init__(self, brand, model, year, type):
        super().__init__(brand, model, year)
        self.type=type

    def info(self):
        print(f"Brand of the bike: {self.brand}, model of the bike: {self.model}, year of the bike: {self.year}, type of the bike: {self.type}.")

    def start_engine(self):
        print(f"Двигатель мотоцикла {self.brand} {self.model} заведен")

bmw=Bike("BMW","R1200RS",2019,"спортивно-туристический")
bmw.info()
bmw.start_engine()