import tkinter as tk
from accept_message import accept

def new_client(dialog, entries) -> None:
    tk.Label(dialog, text="CI:").grid(row=0, column=0, padx=10, pady=5)
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

    tk.Label(dialog, text="Telefono (opcional):").grid(row=3, column=0, padx=10, pady=5)
    entry = tk.Entry(dialog)
    entry.grid(row=3 , column=1 , padx=10, pady=5)
    entries.append(entry)

    tk.Label(dialog, text="CantidadMeses:").grid(row=4, column=0, padx=10, pady=5)
    entry = tk.Entry(dialog)
    entry.grid(row=4 , column=1 , padx=10, pady=5)
    entries.append(entry)

    tk.Label(dialog, text="FechaInicio(AAAA-MM-DD):").grid(row=5, column=0, padx=10, pady=5)
    entry = tk.Entry(dialog)
    entry.grid(row=5 , column=1 , padx=10, pady=5)
    entries.append(entry)

    accept_button = tk.Button(dialog, text="Accept", command=lambda: accept(dialog, entries))
    accept_button.grid(row=6, column=0, columnspan=2, pady=10)
