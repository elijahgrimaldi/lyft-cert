from tires.tire import Tire

class CarriganTire(Tire):
    def __init__(self,wear):
        self.wear = wear

    def needs_service(self):
        for n in self.wear:
            if n >= 0.9:
                return True
        return False
