import sqlite3

# Open the SQLite database file
conn = sqlite3.connect('data/homedata_05_2.db')

# Create a cursor object to execute SQL queries
cursor = conn.cursor()

# Execute a query to retrieve data from the 'data' table
cursor.execute("SELECT * FROM data")

# Fetch and print the results
rows = cursor.fetchall()
for row in rows:
    print(row)

# Close the database connection
conn.close()
