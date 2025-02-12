import Product

class CategoryNode:
    def __init__(self, category_name: str):
        self.category_name = category_name
        self.products = []
        self.prev = None
        self.next = None


class CategoryList:
    def __init__(self):
        self.head = None
        self.tail = None

    def insert_product(self, product: Product):
        current = self.head
        while current:
            if current.category_name == product.category:
                current.products.append(product)
                return
            current = current.next
        
        new_node = CategoryNode(product.category)
        new_node.products.append(product)
        if not self.head:
            self.head = self.tail = new_node
        else:
            self.tail.next = new_node
            new_node.prev = self.tail
            self.tail = new_node

    def delete_product(self, product_id: str):
        current = self.head
        while current:
            for product in current.products:
                if product.product_id == product_id:
                    current.products.remove(product)
                    if not current.products:
                        self._delete_category_node(current)
                    return True
            current = current.next
        return False

    def delete_category_node(self, node):
        if node.prev:
            node.prev.next = node.next
        if node.next:
            node.next.prev = node.prev
        if node == self.head:
            self.head = node.next
        if node == self.tail:
            self.tail = node.prev

    def get_products_by_category(self, category_name: str):
        current = self.head
        while current:
            if current.category_name == category_name:
                return [product.get_product_info() for product in current.products]
            current = current.next
        return []

