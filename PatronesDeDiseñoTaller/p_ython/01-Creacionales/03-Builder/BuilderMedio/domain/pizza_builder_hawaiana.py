from domain.pizza_builder import PizzaBuilder
from domain.typeOfIngredient import TypeOfIngredient
from pizza import Pizza

class HawaianaBuilder(PizzaBuilder):
    
    def __init__(self) -> None:
        super().__init__()
        self.pizza = Pizza()
        
    def set_dough(self):
        self.pizza.dough = TypeOfIngredient(0).name
        
    def set_sauce(self):
        self.pizza.sauce = TypeOfIngredient(4).name
        
    def set_topping(self):
        self.pizza.topping = TypeOfIngredient(2).name