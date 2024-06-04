from database.crud import get_latest_trip_result, create_trip_result
from database.models import SessionLocal
from controllers.crews import TripCrew

#### Trip
def run_trip_crew(origin, cities, travel_dates, interests):
    trip_crew = TripCrew(origin, cities, travel_dates, interests)
    result = trip_crew.run()
    return result

def save_trip_result(origin, cities, travel_dates, interests, result):
    db = SessionLocal()
    try:
        return create_trip_result(db, origin, cities, travel_dates, interests, result)
    finally:
        db.close()

def get_latest_result():
    db = SessionLocal()
    try:
        return get_latest_trip_result(db)
    finally:
        db.close()