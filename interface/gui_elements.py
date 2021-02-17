from methods.selected_method import OrganiseMethod
from tkinter import ttk, Label


class GuiFormElements():
    def __init__(self, address, method):
        self.address = address
        self.method = method

    def addressLabel(self, user_entry):
        address_label = ttk.Label(user_entry, text="Directory Address:")
        address_label.pack(fill='x', expand=True)

        address_entry = ttk.Entry(user_entry, textvariable=self.address)
        address_entry.pack(fill='x', expand=True, pady=10)
        address_entry.focus()

    def dropDownInput(self, user_entry):
        method_label = ttk.Label(user_entry, text="Organize Method:")
        method_label.pack(fill='x', expand=True, pady=10)

        methods = ('extension', 'size', 'last_modified', 'recently_used')
        month_cb = ttk.Combobox(user_entry, textvariable=self.method)
        month_cb['values'] = methods
        month_cb['state'] = 'readonly'
        month_cb.pack(fill='x', padx=5, pady=5)

    def organizeButton(self, user_entry):
        button = ttk.Button(user_entry, text="organize", command=self.execute)
        button.pack(fill='x', expand=True, pady=20)

    def execute(self):
        OrganiseMethod(self.address.get(), self.method.get())

    def commentLabel():
        comment = " 1. Fill the address/path of the folder/ directory"
        Label(text=comment).pack(anchor="w")
        Label(text="    in the Directory address bar.\n").pack(anchor="w")
        Label(text=" 2. Fill the organize method:").pack(anchor="w")
        Label(text="         - extension").pack(anchor="w")
        Label(text="         - size").pack(anchor="w")
        Label(text="         - last_modified").pack(anchor="w")
        last_comment = "   # Thanks for using the Junk File Organizer."
        font_comment = "comicsans 10 bold"
        Label(text=last_comment, font=font_comment, pady=10).pack(anchor="w")
