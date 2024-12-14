import tkinter as tk
from tkinter import ttk
from functions import *

window = tk.Tk()
window.title("Gimnasio")
window.geometry("700x650")
central_frame = tk.Frame(window)
central_frame.place(relx=0.5, rely=0.5, anchor="center")

# 1. Conexion a SQL Server, confirmación a través de una etiqueta
status_label = tk.Label(central_frame, text="Not connected to SQLServer", font=("Arial", 12))
status_label.grid(row=0, column=0, columnspan=2, pady=10)
connect_to_sqlserver(status_label)

# 2. Boton migracion a MySQL
migrate_button = tk.Button(central_frame, text="Migrate to MySQL", command=lambda: migrate_to_mysql(status_label))
migrate_button.grid(row=1, column=0, columnspan=2, pady=10)

# 3. Menus despegables
menu_registration = ttk.Combobox(central_frame, values=["New Client", "Existing Client"], state="readonly")
menu_registration.set("Registration")
menu_registration.grid(row=2, column=0, pady=10)

menu_attendance = ttk.Combobox(central_frame, values=["Add Attendance", "Remove Attendance"], state="readonly")
menu_attendance.set("Manage Attendance")
menu_attendance.grid(row=2, column=1, pady=10)

menu_trainers = ttk.Combobox(central_frame, values=["Register a New Trainer", "Modify Salary", "Dismiss Trainer"], state="readonly")
menu_trainers.set("Manage Trainers")
menu_trainers.grid(row=3, column=0, pady=10)

menu_services = ttk.Combobox(central_frame, values=["Available Services", "Add Service", "Remove Service"], state="readonly")
menu_services.set("Services")
menu_services.grid(row=3, column=1, pady=10)

menu_payments = ttk.Combobox(central_frame, values=["Add Payment", "Check Debt"], state="readonly")
menu_payments.set("Payments")
menu_payments.grid(row=4, column=0, pady=10)

# Cuadro de diálogo según la selección
def menu_selected(event):
    selection = event.widget.get()
    if selection != "":
        open_dialog(selection)

menus = [menu_registration, menu_attendance, menu_trainers, menu_services, menu_payments]
for menu in menus:
    menu.bind("<<ComboboxSelected>>", menu_selected) # las funciones que ocurriran al seleccionar una opcion

window.mainloop()

close_actual_connection()