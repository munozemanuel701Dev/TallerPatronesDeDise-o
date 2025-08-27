from abc import ABC
from abc import abstractmethod

class Render(ABC):
    
    @abstractmethod
    def render_shape(self, shape):
        pass
    
class VectorRender(Render):
    
    def render_shape(self, shape):
        print(f'Drawing {shape} as lines')
    
class RasterRender(Render):
    
    def render_shape(self, shape):
        print(f'Drawing {shape} as pixeles')
