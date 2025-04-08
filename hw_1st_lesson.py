'''
Задание 1: Класс Person
Создайте класс Person, который будет описывать человека. У каждого человека должны быть следующие свойства:
имя (name)
возраст (age)
город проживания (city)
Добавьте метод introduce(self), который выводит:
python
Привет! Меня зовут {name}, мне {age} лет, я живу в городе {city}.
Создайте 2–3 объекта этого класса и вызовите метод introduce для каждого.
'''
class Person:
    def __init__(self,name,age,city):
        self.name=name
        self.age=age
        self.city=city
    
    def introduce(self):
        print(f"Привет! Меня зовут {self.name}, мне {self.age} лет, я живу в городе {self.city}.")

clara=Person('Клара',15,'Волгоград')
clara.introduce()

alia=Person('Алия',18,'Бишкек')
alia.introduce()

hanan=Person('Ханан',45,'Ар-Русайфа')
hanan.introduce()

'''
Задание 2: Класс Car
Создайте класс Car, у которого есть:
марка (brand)
модель (model)
год выпуска (year)
Добавьте метод info(self), который возвращает строку с информацией о машине:
python
Автомобиль: {brand} {model}, {year} года выпуска.
Добавьте метод is_old(self), который возвращает True, если машине больше 10 лет, иначе False.
'''
class Car:
    def __init__(self,brand,model,year):
        self.brand=brand
        self.model=model
        self.year=year

    def info(self):
        print(f"Автомобиль: {self.brand} {self.model}, {self.year} года выпуска.")

    def is_old(self):
        if self.year <= 2015:
            print(True)
        else:
            print(False)

toyota=Car('Toyota','Camry',2015)
toyota.info()
toyota.is_old()

kia=Car('KIA','Morning',2019)
kia.info()
kia.is_old()

'''
Задание 3: Класс BankAccount ⭐ (повышенной сложности)
Создайте класс BankAccount с атрибутами:
владелец счёта (owner)
баланс (balance, по умолчанию 0)
Добавьте методы:
deposit(amount) — пополнить счёт
withdraw(amount) — снять деньги (если хватает средств)
show_balance() — вывести текущий баланс
'''
class BankAccount:
    def __init__(self,owner,balance=0):
        self.owner=owner
        self.balance=balance

    def deposit(self,amount):
        if amount >= 1:
            self.balance += amount
            print(f"Вы пополнили счет на:{amount} сомов, у вас на счету:{self.balance} сомов")
        else:
            print('Нельзя пополнить счет числом меньше 0 или отрицательным значением')

    def withdraw(self,amount):
        if amount > self.balance:
            print(f'Вы не можете снять с карты сумму больше чем {self.balance}')
        else:
            self.balance -= amount
            print(f'Вы успешно сняли:{amount} сомов с счета, ваш баланс: {self.balance} сомов.')

bakyt=BankAccount('Бакыт')
bakyt.deposit(50000)
bakyt.withdraw(1500)

emma=BankAccount('Эмма')
emma.deposit(-1)
emma.withdraw(50)