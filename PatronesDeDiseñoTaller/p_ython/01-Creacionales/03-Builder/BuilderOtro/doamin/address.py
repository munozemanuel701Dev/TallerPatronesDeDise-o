class Address:
    
    def __init__(self, *args) -> None:
        
        if len(args) == 0:
            self._address = None
            self._city = None
            self._country = None
            self._cp = None
        if len(args) == 4:
            self._address = args[0]
            self._city = args[1]
            self._country = args[2]
            self._cp = args[3]
            
    @property
    def address(self):
        return self._address
    
    @property.setter 
    def setAddress(self, address):
        self._address = address
        
    @property
    def city(self):
        return self._city
    
    @property.setter 
    def setCity(self, city):
        self._city = city
        
    @property
    def country(self):
        return self._country
    
    @property.setter 
    def setCountry(self, country):
        self._country = country
        
    @property
    def cp(self):
        return self._cp
    
    @property.setter 
    def setCp(self, cp):
        self._cp = cp
        
        
    def __str__(self) -> str:
        return f'Address: {self._address} | City: {self._city} | Country: {self._country} | Code postal: {self._cp}'