from domain.pizza_builder import PizzaBuilder
from pizza import Pizza
from domain.typeOfIngredient import TypeOfIngredient

class MargheritaBuilder(PizzaBuilder):
    
    def __init__(self) -> None:
        super().__init__()
        self.pizza = Pizza()

    def set_dough(self):
        self.pizza.dough = TypeOfIngredient(0).name
        
    def set_sauce(self):
        self.pizza.sauce = TypeOfIngredient(3).name
        
    def set_topping(self):
        self.pizza.topping = TypeOfIngredient(2).name