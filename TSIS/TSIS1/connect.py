import psycopg2
from config import DB_CONFIG

def get_connection():
    return psycopg2.connect(
        host=DB_CONFIG[0],
        port=DB_CONFIG[1],
        user=DB_CONFIG[3],
        dbname=DB_CONFIG[2],
        password=DB_CONFIG[4]
    )