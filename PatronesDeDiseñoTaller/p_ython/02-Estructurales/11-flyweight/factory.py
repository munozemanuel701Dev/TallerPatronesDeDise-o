from flyweight import ChessPiceFlyweight

class ChessPiceFactory:
    
    _flyweights = {}
    
    @classmethod
    def get_flyweight(cls, name, color):
        
        key = (name, color)
        
        if not cls._flyweights.get(key):
            cls._flyweights[key] = ChessPiceFlyweight(name, color)
        return cls._flyweights[key]