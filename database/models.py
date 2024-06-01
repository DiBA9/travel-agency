from sqlalchemy import create_engine, Column, Integer, String, Text, Float
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

class AgentDetails(Base):
    __tablename__ = 'agent_details'
    id = Column(Integer, primary_key=True, index=True)
    role = Column(String, unique=True, nullable=False)
    backstory = Column(Text, nullable=False)
    goal = Column(Text, nullable=False)
    tools = Column(Text, nullable=False)
    llm_model_name = Column(String, nullable=False)
    llm_temperature = Column(Float, nullable=False)

engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

def init_db():
    Base.metadata.create_all(bind=engine)