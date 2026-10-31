# Food Delivery System

class Order:
    def __init__(self, order_id):
        self.order_id = order_id

    def place_order(self):
        print("Order placed")


class OnlineOrder(Order):
    def place_order(self):
        print("Online order placed")


class PickupOrder(Order):
    def place_order(self):
        print("Pickup order placed")


order1 = OnlineOrder(101)
order2 = PickupOrder(102)

order1.place_order()
order2.place_order()