# Creates a decorator to handle the database connection/cursor opening/closing.
# Creates the cursor with DictCursor, thus it returns dictionaries.
from config import Config
import psycopg2
import psycopg2.extras
import time
import datetime


def query_select(sql_str, variables=None, connection_str=Config.DB_CONNECTION_STR):
    try:
        with psycopg2.connect(connection_str) as connection:
            with connection.cursor(cursor_factory=psycopg2.extras.RealDictCursor) as cursor:
                cursor.execute(sql_str, variables)
                return cursor.fetchall()
    except psycopg2.DatabaseError as exception:
        print(exception)


def query_modify(sql_str, variables, connection_str=Config.DB_CONNECTION_STR):
    try:
        with psycopg2.connect(connection_str) as connection:
            with connection.cursor() as cursor:
                cursor.execute(sql_str, variables)
                connection.commit()
                print(sql_str.split()[0] + " done.")
    except psycopg2.DatabaseError as exception:
        connection.rollback()
        print(exception)
