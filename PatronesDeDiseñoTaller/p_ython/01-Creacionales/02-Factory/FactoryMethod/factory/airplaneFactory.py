from factory.vehicleFactory import VehicleFactory
from models.airplane import Airplane

class AirplaneFactory(VehicleFactory):
    
    def createVehicle(self):
        return Airplane()