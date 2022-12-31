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
    # Print the third item in each tuple
    print(item[2])


# Commit command
conn.commit()

# Close connection
conn.close()
