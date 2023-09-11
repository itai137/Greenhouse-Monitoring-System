import sqlite3

# Connect to the SQLite database
conn = sqlite3.connect('data/homedata_05_2.db')

# Create a cursor object
cursor = conn.cursor()

# Execute a SELECT query to retrieve data
cursor.execute("SELECT * FROM data")

# Fetch all rows of data
rows = cursor.fetchall()

# Display the retrieved data
for row in rows:
    print(row)

# Close the database connection
conn.close()
