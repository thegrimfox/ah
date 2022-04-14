class CarHub():

    def __init__(self, car_id) -> None:
        self.car_id = car_id

    def show_car_id(self):
        print(self.car_id)


c = CarHub('khft23')
d = CarHub('khtr11')
c.show_car_id()
d.show_car_id()
c.car_id = 'lmtp12'
c.show_car_id()
d.show_car_id()
