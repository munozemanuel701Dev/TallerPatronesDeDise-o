#primero

class Singlenton():
    
    _instance = {}
    
    def __new__(cls, *args,  **kwargs):
        if cls not in cls._instance:
            cls._instance[cls] = super().__new__(cls)
            
        return cls._instance[cls]
'''
obj1 = Singlenton()
obj2 = Singlenton()

print(obj1 is obj2)
'''