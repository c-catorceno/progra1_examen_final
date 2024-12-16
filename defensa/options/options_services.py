import tkinter as tk
from accept_message import accept

def modify_schedule(dialog, entries) -> None:
    tk.Label(dialog, text="Nombre:").grid(row=0, column=0, padx=10, pady=5)
    entry = tk.Entry(dialog)
    entry.grid(row=0 , column=1 , padx=10, pady=5)
    entries.append(entry)

    tk.Label(dialog, text="HoraInicio:").grid(row=1, column=0, padx=10, pady=5)
    entry = tk.Entry(dialog)
    entry.grid(row=1 , column=1 , padx=10, pady=5)
    entries.append(entry)

    tk.Label(dialog, text="HoraFin:").grid(row=2, column=0, padx=10, pady=5)
    entry = tk.Entry(dialog)
    entry.grid(row=2 , column=1 , padx=10, pady=5)
    entries.append(entry)

    accept_button = tk.Button(dialog, text="Accept", command=lambda: accept(dialog, entries))
    accept_button.grid(row=3, column=0, columnspan=2, pady=10)

def add(dialog, entries) -> None:
    tk.Label(dialog, text="Nombre:").grid(row=0, column=0, padx=10, pady=5)
    entry = tk.Entry(dialog)
    entry.grid(row=0 , column=1 , padx=10, pady=5)
    entries.append(entry)

    tk.Label(dialog, text="HoraInicio:").grid(row=1, column=0, padx=10, pady=5)
    entry = tk.Entry(dialog)
    entry.grid(row=1 , column=1 , padx=10, pady=5)
    entries.append(entry)

    tk.Label(dialog, text="HoraFin:").grid(row=2, column=0, padx=10, pady=5)
    entry = tk.Entry(dialog)
    entry.grid(row=2 , column=1 , padx=10, pady=5)
    entries.append(entry)

    accept_button = tk.Button(dialog, text="Accept", command=lambda: accept(dialog, entries))
    accept_button.grid(row=3, column=0, columnspan=2, pady=10)

def remove(dialog, entries) -> None:
    tk.Label(dialog, text="Nombre:").grid(row=0, column=0, padx=10, pady=5)
    entry = tk.Entry(dialog)
    entry.grid(row=0 , column=1 , padx=10, pady=5)
    entries.append(entry)

    accept_button = tk.Button(dialog, text="Accept", command=lambda: accept(dialog, entries))
    accept_button.grid(row=1, column=0, columnspan=2, pady=10)
