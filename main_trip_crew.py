import os
from textwrap import dedent
from dotenv import load_dotenv
from services.trip import run_trip_crew, save_trip_result, get_latest_result
from database.models import init_db

# Load environment variables
load_dotenv()

# Initialize the database
init_db()

# This is the main function that you will use to run your custom crew.
if __name__ == "__main__":
    print("## Welcome to Trip Agency Crew")
    print("-------------------------------")
    origin = input(dedent("""From where will you be traveling from?"""))
    cities = input(dedent("""What are the cities options you are interested in visiting?"""))
    travel_dates = input(dedent("""What is the date range you are interested in traveling?"""))
    interests = input(dedent("""What are some of your high-level interests and hobbies?"""))

    result = run_trip_crew(origin, cities, travel_dates, interests)

    print("\n\n########################")
    print("## Here is your custom crew run result:")
    print("########################\n")
    print(result)  # Debug print

    save_trip_result(origin, cities, travel_dates, interests, str(result))

    latest_record = get_latest_result()
    print("\n\n########################")
    print("## Latest Record:")
    print("########################\n")
    print(f"ID: {latest_record.id}")
    print(f"Origin: {latest_record.origin}")
    print(f"Cities: {latest_record.cities}")
    print(f"Travel Dates: {latest_record.travel_dates}")
    print(f"Interests: {latest_record.interests}")
    print(f"Result:\n{latest_record.result}")