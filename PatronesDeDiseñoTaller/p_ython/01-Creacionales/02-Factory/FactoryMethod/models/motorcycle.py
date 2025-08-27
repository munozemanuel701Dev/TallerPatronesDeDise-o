from vehicle import Vehicle

class Motorcycle(Vehicle):
    
    def start(self) -> None:
        print("--> Run motorcycle!")
        
    def stop(self) -> None:
        print("--> Stop motorcycle!")