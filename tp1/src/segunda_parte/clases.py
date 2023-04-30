class Product():

    def __init__(self, prod_type, qty):
        self.prod_type = prod_type
        self.qty = qty
        
    def __str__(self):
        return f"Product type: {self.prod_type}-qty: {self.qty}"

class Bribe():
    
    def __init__(self, prod_type, qty):
        self.prod_type = prod_type
        self.qty = qty

    def __str__(self):
        return f"Product Type: {self.prod_type}-qty: {self.qty}"
