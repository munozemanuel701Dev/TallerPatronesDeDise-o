from abc import ABC
from abc import abstractmethod

class CommissionStrategy(ABC):
    
    @abstractmethod
    def calculate_commission(self, amount):
        pass
    
class FixedCommission(CommissionStrategy):
    
    def calculate_commission(self, amount):
        return 5
    
class PercentegeCommission(CommissionStrategy):
    
    def calculate_commission(self, amount):
        return amount * 0.05