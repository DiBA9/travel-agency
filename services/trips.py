from typing import List
from sqlalchemy.orm import Session
from database.models import SessionLocal, TripResults
from database.crud import (
    create_trip_result,
    retrieve_trip_result,
    retrieve_trip_result_by_origin,
    retrieve_all_trip_results,
    update_trip_result,
    delete_trip_result
)

def create_trip_record(origin: str, cities: str, travel_dates: str, interests: str, result: str) -> TripResults:
    db: Session = SessionLocal()
    try:
        trip_result = TripResults(
            origin=origin,
            cities=cities,
            travel_dates=travel_dates,
            interests=interests,
            result=result
        )
        return create_trip_result(db, trip_result)
    finally:
        db.close()

def retrieve_trip_by_id(result_id: int) -> TripResults:
    db: Session = SessionLocal()
    try:
        return retrieve_trip_result(db, result_id)
    finally:
        db.close()

def retrieve_trip_by_origin(origin: str) -> TripResults:
    db: Session = SessionLocal()
    try:
        return retrieve_trip_result_by_origin(db, origin)
    finally:
        db.close()

def retrieve_all_trip_results() -> List[TripResults]:
    db: Session = SessionLocal()
    try:
        return retrieve_all_trip_results(db)
    finally:
        db.close()

def update_trip_record(result_id: int, trip_data: dict) -> TripResults:
    db: Session = SessionLocal()
    try:
        return update_trip_result(db, result_id, trip_data)
    finally:
        db.close()

def delete_trip_record(result_id: int) -> None:
    db: Session = SessionLocal()
    try:
        delete_trip_result(db, result_id)
    finally:
        db.close()