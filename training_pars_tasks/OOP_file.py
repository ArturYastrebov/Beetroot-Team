class Car:
    wheels = 3

    def __init__(self, model, color):
        self.model = model
        self.color = color

    @classmethod
    def wheels_comp(cls, val):
        return cls.wheels > val

my_car_1 = Car('Ferarri','Black')
my_car_2 = Car('BMW', 'Yellow')

print(my_car_1.wheels)
print(my_car_2.wheels)

Car.wheels = 4
my_car_2.wheels = 1
print(my_car_2.wheels)

print(Car.wheels_comp(3))
print(my_car_2.wheels_comp(2))
print(my_car_2.wheels_comp(1))

