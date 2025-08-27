from models.airplane import Airplane
from models.car import Car
from models.motorcycle import Motorcycle
from models.truck import Truck

from vehicle import Vehicle

class VehicleFactory():
    
    def createVehicle(self, typeOfVehicle) -> Vehicle:
        
        if(typeOfVehicle.lower() == "airplane"):
            return Airplane()
        if(typeOfVehicle.lower() == "car"):
            return Car()
        if(typeOfVehicle.lower() == "motorcycle"):
            return Motorcycle()
        if(typeOfVehicle.lower() == "truck"):
            return Truck()
        return None