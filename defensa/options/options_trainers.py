import tkinter as tk
from accept_message import accept

def new_treiner(dialog, entries) -> None:
    tk.Label(dialog, text="ServicioID:").grid(row=0, column=0, padx=10, pady=5)
    entry = tk.Entry(dialog)
    entry.grid(row=0 , column=1 , padx=10, pady=5)
    entries.append(entry)

    tk.Label(dialog, text="Nombre:").grid(row=1, column=0, padx=10, pady=5)
    entry = tk.Entry(dialog)
    entry.grid(row=1 , column=1 , padx=10, pady=5)
    entries.append(entry)

    tk.Label(dialog, text="Apellido:").grid(row=2, column=0, padx=10, pady=5)
    entry = tk.Entry(dialog)
    entry.grid(row=2 , column=1 , padx=10, pady=5)
    entries.append(entry)

    tk.Label(dialog, text="Telefono:").grid(row=3, column=0, padx=10, pady=5)
    entry = tk.Entry(dialog)
    entry.grid(row=3 , column=1 , padx=10, pady=5)
    entries.append(entry)

    tk.Label(dialog, text="Correo (opcional):").grid(row=4, column=0, padx=10, pady=5)
    entry = tk.Entry(dialog)
    entry.grid(row=4 , column=1 , padx=10, pady=5)
    entries.append(entry)

    tk.Label(dialog, text="FechaInicio(AAAA-MM-DD):").grid(row=5, column=0, padx=10, pady=5)
    entry = tk.Entry(dialog)
    entry.grid(row=5 , column=1 , padx=10, pady=5)
    entries.append(entry)

    tk.Label(dialog, text="Sueldo:").grid(row=5, column=0, padx=10, pady=5)
    entry = tk.Entry(dialog)
    entry.grid(row=6 , column=1 , padx=10, pady=5)
    entries.append(entry)

    tk.Label(dialog, text="Turno:").grid(row=5, column=0, padx=10, pady=5)
    entry = tk.Entry(dialog)
    entry.grid(row=7 , column=1 , padx=10, pady=5)
    entries.append(entry)

    accept_button = tk.Button(dialog, text="Accept", command=lambda: accept(dialog, entries))
    accept_button.grid(row=8, column=0, columnspan=2, pady=10)

def modify_salary(dialog, entries) -> None:
    tk.Label(dialog, text="EntrenadorID:").grid(row=0, column=0, padx=10, pady=5)
    entry = tk.Entry(dialog)
    entry.grid(row=0 , column=1 , padx=10, pady=5)
    entries.append(entry)

    tk.Label(dialog, text="Nuevo sueldo:").grid(row=1, column=0, padx=10, pady=5)
    entry = tk.Entry(dialog)
    entry.grid(row=1 , column=1 , padx=10, pady=5)
    entries.append(entry)

    accept_button = tk.Button(dialog, text="Accept", command=lambda: accept(dialog, entries))
    accept_button.grid(row=2, column=0, columnspan=2, pady=10)


def fire_trainer(dialog, entries) -> None:
    tk.Label(dialog, text="EntrenadorID:").grid(row=0, column=0, padx=10, pady=5)
    entry = tk.Entry(dialog)
    entry.grid(row=0 , column=1 , padx=10, pady=5)
    entries.append(entry)

    tk.Label(dialog, text="FechaFin:").grid(row=1, column=0, padx=10, pady=5)
    entry = tk.Entry(dialog)
    entry.grid(row=1 , column=1 , padx=10, pady=5)
    entries.append(entry)

    accept_button = tk.Button(dialog, text="Accept", command=lambda: accept(dialog, entries))
    accept_button.grid(row=2, column=0, columnspan=2, pady=10)
