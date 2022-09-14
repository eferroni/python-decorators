

def object_counter(class_):
    class_.__getattr__orig = class_.__getattribute__

    def new_getattr(self, name):
        if name == 'mileage':
            print('getting mileage')
        return class_.__getattr__orig(self, name)

    class_.__getattribute__ = new_getattr
    return class_


@object_counter
class Car:
    def __init__(self, VIN):
        self.mileage = 0
        self.VIN = VIN


if __name__ == '__main__':
    car = Car('ABC123')
    print('mileage:', car.mileage)
    print('VIN:', car.VIN)
    print('mileage:', car.mileage)
