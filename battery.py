class Battery:

    def __init__(self, battery_size=75):
        self.battery_size = battery_size

    def describe_battery(self):
        print(f'This car has {self.battery_size}--kW battery.')

    def get_range(self):
        if self.battery_size == 75:
            range = 260
        if self.battery_size == 120:
            range = 380

        print(f'This car has a {range} miles range.')