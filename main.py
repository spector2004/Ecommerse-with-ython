import sys
import io
if sys.platform == 'win32':
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

class Product:
    def __init__(self, product_id, name, price, quantity):
        self.product_id = product_id
        self.name = name
        self.price = price
        self.quantity = quantity
    
    def __str__(self):
        return f"{self.name} - ₹{self.price} ({self.quantity} available)"
    
    def update_quantity(self, new_quantity):
        self.quantity = new_quantity


class ShoppingCart:
    def __init__(self):
        self.items = {}  
        self.total_price = 0
    
    def add_item(self, product, quantity):
        if product.quantity >= quantity:
            self.items[product.product_id] = self.items.get(product.product_id, 0) + quantity
            product.quantity -= quantity
            self.total_price += product.price * quantity
            print(f"✅ Added {quantity} {product.name}(s) to cart")
            return True
        else:
            print(f"❌ Not enough stock! Only {product.quantity} available")
            return False
    
    def remove_item(self, product, quantity):
        if product.product_id in self.items:
            if self.items[product.product_id] <= quantity:
                removed_quantity = self.items[product.product_id]
                del self.items[product.product_id]
            else:
                self.items[product.product_id] -= quantity
                removed_quantity = quantity
            
            product.quantity += removed_quantity
            self.total_price -= product.price * removed_quantity
            print(f"✅ Removed {removed_quantity} {product.name}(s) from cart")
        else:
            print("❌ Product not in cart")
    
    def view_cart(self):
        print("\n" + "="*50)
        print("🛒 YOUR SHOPPING CART")
        print("="*50)
        
        if not self.items:
            print("Cart is empty")
            return
        
        for product_id, quantity in self.items.items():
            print(f"Product ID: {product_id}, Quantity: {quantity}")
        
        print(f"💰 TOTAL: ₹{self.total_price}")
        print("="*50)
    
    def checkout(self):
        print("\n" + "="*50)
        print("💳 CHECKOUT")
        print("="*50)
        self.view_cart()
        print("✅ Thank you for your purchase!")
        print("="*50)
        
        self.items = {}
        self.total_price = 0


class ECommerceSystem:
    def __init__(self):
        self.products = []
        self.cart = ShoppingCart()
        self.initialize_sample_products()
    
    def initialize_sample_products(self):
        sample_products = [
            (1, "Laptop", 50000, 10),
            (2, "Wireless Mouse", 500, 50),
            (3, "Mechanical Keyboard", 1500, 20),
            (4, "Bluetooth Headphones", 2000, 15),
            (5, "Monitor", 8000, 8),
            (6, "USB Cable", 200, 100),
            (7, "Laptop Bag", 1200, 12),
            (8, "Wireless Router", 3000, 6)
        ]
        
        for product_id, name, price, quantity in sample_products:
            self.add_product(product_id, name, price, quantity)
    
    def add_product(self, product_id, name, price, quantity):
        product = Product(product_id, name, price, quantity)
        self.products.append(product)
    
    def display_products(self):
        print("\n" + "="*50)
        print("📦 AVAILABLE PRODUCTS")
        print("="*50)
        
        for product in self.products:
            print(f"{product.product_id}. {product}")
        
        print("="*50)
    
    def find_product(self, product_id):
        return next((p for p in self.products if p.product_id == product_id), None)
    
    def view_low_stock(self):
        print("\n" + "="*50)
        print("⚠  LOW STOCK ALERTS")
        print("="*50)
        
        low_stock_items = [p for p in self.products if p.quantity < 5]
        
        if not low_stock_items:
            print("All products have sufficient stock ✅")
        else:
            for product in low_stock_items:
                print(f"🚨 {product.name}: Only {product.quantity} left!")
        
        print("="*50)


def main():
    shop = ECommerceSystem()
    
    print("🏪 WELCOME TO OUR E-COMMERCE STORE!")
    print("="*50)
    
    while True:
        print("\n📋 MAIN MENU:")
        print("1. 🏪 View All Products")
        print("2. 🛒 Add Product to Cart")
        print("3. ❌ Remove Product from Cart")
        print("4. 👀 View My Cart")
        print("5. 💳 Checkout")
        print("6. ⚠  View Low Stock Items")
        print("7. 🚪 Exit")
        
        choice = input("\nEnter your choice (1-7): ").strip()
        
        if choice == '1':
            shop.display_products()
        
        elif choice == '2':
            shop.display_products()
            try:
                product_id = int(input("Enter product ID to add: "))
                quantity = int(input("Enter quantity: "))
                product = shop.find_product(product_id)
                
                if product:
                    shop.cart.add_item(product, quantity)
                else:
                    print("❌ Product not found!")
            
            except ValueError:
                print("❌ Enter valid numbers!")
        
        elif choice == '3':
            if not shop.cart.items:
                print("❌ Cart is empty!")
                continue
            
            shop.cart.view_cart()
            try:
                product_id = int(input("Enter product ID to remove: "))
                quantity = int(input("Enter quantity to remove: "))
                product = shop.find_product(product_id)
                
                if product:
                    shop.cart.remove_item(product, quantity)
                else:
                    print("❌ Product not found!")
            
            except ValueError:
                print("❌ Enter valid numbers!")
        
        elif choice == '4':
            shop.cart.view_cart()
        
        elif choice == '5':
            if not shop.cart.items:
                print("❌ Your cart is empty!")
                continue
            shop.cart.checkout()
        
        elif choice == '6':
            shop.view_low_stock()
        
        elif choice == '7':
            print("\n" + "="*50)
            print("🙏 Thank you for visiting our store!")
            print("="*50)
            break
        
        else:
            print("❌ Invalid choice! Enter 1–7.")


if __name__ == "__main__":
    main()
