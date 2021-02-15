from logic_classes.selected_method import OrganiseMethod
import tkinter as tk
from tkinter import Label, ttk


def execute():
    OrganiseMethod(address.get(), method.get())

if __name__ == "__main__":
    root = tk.Tk()
    root.geometry("400x420")
    root.title('Junk File Organizer')

    address = tk.StringVar()
    method = tk.StringVar()

    user_entry = ttk.Frame(root)
    user_entry.pack(padx = 10, pady = 10, fill = 'x', expand = True)

    address_label = ttk.Label(user_entry, text = "Directory Address:")
    address_label.pack(fill = 'x', expand = True)

    address_entry = ttk.Entry(user_entry, textvariable = address)
    address_entry.pack(fill = 'x', expand = True, pady = 10)
    address_entry.focus()

    method_label = ttk.Label(user_entry, text = "Organize Method:")
    method_label.pack(fill = 'x', expand = True, pady = 10)

    methods = ('extension', 'size', 'last_modified')
    month_cb = ttk.Combobox(user_entry, textvariable = method)
    month_cb['values'] = methods
    month_cb['state'] = 'readonly'  
    month_cb.pack(fill = 'x', padx = 5, pady = 5)

    organize_button = ttk.Button(user_entry, text = "organize", command = execute)
    organize_button.pack(fill = 'x', expand = True, pady = 20)

    Label(text = " 1. Fill the address/path of the folder/ directory").pack(anchor = "w")
    Label(text = "    in the Directory address bar.\n").pack(anchor = "w")
    Label(text = " 2. Fill the organize method:").pack(anchor = "w")
    Label(text = "         - extension").pack(anchor = "w")
    Label(text = "         - size").pack(anchor = "w")
    Label(text = "         - last_modified").pack(anchor = "w")
    Label(text = "   # Thanks for using the Junk File Organizer.", font = "comicsans 10 bold", pady = 10).pack(anchor = "w")

    root.mainloop()