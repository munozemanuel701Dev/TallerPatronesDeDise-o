from cook import Cook
from pizza_builder import MargheritaBuilder
from pizza_builder import HawaianaBuilder

cook = Cook()
margherita_builder = MargheritaBuilder()
hawaiana_builder = HawaianaBuilder()
pizza1 = cook.make_pizza(margherita_builder)
print(pizza1)
pizza2 = cook.make_pizza(hawaiana_builder)
print(pizza2)
