import sqlite3

# Path to the SQLite database file in the /data directory
database_path = "/data/trip_results.db"

# Connect to the SQLite database
conn = sqlite3.connect(database_path)
cursor = conn.cursor()

# Query to retrieve all records from the results table
cursor.execute('SELECT * FROM results')
rows = cursor.fetchall()

# Print the retrieved records
print("ID | Origin | Cities | Travel Dates | Interests | Result")
print("----------------------------------------------------------")
for row in rows:
    print(row)

# Close the database connection
conn.close()