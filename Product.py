class StockInfo:
    def __init__(self, in_stock: int, reorder_level: int, reorder_quantity: int, inventory_status: str, batch_number: str):
        self.in_stock = in_stock
        self.reorder_level = reorder_level
        self.reorder_quantity = reorder_quantity
        self.inventory_status = inventory_status
        self.batch_number = batch_number
    
    def update_stock(self, quantity: int):
        self.in_stock += quantity
        self._update_inventory_status()
    
    def _update_inventory_status(self):
        if self.in_stock <= self.reorder_level:
            self.inventory_status = "Reorder Needed"
        else:
            self.inventory_status = "In Stock"
    
    def get_stock_info(self):
        return {
            "in_stock": self.in_stock,
            "reorder_level": self.reorder_level,
            "reorder_quantity": self.reorder_quantity,
            "inventory_status": self.inventory_status,
            "batch_number": self.batch_number
        }


class PriceInfo:
    def __init__(self, cost: float, retail_price: float, discount: float, tax_rate: float):
        self.cost = cost
        self.retail_price = retail_price
        self.discount = discount
        self.tax_rate = tax_rate
    
    def update_price(self, new_price: float):
        self.retail_price = new_price
    
    def apply_discount(self, discount: float):
        self.discount = discount
        self.retail_price -= (self.retail_price * (discount / 100))
    
    def get_price_info(self):
        return {
            "cost": self.cost,
            "retail_price": self.retail_price,
            "discount": self.discount,
            "tax_rate": self.tax_rate
        }


class Attributes:
    def __init__(self, size: str, weight: float, color: str, description: str):
        self.size = size
        self.weight = weight
        self.color = color
        self.description = description
    
    def update_attributes(self, size: str = None, weight: float = None, color: str = None, description: str = None):
        if size:
            self.size = size
        if weight:
            self.weight = weight
        if color:
            self.color = color
        if description:
            self.description = description
    
    def get_attributes(self):
        return {
            "size": self.size,
            "weight": self.weight,
            "color": self.color,
            "description": self.description
        }


class Digital:
    def __init__(self, product_images: list, help_links: list):
        self.product_images = product_images
        self.help_links = help_links
    
    def add_image(self, image_url: str):
        self.product_images.append(image_url)
    
    def add_help_link(self, link: str):
        self.help_links.append(link)
    
    def get_digital_info(self):
        return {
            "product_images": self.product_images,
            "help_links": self.help_links
        }


class Product:
    def __init__(self, product_id: str, name: str, category: str, stock_info: StockInfo, price_info: PriceInfo, attributes: Attributes, digital: Digital):
        self.product_id = product_id
        self.name = name
        self.category = category
        self.stock_info = stock_info
        self.price_info = price_info
        self.attributes = attributes
        self.digital = digital
    
    def update_name(self, new_name: str):
        self.name = new_name
    
    def update_category(self, new_category: str):
        self.category = new_category
    
    def get_product_info(self):
        return {
            "product_id": self.product_id,
            "name": self.name,
            "category": self.category,
            "stock": self.stock_info.in_stock,
            "price": self.price_info.retail_price
        }

