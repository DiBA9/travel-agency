from sqlalchemy import create_engine, Column, Integer, String, Text, Float, Boolean, JSON
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from config import DATABASE_URL

Base = declarative_base()
engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

class AgentDetails(Base):
    __tablename__ = 'agent_details'
    id = Column(Integer, primary_key=True, index=True)
    role = Column(String, unique=True, nullable=False)
    backstory = Column(Text, nullable=False)
    goal = Column(Text, nullable=False)
    tools = Column(Text, nullable=False)
    llm_model_name = Column(String, nullable=False)
    llm_temperature = Column(Float, nullable=False)

class CrewDetails(Base):
    __tablename__ = 'crew_details'
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, unique=True, nullable=False)
    description = Column(Text, nullable=False)
    created_at = Column(DateTime, nullable=False)
    updated_at = Column(DateTime, nullable=False)    
    tasks = Column(Text, nullable=False)  # Comma-separated list of task names
    agents = Column(Text, nullable=False)  # Comma-separated list of agent roles
    process = Column(String, nullable=True)
    verbose = Column(String, nullable=True)
    manager_llm = Column(String, nullable=True)
    function_calling_llm = Column(String, nullable=True)
    config = Column(JSON, nullable=True)  # Define config as a JSON type
    max_rpm = Column(Integer, nullable=True)
    language = Column(String, nullable=True)
    language_file = Column(String, nullable=True)
    memory = Column(String, nullable=True)
    cache = Column(String, nullable=True)
    embedder = Column(String, nullable=True)
    full_output = Column(String, nullable=True)
    step_callback = Column(String, nullable=True)
    task_callback = Column(String, nullable=True)
    share_crew = Column(String, nullable=True)
    output_log_file = Column(String, nullable=True)

class TaskDetails(Base):
    __tablename__ = 'task_details'
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, unique=True, nullable=False)
    description = Column(Text, nullable=False)
    agent = Column(String, nullable=False)
    expected_output = Column(Text, nullable=False)
    tools = Column(Text, nullable=True)  # Comma-separated list of tools
    async_execution = Column(Boolean, default=False)
    context = Column(Text, nullable=True)  # Comma-separated list of context tasks
    config = Column(JSON, nullable=True)  # JSON field for additional configuration
    output_json = Column(Boolean, default=False)
    output_pydantic = Column(Boolean, default=False)
    output_file = Column(Text, nullable=True)  # Path to save the output file
    callback = Column(Text, nullable=True)  # String representation of a callable
    human_input = Column(Boolean, default=False)
    created_at = Column(String, nullable=False)
    updated_at = Column(String, nullable=False)

class TripResults(Base):
    __tablename__ = 'results'
    id = Column(Integer, primary_key=True, index=True)
    origin = Column(String, nullable=False)
    cities = Column(String, nullable=False)
    travel_dates = Column(String, nullable=False)
    interests = Column(String, nullable=False)
    result = Column(String, nullable=False)

def init_db():
    Base.metadata.create_all(bind=engine)