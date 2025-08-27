from abc import ABC
from abc import abstractmethod

class Command(ABC):
    
    @abstractmethod
    def excute(self):
        pass
    
class CopyCommand(Command):
    
    def __init__(self, receiver):
        self.receiver = receiver
        
    def excute(self):
        self.receiver.copy()
        
class PasteCommand(Command):
    
    def __init__(self, receiver):
        self.receiver = receiver
        
    def excute(self):
        self.receiver.paste()