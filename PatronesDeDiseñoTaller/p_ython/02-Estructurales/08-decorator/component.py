from abc import ABC
from abc import abstractmethod

class Text(ABC):
    
    @abstractmethod
    def render(self):
        pass
    