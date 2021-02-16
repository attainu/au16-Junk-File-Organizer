from tkinter import ttk
from interface.gui_elements import GuiFormElements
import tkinter as tk


if __name__ == "__main__":
    root = tk.Tk()
    root.geometry("400x420")
    root.title('Junk File Organizer')

    address = tk.StringVar()
    method = tk.StringVar()

    user_entry = ttk.Frame(root)
    user_entry.pack(padx = 10, pady = 10, fill = 'x', expand = True)

    fill = GuiFormElements(address, method)
    fill.addressLabel(user_entry)
    fill.dropDownInput(user_entry) 
    fill.organizeButton(user_entry)
    GuiFormElements.commentLabel()

    root.mainloop()