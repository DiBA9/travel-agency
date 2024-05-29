import sqlite3

# Path to the SQLite database file in the /data directory
database_path = "../data/trip_results.db"

# Connect to the SQLite database
conn = sqlite3.connect(database_path)
cursor = conn.cursor()

# Query to retrieve all records from the results table
cursor.execute('SELECT * FROM results')
rows = cursor.fetchall()

# Print the retrieved records with formatting
for row in rows:
    record_id, origin, cities, travel_dates, interests, result = row
    print("\n\n########################")
    print(f"## Record ID: {record_id}")
    print("########################\n")
    print(f"Origin: {origin}")
    print(f"Cities: {cities}")
    print(f"Travel Dates: {travel_dates}")
    print(f"Interests: {interests}")
    print("\nResult:\n")
    print(result)
    print("\n\n")

# Close the database connection
conn.close()