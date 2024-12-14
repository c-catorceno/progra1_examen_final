import tkinter as tk
from tkinter import messagebox
import connections
import query 

# Variables globales para conexiones
sqlserver_connection = None
mysql_connection = None


def connect_to_sqlserver(status_label):
    global sqlserver_connection
    try:
        sqlserver_connection = connections.connect_sqlserver()
        status_label.config(text="Connected to SQLServer successfully.")
    except Exception as e:
        status_label.config(text="Failed to connect to SQLServer.")
        messagebox.showerror("Connection Error", f"Failed to connect to SQLServer: {str(e)}")

def migrate_to_mysql(status_label):
    global sqlserver_connection
    
    try:
        if not sqlserver_connection:
            raise connections.Error("No active connection to SQL Server.")

        mysql_connection = connections.connect_mysqll()
        
        old_c = sqlserver_connection.cursor()
        new_c = mysql_connection.cursor()

        # Verificar si la base de datos ya existe para no volver a hacer la migracion
        db_name = "Gym_migrado"
        new_c.execute(f"SHOW DATABASES LIKE '{db_name}';")
        if new_c.fetchone():  
            messagebox.showinfo("Migración", f"La base de datos '{db_name}' ya existe. La migración ya fue realizada.")
            return 
        
        # Crear base de datos si no existe
        new_c.execute(f"CREATE DATABASE {db_name};")
        new_c.execute(f"USE {db_name};") 

        # Tablas a migrar
        tables = ["CLIENTE", "SERVICIO", "INSCRIPCION", "PAGOS", "ASISTENCIA", "ENTRENADORES"]

        for table_name in tables:
            status_label.config(text=f"Migrando tabla: {table_name}")
            status_label.update_idletasks()

            # Obtener esquema de la tabla
            old_c.execute(f"""
                SELECT COLUMN_NAME, DATA_TYPE 
                FROM INFORMATION_SCHEMA.COLUMNS 
                WHERE TABLE_NAME = '{table_name}';
            """)
            columns = old_c.fetchall()

            # Crear tabla en MySQL
            create_table_query = f"CREATE TABLE {table_name} ("
            column_properties = []
            for column in columns:
                column_name, data_type = column

                # Mapear los tipos de datos de SQL Server a MySQL
                if data_type in ["nvarchar", "varchar"]:
                    data_type = "VARCHAR(50)"
                else: data_type = data_type

                column_properties.append(f"{column_name} {data_type}")
            create_table_query += ", ".join(column_properties) + ");"
            new_c.execute(create_table_query)

            # Obtener datos de la tabla
            old_c.execute(f"SELECT * FROM {table_name};")
            rows = old_c.fetchall()

            # Insertar datos en MySQL
            if rows:
                placeholders = ", ".join(["%s"] * len(columns))  # Genera placeholders dinámicos
                insert_query = f"INSERT INTO {table_name} VALUES ({placeholders});"
                for row in rows:
                    new_c.execute(insert_query, tuple(row))  # Convierte Row a tupla antes de insertar
                
                mysql_connection.commit()

            status_label.config(text=f"Tabla {table_name} migrada exitosamente.")
            status_label.update_idletasks()

        # Agregar otras propiedades de las columnas y las relaciones entre tablas
        status_label.config(text="Aplicando modificaciones adicionales...")
        status_label.update_idletasks()

        sql_script = query.other_properties()
        for statement in sql_script.split(';'):  # Divide el script en sentencias individuales
            if statement.strip():  # Ignorar líneas vacías
                new_c.execute(statement + ';')
        mysql_connection.commit()
        status_label.config(text="Modificaciones aplicadas exitosamente.")
        status_label.update_idletasks()

        # Placeholder:
        status_label.config(text="Migración completada exitosamente.")
        status_label.update_idletasks()

        status_label.config(text="Migration completed. Connection closed to SQLServer.")

    except connections.Error as e:
        messagebox.showerror("SQL Server Error", f"An error occurred with SQL Server:\n{str(e)}")
        status_label.config(text="SQL Server migration failed.")
    except connections.connector.Error as e:
        messagebox.showerror("MySQL Error", f"An error occurred with MySQL:\n{str(e)}")
        status_label.config(text="MySQL migration failed.")

    finally:
        if sqlserver_connection:
            old_c.close()
            sqlserver_connection.close()
            sqlserver_connection = None
        if mysql_connection.is_connected():
            new_c.close()

def close_actual_connection ():
    global sqlserver_connection
    global mysql_connection
    if sqlserver_connection: print("SQL Server connection closed.")
    else: print("MySQL connection closed.")

def open_dialog(title):
    def accept():
        param1 = entry1.get()
        param2 = entry2.get()
        if param1 and param2:
            messagebox.showinfo("Confirmation", f"Parameters received: {param1}, {param2}")
            dialog.destroy()
        else:
            messagebox.showerror("Error", "Both fields must be completed.")

    dialog = tk.Toplevel()
    dialog.title(title)

    tk.Label(dialog, text="Parameter 1:").grid(row=0, column=0, padx=10, pady=5)
    entry1 = tk.Entry(dialog)
    entry1.grid(row=0, column=1, padx=10, pady=5)

    tk.Label(dialog, text="Parameter 2:").grid(row=1, column=0, padx=10, pady=5)
    entry2 = tk.Entry(dialog)
    entry2.grid(row=1, column=1, padx=10, pady=5)

    accept_button = tk.Button(dialog, text="Accept", command=accept)
    accept_button.grid(row=2, column=0, columnspan=2, pady=10)
