'''
Тема: Принципы ООП - Наследование Инкапсуляция, Полиморфизм.
'''
class Game:
    def __init__(self,name,year,company,graphics):
        self.name=name
        self.year=year
        self.company=company
        self.graphics=graphics

    def info(self):
        print(f"Game - {self.name} - {self.year} - {self.company} - {self.graphics}")

# game=Game("Minecraft",2017,"Mojang","Full HD")
# game.info()



class Roblox(Game):
    def __init__(self, name, year, company, graphics, multiplayer):
        super().__init__(name, year, company, graphics)
        self.multiplayer=multiplayer

        self.player_name="Player"
        self.gender="None"
        self.skin="None"
        self.hp=100

    def info(self):
        print(f"Game - {self.name} - {self.year} - {self.company} - {self.graphics} - {self.multiplayer}")
        
    def info_player(self):
        print(f"Player - {self.player_name} - {self.gender} - {self.skin} - {self.hp}")

    def edit_player(self):
        name=input("Enter your name: ")
        gender=input("Enter your gender: ")
        skin=input("Enter your skin: ")
        self.player_name=name
        self.gender=gender
        self.skin=skin
    
# roblox=Roblox("Roblox",2006,"Roblox corp.","ULTRA","4")
# roblox.info()
# roblox.edit_player()
# roblox.info_player()



class Strike(Roblox):
    def __init__(self, name, year, company, graphics, multiplayer):
        super().__init__(name, year, company, graphics, multiplayer)

    def edit_player(self):
        return super().edit_player()
    
    def info_player(self):
        return super().info_player()
    
# strike=Strike("Roblox-strike",2017,"Roblox corp.","ULTRA","4")
# strike.edit_player()
# strike.info_player()



class Animal:
    def __init__(self,name):
        self.name=name

    def eat(self):
        print(f"{self.name} eats")

    def sleep(self):
        print(f"{self.name} sleeps")

animal=Animal("Woo-hoo")
animal.eat()
animal.sleep()


class Walker(Animal):
    def __init__(self, name):
        super().__init__(name)

    def walk(self):
        print(f"{self.name} walks")

    
walker=Walker("Yaa-hoo")
walker.walk()
walker.eat()
walker.sleep()



class Swimmer(Animal):
    def __init__(self, name):
        super().__init__(name)

    def swim(self):
        print(f"{self.name} swims")

    
swimmer=Swimmer("Bulb")
swimmer.swim()
swimmer.eat()
swimmer.sleep()



class Flyer(Animal):
    def __init__(self, name):
        super().__init__(name)

    def fly(self):
        print(f"{self.name} flies")

    def eat(self):
        return super().eat()
    
    def sleep(self):
        return super().sleep()
    
flyer=Flyer("Wshhhh")
flyer.fly()
flyer.eat()
flyer.sleep()



class Penguin(Animal,Walker,Swimmer):
    def __init__(self, name):
        super().__init__(name)

    def describe(self):
        print(f"The penguin - {self.name} can swim and walk")
    
    
penguin=Penguin("Doo-doo")
penguin.walk()
penguin.swim()
penguin.describe()
penguin.eat()
penguin.sleep()



class Duck(Animal,Walker,Swimmer,Flyer):
    def __init__(self, name):
        super().__init__(name)

    def describe(self):
        print(f"The duck - {self.name} can swim, walk and fly")

    
duck=Duck("Krya-krya")
duck.walk()
duck.swim()
duck.fly()
duck.describe()
duck.eat()
duck.sleep()



class Bat(Animal,Flyer):
    def __init__(self, name):
        super().__init__(name)

    def describe(self):
        print(f"The bat - {self.name} can fly")
    
bat=Bat("Vampire")
bat.fly()
bat.describe()