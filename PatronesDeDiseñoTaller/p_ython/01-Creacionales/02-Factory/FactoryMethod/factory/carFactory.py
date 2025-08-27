from factory.vehicleFactory import VehicleFactory
from models.car import Car

class CarFactory(VehicleFactory):
    
    def createVehicle(self):
        return Car()