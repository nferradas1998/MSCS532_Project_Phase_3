import Product

class InventoryHashTable:
    def __init__(self):
        self.inventory = {}
    
    def upsert(self, product: Product):
        self.inventory[product.product_id] = product
    
    def search(self, product_id: str):
        return self.inventory.get(product_id, None)
    
    def delete(self, product_id: str):
        return self.inventory.pop(product_id, None) is not None
