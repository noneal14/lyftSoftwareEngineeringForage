from tires.tires import Tires

class OctoprimeTires(Tires):
    def __init__(self, tire_weariness):
        self.tire_weariness = tire_weariness

    def needs_service(self):
        if sum(self.tire_weariness) >= 3:
            return True
        return False

