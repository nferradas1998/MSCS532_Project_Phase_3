import Product 

class PriceNode:
    def __init__(self, product: Product):
        self.product = product
        self.left = None
        self.right = None
        self.height = 1  # Height of the node -> needed for balancing after inserts


class PriceBST:
    def __init__(self):
        self.root = None

    def get_height(self, node):
        return node.height if node else 0

    def get_balance(self, node):
        return self.get_height(node.left) - self.get_height(node.right) if node else 0

    def rotate_right(self, node):
        new_root = node.left # Get the new root
        temporary = new_root.right # store the right tree of the new root in a temp variable
        # rotate by making the node the right child of the new root
        new_root.right = node 
        node.left = temporary # Make temporary the left tree of the node

        # recalculate the heights for the node and the new_root
        node.height = max(self.get_height(node.left), self.get_height(node.right)) + 1
        new_root.height = max(self.get_height(new_root.left), self.get_height(new_root.right)) + 1

        # return the new_root of the tree
        return new_root

    def rotate_left(self, node):
        new_root = node.right # Get the new root
        temp = new_root.left # store the left tree of the new root in a temp variable
        # rotate by making the node the left child of ythe new root
        new_root.left = node
        node.right = temp

        # recalculate the height for the node and new root node
        node.height = max(self.get_height(node.left), self.get_height(node.right)) + 1
        new_root.height = max(self.get_height(new_root.left), self.get_height(new_root.right)) + 1

        return new_root

    def insert(self, product: Product):
        # Create a new node for the given product
        new_node = PriceNode(product)

        # check for empty tree, assign the node as the root if its empty
        if not self.root:
            self.root = new_node
            return

        stack = [] # Use a stack because that helps keep track of visited nodes, so its easier to balance the tree
        current = self.root # this will be used to traverse the tree, needs to start at the root
        parent = None # will be used as the node from with the new node will be attached

        while current:
            parent = current
            stack.append(current)
            # check if the product price is less than the parent to see to what side it needs to go
            if product.price_info.retail_price < current.product.price_info.retail_price: # is less, go left of the current node
                current = current.left
            else: # go right
                current = current.right

        # assign the new node to the correct side of the parent
        if product.price_info.retail_price < parent.product.price_info.retail_price:
            parent.left = new_node
        else:
            parent.right = new_node

        # After insertion is done, need to re-balance the tree, this is where the stack is helpful
        while stack:
            node = stack.pop()
            node.height = max(self.get_height(node.left), self.get_height(node.right)) + 1
            # call the get_balance function to check if the tree is unbalanced
            balance = self.get_balance(node)

            if balance > 1: # this means that we need to rebalance the tree from the left side (do a right rotation)
                if product.price_info.retail_price < node.left.product.price_info.retail_price:
                    if stack:
                        parent = stack[-1]
                        if parent.left == node:
                            parent.left = self.rotate_right(node)
                        else:
                            parent.right = self.rotate_right(node)
                    else:
                        self.root = self.rotate_right(node)
                else:
                    node.left = self.rotate_left(node.left)
                    if stack:
                        parent = stack[-1]
                        if parent.left == node:
                            parent.left = self.rotate_right(node)
                        else:
                            parent.right = self.rotate_right(node)
                    else:
                        self.root = self.rotate_right(node)
            elif balance < -1: # this means that we need to rebalance the tree from the right side (left rotation)
                if product.price_info.retail_price > node.right.product.price_info.retail_price:
                    if stack:
                        parent = stack[-1]
                        if parent.left == node:
                            parent.left = self.rotate_left(node)
                        else:
                            parent.right = self.rotate_left(node)
                    else:
                        self.root = self.rotate_left(node)
                else:
                    node.right = self.rotate_right(node.right)
                    if stack:
                        parent = stack[-1]
                        if parent.left == node:
                            parent.left = self.rotate_left(node)
                        else:
                            parent.right = self.rotate_left(node)
                    else:
                        self.root = self.rotate_left(node)

    def search_min_price(self):
        current = self.root
        while current and current.left:
            current = current.left
        return current.product.get_product_info() if current else None

    def search_max_price(self):
        current = self.root
        while current and current.right:
            current = current.right
        return current.product.get_product_info() if current else None

    def search_price_range(self, min_price, max_price):
        results = []
        stack = [self.root]
        while stack:
            node = stack.pop()
            if node:
                if min_price <= node.product.price_info.retail_price <= max_price:
                    results.append(node.product.get_product_info())
                if min_price < node.product.price_info.retail_price:
                    stack.append(node.left)
                if max_price > node.product.price_info.retail_price:
                    stack.append(node.right)
        return results

    def search_above_price(self, min_price):
        results = []
        stack = [self.root]
        while stack:
            node = stack.pop()
            if node:
                if node.product.price_info.retail_price >= min_price:
                    results.append(node.product.get_product_info())
                    stack.append(node.left)
                stack.append(node.right)
        return results

    def search_below_price(self, max_price):
        results = []
        stack = [self.root]
        while stack:
            node = stack.pop()
            if node:
                if node.product.price_info.retail_price <= max_price:
                    results.append(node.product.get_product_info())
                    stack.append(node.left)
                stack.append(node.right)
        return results

price_bst = PriceBST()

for i in range(1, 11):
    stock = Product.StockInfo(in_stock=100, reorder_level=10, reorder_quantity=50, inventory_status="In Stock", batch_number=f"B{i}")
    price = Product.PriceInfo(cost=5.0 * i, retail_price=10.0 * i, discount=0.0, tax_rate=5.0)
    attributes = Product.Attributes(size="Medium", weight=1.5, color="Blue", description=f"Product {i}")
    digital = Product.Digital(product_images=[f"image{i}.jpg"], help_links=[f"help{i}.com"])
    product = Product.Product(product_id=f"P00{i}", name=f"Product {i}", category="Electronics", stock_info=stock, price_info=price, attributes=attributes, digital=digital)
    price_bst.insert(product)

# Price-based searches
print("=======This is the cheapest Product============\n")
print("Minimum priced product:", price_bst.search_min_price())

print("\n\n========This is the most expensive Product=========\n")
print("Maximum priced product:", price_bst.search_max_price())

print("\n\n=========These are products between 30 and 70 bucks===========\n")
print("Products in price range 30 to 70:", price_bst.search_price_range(30, 70))

print("\n\n=========These are products above 70 bucks===========\n")
print("Products above price 70:", price_bst.search_above_price(70))

print("\n\n=========These are products below 50 bucks===========\n")
print("Products below price 50:", price_bst.search_below_price(50))