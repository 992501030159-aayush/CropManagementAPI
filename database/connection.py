import mysql.connector
from utils.logger import logger
from dotenv import load_dotenv
import os

load_dotenv()

def get_db():
    conn = None
    try:
        conn = mysql.connector.connect(
            host = os.getenv("DB_HOST"),
            user = os.getenv("DB_USER"),
            password = os.getenv("DB_PASSWORD"),
            database = os.getenv("DB_NAME")
    )
        logger.info("DataBase Connected")
        yield conn
    except Exception:
        logger.exception("Database connection failed! ")
        raise 
    finally:
        if conn:
            conn.close()
            logger.info("Database connection closed! ")
