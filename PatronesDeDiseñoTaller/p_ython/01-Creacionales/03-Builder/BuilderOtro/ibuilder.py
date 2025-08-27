from abc import ABC, abstractmethod
from typing import TypeVar, Generic

T = TypeVar('T')

class IBuilder(ABC, Generic[T]):
    
    @abstractmethod
    def build(self) -> T:
        pass