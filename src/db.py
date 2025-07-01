import psycopg2
from dotenv import load_dotenv
import os

load_dotenv()

def get_connection():
    print(repr(os.getenv("DATABASE_URL")))
    return psycopg2.connect(os.getenv('DATABASE_URL'))