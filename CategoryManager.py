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

    def _delete_category_node(self, node):
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


# Sample Usage with 10 Products
categories = CategoryList()

category_options = ["Electronics", "Home Appliances", "Furniture"]

for i in range(1, 11):
    stock = Product.StockInfo(in_stock=100, reorder_level=10, reorder_quantity=50, inventory_status="In Stock", batch_number=f"B{i}")
    price = Product.PriceInfo(cost=5.0 * i, retail_price=10.0 * i, discount=0.0, tax_rate=5.0)
    attributes = Product.Attributes(size="Medium", weight=1.5, color="Blue", description=f"Product {i}")
    digital = Product.Digital(product_images=[f"image{i}.jpg"], help_links=[f"help{i}.com"])
    category = category_options[i % 3]  # Distribute products among the 3 categories
    product = Product.Product(product_id=f"P00{i}", name=f"Product {i}", category=category, stock_info=stock, price_info=price, attributes=attributes, digital=digital)
    categories.insert_product(product)

# Retrieve products by category
print("====================These Products are on the Electronics Category==================\n")
print(categories.get_products_by_category("Electronics"))

print("\n\n====================These Products are on the Home Appliances Category==================\n")
print(categories.get_products_by_category("Home Appliances"))

print("\n\n====================These Products are on the Furniture Category==================\n")
print(categories.get_products_by_category("Furniture"))
