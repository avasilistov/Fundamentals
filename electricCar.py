from car import Car
from battery import Battery


class ElectricCar(Car):
    def __init__(self, make, model, year):
        super().__init__(make, model, year)
        self.battery = Battery(120)

    # def describe_battery(self):
    #     print(f'This car has {self.battery_size}--kW battery.')

    def fill_gas_tank(self):
        print('This car doesn\'t need a gas tank')


my_tesla = ElectricCar('tesla', 'model s', 2022)
my_subaru = Car('subaru', 'outback', 2022)
print(my_tesla.get_descriptive_name())
my_tesla.increment_odometr(200)
my_tesla.update_odometr(100)
my_tesla.read_odometr()
my_tesla.battery.describe_battery()
my_tesla.fill_gas_tank()
my_subaru.fill_gas_tank()
my_tesla.battery.get_range()
