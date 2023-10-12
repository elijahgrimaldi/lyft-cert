import engine, engine.model

class Car():
    def __init__(self, last_service_date, model):
        self.last_service_date = last_service_date
        self.Model = model

    def needs_service(self):
        return self.Model.needs_service()
        


