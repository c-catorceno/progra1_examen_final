import tkinter as tk
from accept_message import accept

def add(dialog, entries) -> None:
    tk.Label(dialog, text="InscripcionID:").grid(row=0, column=0, padx=10, pady=5)
    entry = tk.Entry(dialog)
    entry.grid(row=0 , column=1 , padx=10, pady=5)
    entries.append(entry)

    tk.Label(dialog, text="ServicioID:").grid(row=1, column=0, padx=10, pady=5)
    entry = tk.Entry(dialog)
    entry.grid(row=1 , column=1 , padx=10, pady=5)
    entries.append(entry)

    tk.Label(dialog, text="Fecha:").grid(row=2, column=0, padx=10, pady=5)
    entry = tk.Entry(dialog)
    entry.grid(row=2 , column=1 , padx=10, pady=5)
    entries.append(entry)

    tk.Label(dialog, text="Hora Ingreso:").grid(row=3, column=0, padx=10, pady=5)
    entry = tk.Entry(dialog)
    entry.grid(row=3 , column=1 , padx=10, pady=5)
    entries.append(entry)

    accept_button = tk.Button(dialog, text="Accept", command=lambda: accept(dialog, entries))
    accept_button.grid(row=4, column=0, columnspan=2, pady=10)

def search(dialog, entries) -> None:
    tk.Label(dialog, text="InscripcionID: ").grid(row=0, column=0, padx=10, pady=5)
    entry = tk.Entry(dialog)
    entry.grid(row=0 , column=1 , padx=10, pady=5)
    entries.append(entry)

    tk.Label(dialog, text="Fecha:").grid(row=1, column=0, padx=10, pady=5)
    entry = tk.Entry(dialog)
    entry.grid(row=1 , column=1 , padx=10, pady=5)
    entries.append(entry)

    accept_button = tk.Button(dialog, text="Accept", command=lambda: accept(dialog, entries))
    accept_button.grid(row=2, column=0, columnspan=2, pady=10)
