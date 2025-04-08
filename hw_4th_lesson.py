class Transport:
    def __init__(self, brand, model, speed):
        self.brand=brand
        self.model=model
        self._speed=speed

    def move(self):
        print(f'Транспорт начал движение.')

    def get_speed(self):
        return self._speed

    def set_speed(self,speed):
        if isinstance(speed,int):
            self._speed=speed
        else:
            print('Error: speed should be an integer.')



class Car(Transport):
    def move(self):
        print(f'Автомобиль {self.brand}-{self.model} едет по дороге.')



class Bicycle(Transport):
    def move(self):
        print(f'Велосипед {self.brand}-{self.model} катится по велодорожке.')

transport_list=[Car('KIA','Morning',0), Bicycle('China','HRQ1207',0)]
transport_list[0].set_speed(60)
transport_list[1].set_speed(20)

for transport in transport_list:
    transport.move()
    print(f'Скорость: {transport.get_speed()} км/ч\n')