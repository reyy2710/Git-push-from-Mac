class Restaurant:
    def __init__(self):
        self.menu_items = {}
        self.book_table = []
        self.customer_orders = {}

    def add_item_to_menu(self, item, price):
        self.menu_items[item] = price

    def book_tables(self, table_no):
        if table_no not in self.book_table:
            self.book_table.append(table_no)
        else:
            print("Table already booked!")

    def customer_order(self, table_no, order_items):
        if table_no not in self.book_table:
            print("Table not booked!")
            return
        self.customer_orders[table_no] = order_items

    def print_menu(self):
        print("Menu:", self.menu_items)

    def print_table_reservations(self):
        print("Booked tables:", self.book_table)

    def print_customer_orders(self):
        print("Orders:", self.customer_orders)

# Example usage
rest = Restaurant()
rest.add_item_to_menu("Pizza", 500)
rest.book_tables(1)
rest.customer_order(1, ["Pizza", "Pasta"])
rest.print_menu()
rest.print_table_reservations()
rest.print_customer_orders()
