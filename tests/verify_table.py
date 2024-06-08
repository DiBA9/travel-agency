import os
import sys

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from sqlalchemy import create_engine, inspect, text
from sqlalchemy.orm import sessionmaker
from config import DATABASE_URL

# Create an engine and session
engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
session = SessionLocal()

# Create an inspector
inspector = inspect(engine)

# Check if the table exists
tables = inspector.get_table_names()
if 'trip_results' in tables:
    print("Table 'trip_results' exists.")
else:
    print("Table 'trip_results' does not exist.")

# Check if the table is populated
result = session.execute(text("SELECT COUNT(*) FROM trip_results"))
count = result.scalar()
print(f"Table 'trip_results' has {count} rows.")
