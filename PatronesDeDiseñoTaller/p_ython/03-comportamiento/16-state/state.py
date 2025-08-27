from abc import ABC
from abc import abstractmethod

class PlayerState(ABC):
    
    @abstractmethod
    def press_play(self, player):
        pass
    
class PlayingState(PlayerState):
    
    def press_play(self, player):
        print("Pausing")
        player.state = PausedState()
        
class PausedState(PlayerState):
    
    def press_play(self, player):
        print("Playing")
        player.state = PlayingState()
        
class StoppedState(PlayingState):
    
    def press_play(self, player):
        print("Stopped")
        player.state = PlayingState()