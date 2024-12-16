from sqlserver_to_mysql.connections import *
from sqlserver_to_mysql.functions_migration import *
import options.options_registration as registration
import options.options_attendance as attendance
import options.options_payments as payments
import options.options_services as services
import options.options_trainers as trainers

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
    if selection == "Existing Client": registration.existing_client(dialog, entries)

    if selection == "Add attendance": attendance.add(dialog, entries)
    if selection == "Search Attendance": attendance.search(dialog, entries)

    if selection == "Register a New Trainer": trainers.new_treiner(dialog, entries)
    if selection == "Modify Salary": trainers.modify_salary(dialog, entries)
    if selection == "Fire Trainer": trainers.dismiss_trainer(dialog, entries)

    if selection == "Modify Schedule": services.modify_schedule(dialog, entries)
    if selection == "Add Service": services.add(dialog, entries)
    if selection == "Remove Service": services.remove(dialog, entries)

    if selection == "Add Payment": payments.add(dialog, entries)
    if selection == "Check Debt": payments.check_debt(dialog, entries)
