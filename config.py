import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Get the database URL from environment variable
relative_db_url = os.getenv('DATABASE_URL')

# Convert to absolute path relative to the project's root directory
if relative_db_url.startswith('sqlite:///'):
    base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))  # Get the parent directory of the current file
    db_path = relative_db_url.replace('sqlite:///', '', 1)
    absolute_db_path = os.path.join(base_dir, db_path)
    DATABASE_URL = f'sqlite:///{absolute_db_path}'
else:
    DATABASE_URL = relative_db_url