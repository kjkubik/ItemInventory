import sqlite3

# open connection to a database
conn = sqlite3.connect('inventory.db') 

# create a cursor object
cursor = conn.cursor()

# execute SQL
cursor.execute('select * FROM items_sold ')

# cursor.execute('delete FROM items_sold ')
# conn.commit()  # Commit the changes

# Fetch all results
rows = cursor.fetchall()

# Print each row
for row in rows:
    print(row)

# Close the connection
conn.close()