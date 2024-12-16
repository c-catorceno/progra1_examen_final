from sqlserver_to_mysql import connections
from tkinter import messagebox 

def connect_to_sqlserver(status_label) -> connections.pyodbc.Connection:
    global sqlserver_connection
    try:
        sqlserver_connection = connections.connect_sqlserver()
        status_label.config(text="Connected to SQLServer successfully.")
        return sqlserver_connection
    except Exception as e:
        status_label.config(text="Failed to connect to SQLServer.")
        messagebox.showerror("Connection Error", f"Failed to connect to SQLServer: {str(e)}")

def close_actual_connection(actual_conn):
    if type(actual_conn) == connections.pyodbc.Connection:
        actual_conn.close()
        print("SQL Server connection closed.")
    else:
        actual_conn.close()
        print("MySQL connection closed.")
