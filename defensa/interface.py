import tkinter as tk
from tkinter import ttk
from functions import *
from widgets import *
from defense_function import show_submenu

import tkinter as tk 
from tkinter import ttk

window = tk.Tk()
window.title("Gimnasio")
window.geometry("700x650")
central_frame = tk.Frame(window)
central_frame.place(relx=0.5, rely=0.5, anchor="center")

# 1. Conexión a SQL Server, confirmación a través de una etiqueta
status_label = tk.Label(central_frame, text="Not connected to SQLServer", font=("Arial", 12))
status_label.grid(row=0, column=0, columnspan=2, pady=10)
actual_conn = connect_to_sqlserver(status_label)

# 2. Boton migracion a MySQL
def handle_migration():
    global actual_conn 
    new_conn = migrate_to_mysql(actual_conn, status_label)
    if new_conn: actual_conn = new_conn
migrate_button = tk.Button(central_frame, text="Migrate to MySQL", command=lambda: handle_migration())
migrate_button.grid(row=1, column=0, columnspan=2, pady=10)

# 3. Menus desplegables
palindrome_options : list[str] = ["cliente", "servicio", "entrenadores"]
menus_config : list[tuple] = [
    ("Registration", ["New Client", "Existing Client"], 2, 0),
    ("Manage Attendance", ["Add attendance", "Search Attendance"], 2, 1),
    ("Manage Trainers", ["Register a New Trainer", "Modify Salary", "Dismiss Trainer"], 3, 0),
    ("Services", ["Available Services", "Add Service", "Remove Service"], 3, 1),
    ("Payments", ["Add Payment", "Check Debt"], 4, 0),
    ("Verify Palindrome", palindrome_options, 4, 1),
]
menus : list[ttk.Combobox]= create_comboboxes(central_frame, menus_config)

# 4. Cuadro de diálogo según la elección
def menu_selected(event):
    selection = event.widget.get()
    if selection in palindrome_options: # submenu for palindrome menu
        show_submenu(selection, central_frame)
    elif selection != "":
        open_dialog(selection)

for menu in menus:
    menu.bind("<<ComboboxSelected>>", menu_selected) 

window.mainloop()
close_actual_connection(actual_conn)
