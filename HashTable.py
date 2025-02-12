import Product

class InventoryHashTable:
    def __init__(self, capacity=100, load_factor=0.8):
        self.capacity = capacity  # Initial size of the hash table
        self.load_factor = load_factor # determines how much space is left in the table
        self.size = 0
        self.inventory = [None] * self.capacity  # Storage for items
        self.deleted = object()  # Special marker for deleted items

    def hash_product(self, product_id: str):
        return hash(product_id) % self.capacity # using built in python hash function 

    def resize(self):
        old_inventory = self.inventory
        self.capacity *= 2  # duplicate capacity
        self.inventory = [None] * self.capacity
        self.size = 0  # reset size and reinsert elements

        for item in old_inventory:
            if item and item is not self.deleted:
                self.upsert(item)

    def upsert(self, product: Product):
        if self.size / self.capacity >= self.load_factor:
            self.resize()

        index = self.hash_product(product.product_id)

        while self.inventory[index] is not None and self.inventory[index] is not self.deleted:
            if self.inventory[index].product_id == product.product_id:
                # update existing product
                self.inventory[index] = product
                return
            index = (index + 1) % self.capacity 

        # insert new product
        self.inventory[index] = product
        self.size += 1

    def search(self, product_id: str):
        index = self.hash_product(product_id)

        while self.inventory[index] is not None: # while the index is not null, that means there is a product to be checked
            if self.inventory[index] is not self.deleted and self.inventory[index].product_id == product_id: # check if product id matches
                return self.inventory[index]
            index = (index + 1) % self.capacity # handle collision search

        return None

    def delete(self, product_id: str):
        index = self._hash(product_id)

        while self.inventory[index] is not None:
            if self.inventory[index] is not self.deleted and self.inventory[index].product_id == product_id:
                self.inventory[index] = self.deleted  # Mark as deleted
                self.size -= 1
                return True
            index = (index + 1) % self.capacity

        return False

