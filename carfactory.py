from car import Car
class CarFactory():

    def __init__(self,model):
        self.CreateCar(model)
    def CreateCar(model):
        return Car(model)
