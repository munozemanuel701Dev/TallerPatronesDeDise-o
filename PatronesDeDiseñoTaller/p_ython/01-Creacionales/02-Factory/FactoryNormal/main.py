from factory.vehicleFactory import VehicleFactory

if __name__ == "__main__":
    
    vehicleFactory = VehicleFactory()
    
    car = vehicleFactory.createVehicle(typeOfVehicle="Car")
    car.start()
    car.stop()
    
    motorcycle = vehicleFactory.createVehicle(typeOfVehicle="Motorcycle")
    motorcycle.start()
    motorcycle.stop()
    
    obj1 = vehicleFactory.createVehicle(typeOfVehicle="Truck")
    obj1.start()
    obj1.stop()
    
    airplane = vehicleFactory.createVehicle(typeOfVehicle="Airplane")
    airplane.start()
    airplane.stop()
    airplane.fly()
     