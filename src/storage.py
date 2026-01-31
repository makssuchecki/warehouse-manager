from src.product import Product

class Storage:
    def __init__(self):
        self.products = []
    
    def add_product(self, product):
        self.products.append(product)

    def get_product_by_name(self, name):
        for product in self.products:
            if product.name == name:
                return product
        return None
    
    def get_all_products(self):
        return self.products
    
    def delete_product(self, name, user):
        if user.role != "admin":
            return False

        original_len = len(self.products)
        self.products = [p for p in self.products if p.name != name]
        return len(self.products) < original_len
    
    def count_products(self):
        return len(self.products)
    
    def clear(self):
        self.products = []