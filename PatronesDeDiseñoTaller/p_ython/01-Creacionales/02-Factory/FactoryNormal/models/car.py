from vehicle import Vehicle

class Car(Vehicle):
    
    def start(self) -> None:
        print("--> Run car!")
        
    def stop(self) -> None:
        print("--> Stop car!")