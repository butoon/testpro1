class Bicycle:
    def run(self, km):
        print(f'骑行公里数为： {km}')


class Ebicycle(Bicycle):
    def __init__(self, battery_level):
        self.battery_level = battery_level

    def fill_charge(self, vol):
        self.battery_level = self.battery_level + vol

    def run(self, km):
        miles = km - self.battery_level * 10
        if miles > 0:
            print(f'已经用电行驶{self.battery_level * 10}公里')
            super().run(miles)
        else:
            print(f'已经用电行驶{km}')


if __name__ == '__main__':
    eb = Ebicycle(1)
    eb.fill_charge(5)
    eb.run(101)
