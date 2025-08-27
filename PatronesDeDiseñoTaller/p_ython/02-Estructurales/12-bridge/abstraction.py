from implementor import Render

class Shape:
    
    def __init__(self, render):
        self.render = render
        
    def draw(self):
        pass
    
    def resize(self, factor):
        pass
    
class Circle(Shape):
    
    def __init__(self, render, radius):
        super().__init__(render)  
        self.radius = radius
        
    def draw(self):
        self.render.render_shape("circle")
        
    def resize(self, factor):
        self.radius *= factor