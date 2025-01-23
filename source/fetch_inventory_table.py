import sqlite3
from inventory_class_definitions import ItemSold


# Create a function to fetch data from the database and create ItemSold objects
def fetch_inventory_db():
    # Establish a connection to the database
    conn = sqlite3.connect('inventory.db')
    cursor = conn.cursor()

    # Execute the query to fetch data 
    cursor.execute('SELECT * FROM items_sold')

    # Fetch all rows
    rows = cursor.fetchall()

    # Create a list to hold ItemSold objects
    items = []

    # each row is an instance of the class ItemSold. They are objects
    # Loop through each row and create ItemSold objects (AN INSTANCE OF THE ItemSold class)
    for row in rows:
        # row contains a tuple: (item_id, item_name, item_department, item_price)
        item = ItemSold(row[0], row[1], row[2], row[3], row[4])
        print(item)
        items.append(item)
        

    print(items)
    # Close the database connection
    conn.close()

    return items

# Call the function and print the resulting list of ItemSold objects
items = fetch_inventory_db()

# Print all items (this will use the __str__ method of the ItemSold class)
for item in items:
    print(item)