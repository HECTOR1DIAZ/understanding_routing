class Store:
    def __init__(self, given_name):
        self.name = given_name
        self.products = []
        
    def add_product(self,new_product):
        self.products.append(new_product)
        return self
    
    def sell_product(self,id):
        sold_product = self.products.pop(id)
        sold_product.print_info()
        return self
    
    def inflation(self, percent_increase):
        for product in self.products:
            product.update_price(percent_increase, True)
        return self
    
    
    def show_products(self):
        for product in self.products:
            product.print_info()
        return self

class Product:
    def __init__(self, given_name, given_price, given_category):
        self.name = given_name
        self.price = given_price
        self.category = given_category
        
# update_price(self, percent_change, is_increased) - updates the product's price. If is_increased is True, the price should increase by the percent_change provided. If False, the price should decrease by the percent_change provided.

    def update_price(self, percent_change, is_increased):
        if is_increased == True:
            self.price = self.price + (percent_change * self.price)
        else:
            self.price = self.price - (percent_change * self.price)
        return self
    
# print_info(self) - print the name of the product, its category, and its price.

def print_info(self):
    print(f'Product Name:{self.name}, Price: $ {self.price}, Category: {self.category}')
    return self


just_pants = Store("Just Pants")

levis501 = Product("Levi's 501", 50, "jeans")
levis503 = Product("Levi's 503", 50, "jeans")
levis505 = Product("Levi's 505", 50, "jeans")
levis511 = Product("Levi's 511", 50, "jeans")

just_pants.add_product(levis501).add_product(levis503).show_products()

# Let's also give some methods to our Store class:

# add_product(self, new_product) - takes a product and adds it to the store
# sell_product(self, id) - remove the product from the store's list of products given the id (assume id is the index of the product in the list) and print its info.
# inflation(self, percent_increase) - increases the price of each product by the percent_increase given (use the method you wrote in the Product class!)
# set_clearance(self, category, percent_discount) - updates all the products matching the given category by reducing the price by the percent_discount given (use the method you wrote in the Product class!)