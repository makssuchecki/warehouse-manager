from datetime import datetime

class Product:
    def __init__(self, name, quantity):
        self.name = name
        if  quantity <= 0 or quantity >= 999:
            self.quantity = "Invalid amount"
        else:
            self.quantity = quantity
        self.history = []

    
    def receive_stock(self, amount):
        if amount <= 0:
            self.quantity = "Invalid amount"
            return False
        
        self.quantity += amount
        self.history.append({
            "change": +amount,
            "timestamp": datetime.today().strftime("%Y-%m-%d")
        })
        return True
    
    def release_stock(self, amount):
        if amount <= 0:
            return False
        if amount > self.quantity:
            return False
        
        self.quantity -= amount
        self.history.append({
            "change": -amount,
            "timestamp": datetime.today().strftime("%Y-%m-%d")
        })
        return True
