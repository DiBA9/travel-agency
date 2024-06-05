from sqlalchemy.orm import Session
from database.models import SessionLocal, TripResult
from database.crud import (
    get_all_trip_results,
    get_trip_results_by_city,
    get_trip_results_sorted_by_date,
    get_latest_trip_result,
    get_trip_result_by_id,
    create_trip_result
)

def retrieve_all_trip_results() -> list:
    db: Session = SessionLocal()
    try:
        results = get_all_trip_results(db)
        return results
    finally:
        db.close()

def retrieve_trip_results_by_city(city: str) -> list:
    db: Session = SessionLocal()
    try:
        results = get_trip_results_by_city(db, city)
        return results
    finally:
        db.close()

def retrieve_trip_results_sorted_by_date(descending: bool = True) -> list:
    db: Session = SessionLocal()
    try:
        results = get_trip_results_sorted_by_date(db, descending)
        return results
    finally:
        db.close()

def retrieve_trip_result_by_id(id: int) -> TripResult:
    db: Session = SessionLocal()
    try:
        result = get_trip_result_by_id(db, id)
        return result
    finally:
        db.close()

def save_trip_result(origin: str, cities: str, travel_dates: str, interests: str, result: str) -> TripResult:
    db: Session = SessionLocal()
    try:
        created_result = create_trip_result(db, origin, cities, travel_dates, interests, result)
        return created_result
    finally:
        db.close()