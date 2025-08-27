from factory.vehicleFactory import VehicleFactory
from models.truck import Truck

class TruckFactory(VehicleFactory):
    
    def createVehicle(self):
        return Truck()