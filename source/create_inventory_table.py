import sqlite3

# Create a SQLite database and a table
conn = sqlite3.connect('inventory.db')
cursor = conn.cursor()

# Create a Students table
cursor.execute('''
    CREATE TABLE IF NOT EXISTS items_sold (
    item_sales_date_time TEXT NOT NULL,
    item_id INTEGER NOT NULL,
    item_name TEXT NOT NULL,
    item_vendor TEXT NOT NULL,
    item_price FLOAT NOT NULL,
    PRIMARY KEY (item_sales_date_time, item_id)
)
''')

# Insert some sample data into the Students table
cursor.execute('''
    INSERT INTO items_sold (item_sales_date_time, item_id, item_name, item_vendor, item_price) 
    VALUES 
    ('2024-06-14 14:42', 7858692633, 'frog', 'Photobug', 37.75),
    ('2023-12-12 01:31', 5956678433, 'cat', 'Dabjam', 43.27),
    ('2023-09-07 13:52', 9612896933, 'dog', 'Yakidoo', 31.05),
    ('2023-10-12 21:17', 5145708233, 'walrus', 'Edgeblab', 4.06),
    ('2023-11-30 04:46', 1499507733, 'fish', 'Centidel', 31.49),
    ('2024-08-21 12:29', 7294702733, 'bee', 'Topicstorm', 26.12),
    ('2023-11-26 22:17', 143432833, 'squid', 'Edgeclub', 32.10),
    ('2024-01-27 11:10', 9058178133, 'deer', 'Muxo', 46.89),
    ('2024-03-02 02:22', 2564553933, 'chicken', 'Brightdog', 45.34)
''')

# Commit the changes and close the connection
conn.commit()
conn.close()
