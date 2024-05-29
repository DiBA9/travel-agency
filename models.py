from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from config import DATABASE_URL

Base = declarative_base()

class TripResult(Base):
    __tablename__ = 'results'
    id = Column(Integer, primary_key=True, index=True)
    origin = Column(String, nullable=False)
    cities = Column(String, nullable=False)
    travel_dates = Column(String, nullable=False)
    interests = Column(String, nullable=False)
    result = Column(String, nullable=False)

engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

def init_db():
    Base.metadata.create_all(bind=engine)