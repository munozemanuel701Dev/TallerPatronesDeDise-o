from vehicle import Vehicle

class Truck(Vehicle):
    
    def start(self) -> None:
        print("--> Run truck!")
        
    def stop(self) -> None:
        print("--> Stop truck!")