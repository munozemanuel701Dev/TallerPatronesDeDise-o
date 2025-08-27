from abstraction import Circle
from implementor import RasterRender
from implementor import VectorRender

if __name__ == "__main__":
    
    vector_circle = Circle(VectorRender(), radius=5)
    raster_circle = Circle(RasterRender(), radius=5)
    
    vector_circle.draw()
    raster_circle.draw()