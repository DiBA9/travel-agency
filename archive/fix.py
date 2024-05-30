import sqlite3

# Establish a connection to the database
conn = sqlite3.connect('../data/trip_results.db')
cursor = conn.cursor()

# Define the new value for llm_temperature
new_value = 0.7

# Construct the SQL update statement
update_query = f"UPDATE agent_details SET llm_temperature = {new_value};"

# Execute the update statement
cursor.execute(update_query)

# Commit the transaction
conn.commit()

# Close the connection
conn.close()

print("The llm_temperature column in the 'agent_details' table has been updated to 0.7 successfully.")