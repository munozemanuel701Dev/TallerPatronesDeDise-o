from factory.vehicleFactory import VehicleFactory
from typeOfVehicle import TypeOfVehicle

if __name__ == "__main__":
    
    vehicleFactory = VehicleFactory()
    
    car = vehicleFactory.createVehicle(TypeOfVehicle(2).name)
    car.start()
    car.stop()
    
    motorcycle = vehicleFactory.createVehicle(TypeOfVehicle(3).name)
    motorcycle.start()
    motorcycle.stop()
    
    obj1 = vehicleFactory.createVehicle(TypeOfVehicle(4).name)
    obj1.start()
    obj1.stop()
    
    airplane = vehicleFactory.createVehicle(TypeOfVehicle(1).name)
    airplane.start()
    airplane.stop()
    airplane.fly()
     