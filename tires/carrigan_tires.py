from tires.tires import Tires

class CarriganTires(Tires):
    def __init__(self, tire_weariness):
        self.tire_weariness = tire_weariness

    def needs_service(self):
        total = 0
        for ti in self.tire_weariness:
            print("1111111111111111111111111111111111111")
            print(ti)
            print(ti >= 0.9)
            print("11111111111111111111111111111111111111")
            if ti >= 0.9:
                return True
        return False
