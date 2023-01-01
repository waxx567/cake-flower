import sqlite3

# Connect to database
conn = sqlite3.connect("users.db")

# Create cursor
c = conn.cursor()

# Query database
c.execute("SELECT * FROM test WHERE number < 500")

# Loop
items = c.fetchall()

# Loop through all
for item in items:
    print(item)


# Commit command
conn.commit()

# Close connection
conn.close()
