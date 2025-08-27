from vehicle import Vehicle

class Airplane(Vehicle):
    
    def start(self) -> None:
        print("--> Run airplane!")
        
    def stop(self) -> None:
        print("--> Stop airplane!")
        
    def fly(self) -> None:
        print("--> Take off the plane!")