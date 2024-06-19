from typing import List
from sqlalchemy.orm import Session
from database.models import SessionLocal, TripResults
from database.crud import (
    create_trip_results,
    read_trip_results_by_id,
    read_trip_results_by_origin,
    read_all_trip_results,
    update_trip_results,
    delete_trip_results
)

def create_trip_record(origin: str, cities: str, travel_dates: str, 
        interests: str, result: str, created_at: str, updated_at: str
    ) -> TripResults:
    db: Session = SessionLocal()
    try:
        trip_results = TripResults(
            origin=origin,
            cities=cities,
            travel_dates=travel_dates,
            interests=interests,
            result=result,
            created_at=created_at,
            updated_at=updated_at
        )
        return create_trip_results(db, trip_results)
    finally:
        db.close()

def retrieve_trip_by_id(result_id: int) -> TripResults:
    db: Session = SessionLocal()
    try:
        return read_trip_results_by_id(db, result_id)
    finally:
        db.close()

def retrieve_trip_by_origin(origin: str) -> TripResults:
    db: Session = SessionLocal()
    try:
        return read_trip_results_by_origin(db, origin)
    finally:
        db.close()

def retrieve_all_trips() -> List[TripResults]:
    db: Session = SessionLocal()
    try:
        return read_all_trip_results(db)
    finally:
        db.close()

def update_trip_record(result_id: int, trip_data: dict) -> TripResults:
    db: Session = SessionLocal()
    try:
        return update_trip_results(db, result_id, trip_data)
    finally:
        db.close()

def delete_trip_record(result_id: int) -> None:
    db: Session = SessionLocal()
    try:
        delete_trip_results(db, result_id)
    finally:
        db.close()