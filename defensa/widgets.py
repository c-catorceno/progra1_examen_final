from sqlserver_to_mysql.connections import *
from sqlserver_to_mysql.functions_migration import *
import options.options_registration as registration

import tkinter as tk
from tkinter import messagebox
from tkinter import ttk

def migrate_to_mysql(actual_conn, status_label) -> mysql.connector.connection.MySQLConnection:
    try:
        old_c = actual_conn.cursor()

        new_actual_conn = connect_mysqll()
        new_c = new_actual_conn.cursor()

        db_name = "Gym_migrado"
        new_c.execute(f"SHOW DATABASES LIKE '{db_name}';")
        if new_c.fetchone():
            messagebox.showinfo("Migración", f"La base de datos '{db_name}' ya existe. La migración ya fue realizada.'")
            return 

        new_c.execute(f"CREATE DATABASE {db_name};")
        new_c.execute(f"USE {db_name};")
        tables = ["CLIENTE", "SERVICIO", "INSCRIPCION", "PAGOS", "ASISTENCIA", "ENTRENADORES"]
        for table_name in tables:
            status_label.config(text=f"Migrando tabla: {table_name}")
            status_label.update_idletasks()

            columns = get_schema(table_name, old_c)
            create_tables(table_name, columns, new_c)
            migrate_records(table_name, columns, old_c, new_c)
            new_actual_conn.commit()
            status_label.config(text=f"Tabla {table_name} migrada exitosamente.")
            status_label.update_idletasks()

        status_label.config(text="Aplicando modificaciones adicionales...")
        status_label.update_idletasks()
        get_relations(new_c)
        new_actual_conn.commit()
        status_label.config(text="Modificaciones aplicadas exitosamente.")
        status_label.update_idletasks()

        status_label.config(text="Migración completed. Connection closed to SQL Server. Connected to MySQL successfully.")
        
        return new_actual_conn
    except pyodbc.Error as e:
        messagebox.showerror("SQL Server Error", f"An error ocurred: \n{str(e)}")
        status_label.config(text="SQL Server migration failed.")
    except Error as e:
        messagebox.showerror("MySQL Error", f"An error ocurred: \n{str(e)}")
        status_label.config(text="MySQL migration failed.")

    finally:
        if actual_conn:
            if new_actual_conn.is_connected():
                new_c.close()
                new_actual_conn.close()
                print("We are on close mysql")
            else:
                old_c.close()
                actual_conn.close()
                print("We are on close sqlserver")
            print("We are on sqlserver")

def create_comboboxes(central_frame, menus_config : list[tuple]):
    comboboxes : list[ttk.Combobox] = []
    for menu_name, values, row, column in menus_config:
        combobox = ttk.Combobox(central_frame, values=values, state="readonly")
        combobox.set(menu_name)
        combobox.grid(row=row, column=column, pady=10)
        comboboxes.append(combobox)
    return comboboxes

def open_dialog(selection):
    dialog = tk.Toplevel()
    dialog.title(selection)

    entries = []

    if selection == "New Client": registration.new_client(dialog, entries)
    if selection == "Existing Client": pass 

    if selection == "Add attendance": pass 
    if selection == "Search Attendance": pass 

    if selection == "Register a New Trainer": pass 
    if selection == "Modify Salary": pass 
    if selection == "Dismiss Trainer": pass 

    if selection == "Available Services": pass 
    if selection == "Add Service": pass 
    if selection == "Remove Service": pass 

    if selection == "Add Payment": pass 
    if selection == "Check Debt": pass 

