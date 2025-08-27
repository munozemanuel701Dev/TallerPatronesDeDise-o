from abc import ABC 
from abc import abstractmethod

class FileSystemComponent(ABC):
    
    @abstractmethod
    def show_details(self):
        pass
    