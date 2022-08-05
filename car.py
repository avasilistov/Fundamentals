from time import sleep as s


class Car:

    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        self.odometr_reading = 0

    def get_descriptive_name(self):
        long_name = f'{self.year} {self.make} {self.model}'
        return long_name.title()

    def read_odometr(self):
        print(f'This car has {self.odometr_reading} miles on it.')

    def fill_gas_tank(self):
        print('The gas tank is fillig...')
        s(5)
        print("The gas tank is full!")


    def update_odometr(self, mileage):
        if mileage >= self.odometr_reading:
            self.odometr_reading = mileage
        else:
            print("You can't roll back an odometr!")

    def increment_odometr(self, miles):
        if miles >= 0:
            self.odometr_reading += miles
        else:
            print("You can't roll back an odometr!")