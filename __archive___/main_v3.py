import os
import sqlite3
from textwrap import dedent
from crewai import Crew
from agents import TravelAgents
from tasks import TravelTasks
from dotenv import load_dotenv

load_dotenv()

# Ensure the /data directory exists
os.makedirs("../data", exist_ok=True)

# Path to the SQLite database file in the /data directory
database_path = "../data/trip_results.db"

class TripCrew:
    def __init__(self, origin, cities, travel_dates, interests):
        self.origin = origin
        self.cities = cities
        self.travel_dates = travel_dates
        self.interests = interests

    def run(self):
        # Define your custom agents and tasks in agents.py and tasks.py
        agents = TravelAgents()
        tasks = TravelTasks()

        # Define your custom agents and tasks here
        expert_travel_agent = agents.expert_travel_agent()
        city_selection_expert = agents.city_selection_expert()
        local_tour_guide = agents.local_tour_guide()

        # Custom tasks include agent name and variables as input
        plan_itinerary = tasks.plan_itinerary(
            expert_travel_agent,
            self.cities,
            self.travel_dates,
            self.interests
        )

        identify_city = tasks.identify_city(
            city_selection_expert,
            self.origin,
            self.cities,
            self.travel_dates,
            self.interests
        )

        gather_city_info = tasks.gather_city_info(
            local_tour_guide,
            self.cities,
            self.travel_dates,
            self.interests
        )

        # Define your custom crew here
        crew = Crew(
            agents=[expert_travel_agent, city_selection_expert, local_tour_guide],
            tasks=[plan_itinerary, identify_city, gather_city_info],
            verbose=True,
        )

        result = crew.kickoff()
        return result


# This is the main function that you will use to run your custom crew.
if __name__ == "__main__":
    print("## Welcome to Trip Agency Crew")
    print("-------------------------------")
    origin = input(dedent("""From where will you be traveling from?"""))
    cities = input(dedent("""What are the cities options you are interested in visiting?"""))
    travel_dates = input(dedent("""What is the date range you are interested in traveling?"""))
    interests = input(dedent("""What are some of your high-level interests and hobbies?"""))

    trip_crew = TripCrew(origin, cities, travel_dates, interests)
    result = trip_crew.run()

    print("\n\n########################")
    print("## Here is your custom crew run result:")
    print("########################\n")
    print(result)  # Debug print

    # Save the results to the SQLite database in the /data directory
    conn = sqlite3.connect(database_path)
    cursor = conn.cursor()

    # Create the results table if it doesn't exist
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS results (
        id INTEGER PRIMARY KEY,
        origin TEXT,
        cities TEXT,
        travel_dates TEXT,
        interests TEXT,
        result TEXT
    )
    ''')

    # Insert the result into the table
    cursor.execute('''
    INSERT INTO results (origin, cities, travel_dates, interests, result)
    VALUES (?, ?, ?, ?, ?)
    ''', (origin, cities, travel_dates, interests, str(result)))

    # Commit the transaction
    conn.commit()

    # Fetch the last inserted record
    cursor.execute('''
    SELECT * FROM results WHERE id = (SELECT MAX(id) FROM results)
    ''')
    latest_record = cursor.fetchone()
    print("\n\n########################")
    print("## Latest Record:")
    print("########################\n")
    print(latest_record)

    # Close the database connection
    conn.close()