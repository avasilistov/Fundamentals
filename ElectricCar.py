from Car import Car


class ElectricCar(Car):
    def __init__(self, make, model, year):
        super().__init__(make, model, year)


my_tesla = ElectricCar('tesla', 'model s', 2022)
print(my_tesla.get_descriptive_name())
my_tesla.increment_odometr(200)
my_tesla.update_odometr(100)
my_tesla.read_odometr()
