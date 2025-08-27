
class Pizza:
    
    def __init__(self) -> None:
        self.dough = None
        self.sauce = None
        self.topping = None
        
    def __str__(self) -> str:
        return f'Dough: {self.dough} | Sauce: {self.sauce} | Topping: {self.topping}'