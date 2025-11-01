# Forecasting Service Configuration
import os
from dotenv import load_dotenv

load_dotenv()

# Service Configuration
FORECASTING_PORT = int(os.getenv('FORECASTING_PORT', 5000))
FLASK_DEBUG = os.getenv('FLASK_DEBUG', 'False').lower() == 'true'

# Database Configuration - Use DATABASE_URL for Supabase (preferred)
DATABASE_URL = os.getenv('DATABASE_URL', 
    'postgresql://postgres.nacwxaebqxiihwgowaok:XmwcJTZ2QF0qSn6M@aws-1-ap-southeast-1.pooler.supabase.com:5432/postgres'
)

# Alternative: Individual database config (if DATABASE_URL not provided)
DB_CONFIG = {
    'host': os.getenv('DB_HOST', 'aws-1-ap-southeast-1.pooler.supabase.com'),
    'port': os.getenv('DB_PORT', '5432'),
    'database': os.getenv('DB_NAME', 'postgres'),
    'user': os.getenv('DB_USER', 'postgres.nacwxaebqxiihwgowaok'),
    'password': os.getenv('DB_PASS', 'XmwcJTZ2QF0qSn6M')
}
