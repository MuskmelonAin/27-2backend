'''
Тема: Принцип ООП - Абстракция.
'''

class It:                #Абстрактный класс
    def direction(self):
        pass

    def language(self):
        pass

    def db(self):
        pass


class WebDeveloper(It):   #Конкретный класс
    def direction(self):
        return f'Backend'
    
    def language(self):
        return f'Python'
    
    def db(self):
        return f'Yes'
    

class Vercel(It):
    def direction(self):
        return f'Frontend'
    
    def language(self):
        return f'JS'
    
    def db(self):
        return f'No'
    

class Server(It):
    def direction(self):
        return f'DevOp'
    
    def language(self):
        return f'Linux/Python'
    
    def db(self):
        return f'Yes'
    
''''''

class Transport:
    def __init__(self, brand, speed):
        self.brand=brand
        self.speed=speed

    def info(self):
        return f'brand of the transport: {self.brand}, speed of the transport: {self.speed}'
    
    def move(self):
        return f'Транспорт движется'
    
class Car(Transport):
    def move(self):
        return f'Машина {self.brand} едет по дороге'
    
    def honk(self):
        return f"Машина сигналит"
    

class Bicycle(Transport):
    def move(self):
        return f'Велосипед {self.brand} едет по тропинке'
    
    def ring_bell(self):
        return f'Велосипед звенит звонком'
    

class Airplane(Transport):
    def move(self):
        return f'Самолет {self.brand} летит в небе'
    
    def take_off(self):
        return f'Самолет взлетает'
    

car=Car("BMW",60)
# print(car.move())
# print(car.honk())

bicycle=Bicycle("Airo",80)
# print(bicycle.move())
# print(bicycle.ring_bell())

airplane=Airplane("Air",150)
# print(airplane.move())
# print(airplane.take_off())


'''
Тема: Работа с базой даннных
СУБД - Система управления базы данных
CRUD - CREATE, RETRIVE, UPDATE, DELETE
'''

import sqlite3

connect = sqlite3.connect('geeks.db')
cursor = connect.cursor()

'''
Есть 2 вида запросов: sql и http
VARCHAR = STRING с ограничением что указывается в скобках
TEXT = STRING без ограничения

FLOAT=DOUBLE
'''

cursor.execute("""
        CREATE TABLE IF NOT EXISTS users(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            full_name VARCHAR (50) NOT NULL,
            age INT DEFAULT NULL,
            direction TEXT,
            is_have BOOLEAN NOT NULL DEFAULT FALSE,
            birth_date DATE,
            rating DOUBLE (4,2) DEFAULT (0.0)
        )
""")


def register():
    full_name = input("Введите ФИО: ")
    age = int(input("Введите возраст: "))
    direction = input("Введите направление: ")
    is_have = bool(input("Наличие ноутбука: "))
    birth_date = input("Введите дату рождения: ")
    rating = float(input("Введите свой рейтинг: "))

#-------написание sql запросов - 1 способ - ненадежный способ---------

#     cursor.execute(f""" INSERT INTO users
#                    (full_name, age, direction, is_have, birth_date, rating)
#                    VALUES ('{full_name}', {age}, '{direction}', {is_have}, '{birth_date}', {rating}) """)  
    
#     connect.commit() #Сохранение изменений в базе данных

# register()

    # Использование форматированных строк (f"") для вставки в SQL-запрос может привести к уязвимости типа SQL-инъекции,если пользователь
    # вводит специальные символы в текстовые поля  

#-------написание sql запросов - 2 способ - надежный способ---------

    cursor.execute(""" INSERT INTO users
                   (full_name, age, direction, is_have, birth_date, rating)
                   VALUES (?, ?, ?, ?, ?, ?) """, (full_name, age, direction, is_have, birth_date, rating))  
    
    # place-holding in Backend = (?)

    connect.commit() #Сохранение изменений в базе данных


# --------вытаскивание значений из базы данных------------

# ------вытаскиваем всё

# def all_students():
#     cursor.execute("SELECT * FROM users")
#     students = cursor.fetchall()
#     print(students)



# ------вытаскиваем одного пользователя

def all_students(id):
    cursor.execute("SELECT * FROM users WHERE id=?", (id,))
    students = cursor.fetchone()
    print(students)

# all_students(1)   #выйдут данные пользователя с id 1
# all_students(2)   #выйдут данные пользователя с id 2
# all_students(3)   #ничего не выйдет - None(т.к. там никого нет)


# если не записать запятую в (id,) то он будет читать как строку, а нам нужен tuple потому нужна запятая



# --------удаление значений из базы данных------------


def delete_students(id):
    cursor.execute("DELETE FROM users WHERE ID=?", (id,))
    connect.commit()
    print(f"The user {id} was deleted succesfully.")

delete_students(2)
# register()