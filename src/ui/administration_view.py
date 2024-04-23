from tkinter import ttk, constants, messagebox
import tkinter as tk
from services.house_service import house_service


class AdministrationView:
    def __init__(self, root, administrator, handle_login):
        self._root = root
        self._handle_login = handle_login
        self._frame = None
        self._administrator_id = administrator._id
        self._administrator = administrator

        self._initialize()

    def destroy(self):
        self._frame.destroy()

    def _initialize(self):
        self._frame = ttk.Frame(master=self._root)
        # Grid the frame within the root widget
        self._frame.grid(row=0, column=0)

        self.txt_edit = tk.Text(self._frame, width=40, height=5)

        self.txt_edit.insert(tk.END, "5+5")

        update_button = tk.Button(
            master=self._frame,
            text="Update",
            command=lambda: self._update_click(),
            bg="#808000", fg="#ffffff"
        )

        logout_button = tk.Button(
            master=self._frame,
            text="Logout",
            command=lambda: self._handle_logout_click(),
            bg="#ff8c00", fg="#ffffff"
        )

        self.model = house_service.get_model()

        self.tree_house_age = ttk.Treeview(self._frame)
        self.tree_house_age['columns'] = (
            'Min Year', 'Max Year', 'Energy Consumption', 'Pollution')

        self.tree_house_age.heading('#0', text='ID')
        self.tree_house_age.heading('Min Year', text='Min Year')
        self.tree_house_age.heading('Max Year', text='Max Year')
        self.tree_house_age.heading(
            'Energy Consumption', text='Energy Consumption')
        self.tree_house_age.heading('Pollution', text='Pollution')

        for row in self.model._house_age:
            self.tree_house_age.insert(
                '', 'end', text=row[0], values=(row[1], row[2], row[3], row[4]))

        self.tree_types_of_heating = ttk.Treeview(self._frame)
        self.tree_types_of_heating['columns'] = (
            'Type', 'Name', 'Energy Consumption', 'Pollution')

        self.tree_types_of_heating.heading('#0', text='ID')
        self.tree_types_of_heating.heading('Type', text='Type')
        self.tree_types_of_heating.heading('Name', text='Name')
        self.tree_types_of_heating.heading(
            'Energy Consumption', text='Energy Consumption')
        self.tree_types_of_heating.heading('Pollution', text='Pollution')

        for row in self.model._types_of_heating:
            self.tree_types_of_heating.insert(
                '', 'end', text=row[0], values=(row[1], row[2], row[3], row[4]))

        self.tree_house_age.grid(row=1, column=0, columnspan=2, sticky=(
            constants.E, constants.W), padx=5, pady=5)
        self.tree_types_of_heating.grid(row=2, column=0, columnspan=2, sticky=(
            constants.E, constants.W), padx=5, pady=5)

        self.txt_edit.grid(row=3, column=0, columnspan=2, sticky="ew")
        update_button.grid(row=4, column=0, columnspan=2, sticky=(
            constants.E, constants.W), padx=5, pady=5)
        logout_button.grid(row=5, column=0, columnspan=2, sticky=(
            constants.E, constants.W), padx=5, pady=5)

        # Adjust column configuration for root widget
        self._root.grid_columnconfigure(0, weight=1)

    def _update_click(self):
        text = self.txt_edit.get("1.0", tk.END)
        print(text)

        if house_service.check_equation(text):
            print("equation checked, works")
        print("equation checked, doesnt work")
        try:
            print(eval(text))
            messagebox.showinfo(title="Update successfull",
                                message="You have successfully updated the model")
        except:
            print("Failed to evalute")
            messagebox.showerror(title="Update failed",
                                 message="Failed to parse your input")

    def _handle_logout_click(self):
        self._handle_login()
