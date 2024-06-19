import os
import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

# Add the path to the system path for imports
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from database.models import Base
from config import DATABASE_URL

engine = create_engine(DATABASE_URL)
Base.metadata.create_all(engine)
