import sqlite3

# Connect to database
conn = sqlite3.connect("users.db")

# Create cursor
c = conn.cursor()

# Query database
c.execute("SELECT * FROM test")

# Loop
items = c.fetchall()

for item in items:
    # Print the first item in each tuple
    print(item[0])


# Commit command
conn.commit()

# Close connection
conn.close()
