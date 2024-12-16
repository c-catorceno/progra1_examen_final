from tkinter import messagebox

def accept(dialog, entries):
    values = [entry.get().strip() for entry in entries]
    if all(values[:len(entries) - 2]):
        messagebox.showinfo("Confirmation", f"Parameters received: {values}")
        dialog.destroy()
    else: messagebox.showerror("Error", "Requeried fields must be completed.")