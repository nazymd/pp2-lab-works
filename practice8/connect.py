import psycopg2
from config import datas
def conn():
    return psycopg2.connect(
    host = datas[0],
    port = datas[1],
    dbname = datas[2],
    user = datas[3],
    password = datas[4]
)
