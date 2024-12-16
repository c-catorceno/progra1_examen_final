import pyodbc
import mysql.connector 
from mysql.connector import Error 

def connect_sqlserver() -> pyodbc.Connection:
    return pyodbc.connect(
        "Driver={ODBC Driver 17 for SQL Server};"
        "Server=DESKTOP-K99GLDO\\SQLEXPRESS;"
        "Database=Gym;" 
        "Trusted_Connection=yes;"
    )

def connect_mysqll() -> mysql.connector.connection.MySQLConnection:
    return mysql.connector.connect(
        host="127.0.0.1",
        user="root",
        password="Quitaelojodelroj0"
    )
