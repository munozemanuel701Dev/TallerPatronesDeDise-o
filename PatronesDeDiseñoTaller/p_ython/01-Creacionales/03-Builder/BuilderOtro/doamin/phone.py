class Phone:
    
    def __init__(self, *args) -> None:
        
        if len(args) == 0:
            self._phoneNumber = None
            self._ext = None
            self._phoneType = None
            self._cp = None
        if len(args) == 3:
            self._phoneNumber = args[0]
            self._ext = args[1]
            self._phoneType = args[2]
            
    @property
    def phoneNumber(self):
        return self._phoneNumber
    
    @property.setter 
    def setPhoneNumber(self, phoneNumber):
        self._phoneNumber = phoneNumber
        
    @property
    def ext(self):
        return self._ext
    
    @property.setter 
    def setExt(self, ext):
        self._ext = ext
        
    @property
    def phoneType(self):
        return self._phoneType
    
    @property.setter 
    def setPhoneType(self, phoneType):
        self._phoneType = phoneType
        
    def __str__(self) -> str:
        return f'PhoneNumber: {self._phoneNumber} | Ext: {self._ext} | PhoneType: {self._phoneType}'