'''
Тема: Принципы ООП - Инкапсуляция, Полиморфизм.
'''
class PublicExample:
    def __init__(self,value):
        self.value=value

    def info(self):
        return self.value              #Публичный метод
    
public=PublicExample("Public class")
# print(public.info())                 #Вызов публичного метода
# print(public.value)                  #Доступ к публичному атрибуту


class ProtectedExample:
    def __init__(self,value):
        self._value=value

    def _info(self):
        return self._value             #Защищенный метод

protected=ProtectedExample("Protected class")
# print(protected._info())             #Работает но не рекомендуется, т.к. противоречит принципам иинкапсуляции
# print(protected._value)              #Работает но не рекомендуется, т.к. противоречит принципам иинкапсуляции


class PrivateExample:
    def __init__(self,value):
        self.__value=value

    def __info(self):
        return self.__value            #Приватный метод
    
    def access_private(self):
        return self.__info()           #Публичный метод где мы получаем доступ к приватному методу или атрибуту
    
private=PrivateExample("Private class")
# print(private.__info())              #Выйдет ошибка
# print(private.__value)               #Выйдет ошибка

print(private.access_private())        #Доступ через приватный метод

print(private._PrivateExample__info()) #Искажение названия (name managing)


" Полиморфизм "
num1=1
num2=2
# print(num1+num2)


string1='hello'
string2='geeks'
# print(string1+string2)


# print(len("Geeks"))


# print(len(['python','js','php','react']))


# print(len({'python':'django','js':'react'}))


class Cat:
    def __init__(self,name,age):
        self.name=name
        self.age=age

    def info(self):
        print(f"Hi, I`m  a cat and my name is {self.name}, I`m {self.age} years old.")

    def make_sound(self):
        print(f"Meow")

class Dog:
    def __init__(self,name,age):
        self.name=name
        self.age=age

    def info(self):
        print(f"Hi, I`m  a dog and my name is {self.name}, I`m {self.age} years old.")

    def make_sound(self):
        print(f"Woof")

cat=Cat('Vaska',2)
dog=Dog("Bobik",3)

for animal in (cat,dog):
    animal.info()
    animal.make_sound()