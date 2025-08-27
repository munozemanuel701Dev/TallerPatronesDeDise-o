from factory.airplaneFactory import AirplaneFactory
from factory.carFactory import CarFactory
from factory.motorcycle import MotorcycleFactory
from factory.truckFactory import TruckFactory

if __name__ == "__main__":
  
    airplane = AirplaneFactory().createVehicle()
    airplane.start()
    airplane.stop()
    airplane.fly()
    car = CarFactory().createVehicle()
    car.start()
    car.stop()
    motorcycle = MotorcycleFactory().createVehicle()
    motorcycle.start()
    motorcycle.stop()
    truck = TruckFactory().createVehicle()
    truck.start()
    truck.stop()