"""ООП - Объектно-ориентированное программирование"""

class Car:
    def __init__(self,wheel,motor,body): #это конструктор __init__
        self.wheel=wheel
        self.motor=motor
        self.body=body

        self.bak=20
        self.is_start=False

    def info(self):
        print(f"Motor - {self.motor}, Wheels - {self.wheel}, Body - {self.body}")

    def start(self):
        if self.bak >0:
            self.is_start=True
            print("Car is on")
        else:
            print("Car is off")

    def stop(self):
        self.is_start=False
        print("Car is off")

    def drive(self,city):
        if self.is_start==True:
            print(f'The car is on the way to {city}')
        else:
            print("The car isn`t on the way")

car=Car("R20","V6","Khan")
car.info()
car.start()
car.drive("Dubai")


class Book:
    def __init__(self,author,name,year):
        self.author=author
        self.name=name
        self.year=year

    def info(self):
        return f"Author of the book - {self.author}, Name of the book - {self.name}, Year of the book - {self.year}"
    
book=Book('A.S.Pushkin','Evgeniy Onegin',1889)
print(book.info())


"""Наследование"""

class Animal:
    def __init__(self,name,color,year,type):
        self.name=name
        self.color=color
        self.year=year
        self.type=type

    def info(self):
        print(f"Name of the animal - {self.name}, Color of the animal - {self.color}, Age of the animel - {self.year}, Type of the animal - {self.type}")

class Cat(Animal):
    def __init__(self, name, color, year, type):
        super().__init__(name, color, year, type)
        # Animal().__init__(name,year)

    def info(self):
        return super().info()
    
animal=Animal("Cat","Orange",40,"s22")
animal.info()

cat=Cat("Vaska","Black",18,"Oshskiy")
cat.info()