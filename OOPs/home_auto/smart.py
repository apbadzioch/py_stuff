class SmartDevice:
    def __init__(self, name):
        self.name = name
        self.is_on = False

    def toggle_power(self):
        self.is_on = not self.is_on

        if self.is_on:
            print("Power on")
        else:
            print("Power off")

my_device = SmartDevice('hall light')
my_device.toggle_power()
my_device.toggle_power()