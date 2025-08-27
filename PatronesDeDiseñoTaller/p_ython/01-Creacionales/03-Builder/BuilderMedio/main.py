from cook import Cook
from domain.pizza_builder_Margherita import MargheritaBuilder
from domain.pizza_builder_hawaiana import HawaianaBuilder

cook = Cook()
margherita_builder = MargheritaBuilder()
hawaiana_builder = HawaianaBuilder()
pizza1 = cook.make_pizza(margherita_builder)
print(pizza1)
pizza2 = cook.make_pizza(hawaiana_builder)
print(pizza2)
