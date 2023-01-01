import sqlite3

# Connect to database
conn = sqlite3.connect("users.db")

# Create cursor
c = conn.cursor()

# Update records
c.execute("""UPDATE test 
    SET last_name = 'Aikeout'
    WHERE rowid = 1
""")
# Query database
c.execute("SELECT * FROM test")

items = c.fetchall()

# Loop through all
for item in items:
    print(item)


# Commit command
conn.commit()

# Close connection
conn.close()
