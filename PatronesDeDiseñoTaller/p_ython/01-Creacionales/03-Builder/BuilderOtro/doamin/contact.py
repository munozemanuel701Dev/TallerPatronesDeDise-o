class Contact:
    
    def __init__(self, *args) -> None:
        
        if len(args) == 0:
            self._name = None
            self._phone = None
            self._address = None
        if len(args) == 3:
            self._name = args[0]
            self._phone = args[1]
            self._address = args[2]
            
    @property
    def name(self):
        return self._name
    
    @property.setter 
    def setName(self, name):
        self._name = name
        
    @property
    def phone(self):
        return self._phone
    
    @property.setter 
    def setphone(self, phone):
        self._phone = phone
        
    @property
    def address(self):
        return self._address
    
    @property.setter 
    def setAddress(self, address):
        self._address = address
        
    def __str__(self) -> str:
        return f'Name: {self._name} |  Phone: {self._phone} | Address: {self._address}'