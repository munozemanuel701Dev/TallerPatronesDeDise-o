from abc import ABC, abstractmethod
from typing import TypeVar, Generic

T = TypeVar('T')

class IPrototype(ABC, Generic[T]):
    
    @abstractmethod
    def clone(self) -> T:
        pass
    
    @abstractmethod
    def deepClone(self) -> T:
        pass