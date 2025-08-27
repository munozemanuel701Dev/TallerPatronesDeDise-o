from facade import OnLineShoppingFacade

facade = OnLineShoppingFacade()

print(facade.place_order(user_id="user123", product_id="product456", amount=100))