from sqlalchemy.orm import Session
from models import TripResult

def get_latest_trip_result(db: Session):
    return db.query(TripResult).order_by(TripResult.id.desc()).first()

def create_trip_result(db: Session, origin: str, cities: str, travel_dates: str, interests: str, result: str):
    db_trip_result = TripResult(
        origin=origin,
        cities=cities,
        travel_dates=travel_dates,
        interests=interests,
        result=result
    )
    db.add(db_trip_result)
    db.commit()
    db.refresh(db_trip_result)
    return db_trip_result