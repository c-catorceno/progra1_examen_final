#para sqlserver.
from sqlserver_to_mysql.connections import *
from tkinter import ttk
import tkinter as tk
cliente_opt : list[str] = ["Nombre", "Apellido"]
servicio_opt : list[str] = ["Nombre"]
entrenadores_opt : list[str] = ["Nombre", "Apellido", "Correo", "Turno"]

def show_submenu(selection, central_frame):
    submenu_options = {
        "cliente": cliente_opt,
        "servicio": servicio_opt,
        "entrenadores": entrenadores_opt
    }
    if selection in submenu_options:
        submenu = ttk.Combobox(central_frame, values=submenu_options[selection])
        submenu.grid(row=5, column=0, columnspan=2, pady=10)
        submenu.set(f"Select from {selection}")
        submenu.bind("<<ComboboxSelected>>", submenu_selected)

def submenu_selected(event):
    subselection = event.widget.get()
    print(f"Submenu selection: {subselection}") 
    if subselection in cliente_opt: dialog_table("CLIENTE", "ClienteID", subselection)
    elif subselection in servicio_opt: dialog_table("SERVICIO", "ServicioID", subselection)
    elif subselection in entrenadores_opt: dialog_table("ENTRENADORES", "EntrenadorID", subselection)


def dialog_table(table_name, table_key, subselection):    
    dialog = tk.Toplevel()
    dialog.title(subselection)
    
    create_new_column(table_name, table_key, subselection)
    conn = connect_sqlserver()
    mycursor = conn.cursor()

    mycursor.execute(f"SELECT {subselection}, is_palindrome FROM {table_name}")
    i = 1
    for row in mycursor.fetchall():
        tk.Label(dialog, text=f"{row[0]}", ).grid(row=i, column=0, padx=10, pady=5)
        tk.Label(dialog, text=f"{row[1]}", ).grid(row=i, column=1, padx=10, pady=5)
        i += 1

def create_new_column(selected_table, table_key, selected_column):
    new_column : str = 'is_palindrome'
    conn = connect_sqlserver()
    mycursor = conn.cursor()

    mycursor.execute(f"""
                     SELECT COLUMN_NAME
                     FROM INFORMATION_SCHEMA.COLUMNS
                     WHERE TABLE_NAME = '{selected_table}' AND COLUMN_NAME = '{new_column}';
                     """)
    column_exists = mycursor.fetchone() is not None 
    
    if not column_exists:
        mycursor.execute(f"""
        ALTER TABLE {selected_table}
            ADD {new_column} VARCHAR(50);
        """)
        conn.commit()

    mycursor.execute(f"SELECT {table_key}, {selected_column} FROM {selected_table}")
    records = mycursor.fetchall()

    for record in records:
        primary_key = record[0]
        value = record[1]

        is_palindrome : str = ''
        if rec_palindrome(value) == True:
            is_palindrome = 'YES'
        else: is_palindrome = 'NO'

        mycursor.execute(f"""UPDATE {selected_table}
                             SET {new_column} = ?
                             WHERE {table_key} = ?
                             """, (is_palindrome, primary_key))
        conn.commit()

    mycursor.close()
    conn.close()

def rec_palindrome(record : str):
    record = record.lower().replace(" ", "")
    if len(record) <= 1: return True 
    if record[0] != record[-1]:
        return False 
    return rec_palindrome(record[1:-1])
