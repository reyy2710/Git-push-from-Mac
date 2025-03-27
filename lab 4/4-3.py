class Inventory:
    def __init__(self):
        self.items = {}

    def add_item(self, item_id, item_name, stock_count, price):
        self.items[item_id] = {"item_name": item_name, "stock_count": stock_count, "price": price}

    def update_item(self, item_id, stock_count=None, price=None):
        if item_id in self.items:
            if stock_count is not None:
                self.items[item_id]["stock_count"] = stock_count
            if price is not None:
                self.items[item_id]["price"] = price
        else:
            print("Item not found.")

    def check_item_details(self, item_id):
        return self.items.get(item_id, "Item not found.")

# Example usage
inv = Inventory()
inv.add_item(101, "Laptop", 5, 50000)
inv.update_item(101, stock_count=4)
print(inv.check_item_details(101))
