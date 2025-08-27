from factory.vehicleFactory import VehicleFactory
from models.motorcycle import Motorcycle

class MotorcycleFactory(VehicleFactory):
    
    def createVehicle(self):
        return Motorcycle()