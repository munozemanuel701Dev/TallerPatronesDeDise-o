from ibuilder import IBuilder

class Employee:
    
    def __init__(self, *args) -> None:
        
        if len(args) == 0:
            self._age = None
            self._name = None
            self._gender = None
            self._address = []
            self._phones = []
            self._contact = []
        if len(args) == 6:
            self._age = args[0]
            self._name = args[1]
            self._gender = args[2]
            self._address = args[3]
            self._phones = args[4]
            self._contact = args[5]
    
    @classmethod    
    class EmployeeBuilder(IBuilder):
        
        _age = None
        _name = None
        _gender = None
        _address = []
        _phones = []
        _contact = []
        
        def setAge(self, age):
            self._age = age
            return self
        
        def setName(self, name):
            self._name = name
            return self
        
        def setGender(self, gender):
            self._gender = gender
            return self
        
        def setAddress(self, address, city, country, cp):
            self._address = Address(address, city, country, cp)
            
            
        def build(self):
            return None
            
    @property
    def age(self):
        return self._age
    
    @property.setter 
    def setAge(self, age):
        self._age = age
        
    @property
    def name(self):
        return self._name
    
    @property.setter 
    def setName(self, name):
        self._name = name
        
    @property
    def gender(self):
        return self._gender
    
    @property.setter 
    def setGender(self, gender):
        self._gender = gender
        
    @property
    def address(self):
        return self._address
    
    @property.setter 
    def setAddress(self, address):
        self._address = address
        
    @property
    def phones(self):
        return self._phones
    
    @property.setter 
    def setPhones(self, phones):
        self._phones = phones
        
    @property
    def contact(self):
        return self._contact
    
    @property.setter 
    def setContact(self, contact):
        self._contact = contact
        
    def __str__(self) -> str:
        return f'Age: {self._age} |  Name: {self._name} | Gender: {self._gender} | Address: {self._address} | Phones: {self._phones} | Contact: {self._contact}'