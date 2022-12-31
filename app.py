import sqlite3

# Connect to database
conn = sqlite3.connect("users.db")

# Create cursor
c = conn.cursor()

# Insert many records into db
many_data = [("Liksmi", "Lotz", 48), ("Bo", "Low", 8887),
             ("Peat", "Bong", 420), ("Halal", "Tukka", 308),]

c.executemany()

# Commit command
conn.commit()

# Close connection
conn.close()
