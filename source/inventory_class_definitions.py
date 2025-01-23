class ItemSold:
    def __init__(self, item_sales_date_time, item_id, item_name, item_vendor, item_price):
        # Validate and assign the class fields
        self.item_sales_date_time = item_sales_date_time
        self.item_id = item_id
        self.item_name = item_name
        self.item_vendor = item_vendor
        self.item_price = item_price

    def __str__(self):
        return f"Date:{self.item_sales_date_time}, Item: {self.item_id}, Item Name: {self.item_name}, Vendor: {self.item_vendor}, Price: {self.item_price:.2f}"

