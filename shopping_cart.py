class ShoppingCart:
    # class variable
    # products inventory
    products = {'iPhone': 5, 'iMac': 3, 'iWatch': 2, 'iPad': 4}
    # prices are same for all the customer
    prices = {"iPhone": 900, "iMac": 2500, 'iWatch': 3500, 'iPad': 3500}

    def __init__(self):
        self.cart = [ ]

    def add_item(self, name, quantity):
        # validating the name of the product
        if name not in ShoppingCart.products:
            raise Exception(f"Cannot add product {name}")
        # validating the quantity that the user is byuing
        if quantity > ShoppingCart.products[name]:
            raise Exception(f"Product out of stock")
        # if everything is fine, add the item to the cart
        d = {"name": name, "quantity": quantity, "price": ShoppingCart.prices[name]}
        self.cart.append(d)
        ShoppingCart.products[name] = ShoppingCart.products[name] - quantity
    
    def remove_item(self, name):
        for item in self.cart:
           if item['name'] == name:
                if item['quantity'] == 1:
                    self.cart.remove(item)
                else:
                    item['quantity'] = item['quantity'] - 1
    
    def total_cost(self):
        prices = [ item['quantity'] * item['price']  for item in self.cart ]
        total = 0
        for price in prices:
            total = total + price
        return total


c1 = ShoppingCart()
c2 = ShoppingCart()
