from abc import ABC
import mysql.connector
from mysql.connector.errors import custom_error_exception

class DB(ABC):
    conn=mysql.connector.connect(
        host="db",
        user="root",
        password="root",
        database="mabdd",
        port=3306
    )

    @staticmethod
    def connect():
        try:
            cursor=DB.conn.cursor(dictionary=True)
            return cursor
        except mysql.connector.Error as e:
            print(e)
    
