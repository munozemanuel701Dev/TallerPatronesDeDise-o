from abc import ABC, abstractmethod

#con esto tenemos frabicas de cada objeto en específico

class VehicleFactory(ABC):
    
    @abstractmethod
    def createVehicle(self):
        pass