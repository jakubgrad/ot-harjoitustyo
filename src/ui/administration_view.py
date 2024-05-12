from tkinter import ttk, constants, messagebox
import tkinter as tk
from services.house_service import house_service


class AdministrationView:
    """Class representing the administration view for managing house-related data and administrators.

    Args:
        root (tk.Tk): The root Tkinter window.
        administrator: The administrator object associated with the view.
        handle_login (function): Function to handle the logout action.
    """

    def __init__(self, root, administrator, handle_login):
        self._root = root
        self._handle_login = handle_login
        self._frame = None
        self._administrator_id = administrator._id
        self._administrator = administrator

        self._initialize()

    def destroy(self):
        """Destroys the AdministrationView frame."""
        self._frame.destroy()

    def _initialize(self):
        self._frame = ttk.Frame(master=self._root)
        # Grid the frame within the root widget
        self._frame.grid(row=0, column=0)

        self.lbl_house_age = tk.Label(
            self._frame, padx=5, pady=5, text="House Age parameters (influence of the year of construction on the energy consumption and pollution)")

        self.lbl_types_of_heating = tk.Label(
            self._frame, padx=5, pady=5, text="Types of heating parameters (influence of heating a house has on the the energy consumption and pollution)")

        new_admin_button = tk.Button(
            master=self._frame,
            text="Create new admin",
            command=lambda: self._create_new_admin()
        )

        logout_button = tk.Button(
            master=self._frame,
            text="logout",
            command=lambda: self._handle_logout_click()
        )

        send_types_of_heating_button = tk.Button(
            master=self._frame,
            text="Create a new type of_heating",
            command=lambda: self._send_types_of_heating()
        )

        send_house_age_button = tk.Button(
            master=self._frame,
            text="Create a new house age category",
            command=lambda: self._send_house_age()
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
                '', 'end', text=row[0], values=(row[1], row[2], row[3], row[4]),tags=('modify'))

        self.lbl_house_age.grid(row=1, column=0, columnspan=5, sticky=(
            constants.E, constants.W), padx=5, pady=5)
        self.tree_house_age.grid(row=2, column=0, columnspan=5, sticky=(
            constants.E, constants.W), padx=5, pady=5)

        labels = ['Min year', 'Max year', 'Energy consumption:', 'Pollution:']
        self.entries = []

        label = tk.Label(self._frame, text="House age")
        label.grid(row=4, column=0, pady=5, sticky='ew')

        for i, label_text in enumerate(labels):
            label = tk.Label(self._frame, text=label_text)
            label.grid(row=3, column=i+1, pady=5, sticky='ew')
            
        self.min_year_entry = tk.Entry(self._frame)
        self.min_year_entry.grid(row=4,column=1, pady=5, sticky='ew')
        self.max_year_entry = tk.Entry(self._frame)
        self.max_year_entry.grid(row=4,column=2, pady=5, sticky='ew')
        self.ha_energy_consumption_entry = tk.Entry(self._frame)
        self.ha_energy_consumption_entry.grid(row=4,column=3, pady=5, sticky='ew')
        self.ha_pollution_entry = tk.Entry(self._frame)
        self.ha_pollution_entry.grid(row=4,column=4, pady=5, sticky='ew')

        send_house_age_button.grid(row=5, column=0, columnspan=5, sticky=(
            constants.E, constants.W), padx=5, pady=5)

        self.lbl_types_of_heating.grid(row=6, column=0, columnspan=5, sticky=(
            constants.E, constants.W), padx=5, pady=5)
        self.tree_types_of_heating.grid(row=7, column=0, columnspan=5, sticky=(
            constants.E, constants.W), padx=5, pady=5)

        labels = ['Type:', 'Name:', 'Energy consumption:', 'Pollution:']
        self.entries = []

        label = tk.Label(self._frame, text="Types of heating")
        label.grid(row=9, column=0, pady=5, sticky='ew')

        for i, label_text in enumerate(labels):
            label = tk.Label(self._frame, text=label_text)
            label.grid(row=8, column=i+1, pady=5, sticky='ew')
            
        self.type_entry = tk.Entry(self._frame)
        self.type_entry.grid(row=9,column=1, pady=5, sticky='ew')
        self.name_entry = tk.Entry(self._frame)
        self.name_entry.grid(row=9,column=2, pady=5, sticky='ew')
        self.toh_energy_consumption_entry = tk.Entry(self._frame)
        self.toh_energy_consumption_entry.grid(row=9,column=3, pady=5, sticky='ew')
        self.toh_pollution_entry = tk.Entry(self._frame)
        self.toh_pollution_entry.grid(row=9,column=4, pady=5, sticky='ew')

        send_types_of_heating_button.grid(row=10, column=0, columnspan=5, sticky=(
            constants.E, constants.W), padx=5, pady=5)

        label = tk.Label(self._frame, text="Username")
        label.grid(row=11, column=1, pady=5, sticky='ew')
        label = tk.Label(self._frame, text="Password")
        label.grid(row=11, column=2, pady=5, sticky='ew')

        label = tk.Label(self._frame, text="New admin")
        label.grid(row=12, column=0, pady=5, sticky='ew')
        self.new_admin_username = tk.Entry(self._frame)
        self.new_admin_username.grid(row=12,column=1, pady=5, sticky='ew')
        self.new_admin_password = tk.Entry(self._frame)
        self.new_admin_password .grid(row=12,column=2, pady=5, sticky='ew')

        new_admin_button.grid(row=12, column=3, columnspan=1, sticky=(
            constants.E, constants.W), padx=5, pady=5)

        logout_button.grid(row=14, column=0, columnspan=5, sticky=(
            constants.E, constants.W), padx=5, pady=5)

        self._root.grid_columnconfigure(0, weight=1)

    def _send_house_age(self):
        entries = [
            self.min_year_entry.get(),
            self.max_year_entry.get(),
            self.ha_energy_consumption_entry.get(),
            self.ha_pollution_entry.get()
        ]

        if not all(entries):
            messagebox.showerror(title="Uploading data failed",
                                 message="One of the fields was empty")
            return 

        min_year, max_year, ha_energy_consumption, ha_pollution = entries

        new_house_age = {
            "min_year": min_year,
            "max_year": max_year,
            "ha_energy_consumption": ha_energy_consumption,
            "ha_pollution": ha_pollution
        }

        if house_service.update_house_age(new_house_age):
            print("Database update succeeded")
            messagebox.showinfo(title="Uploading data succeeded", 
                                message="Database upload successful.")
        else:
            print("Database update failed")
            messagebox.showerror(title="Uploading data failed",
                                 message="Database update failed")

    def _send_types_of_heating(self):
        entries = [
            self.type_entry.get(),
            self.name_entry.get(),
            self.toh_energy_consumption_entry.get(),
            self.toh_pollution_entry.get()
        ]

        if not all(entries):
            messagebox.showerror(title="Uploading data failed",
                                 message="One of the fields was empty")
            return

        type_of_heating, name, energy_consumption, pollution = entries

        new_toh = {
            "type_of_heating": type_of_heating,
            "name": name,
            "energy_consumption": energy_consumption,
            "pollution": pollution
        }
        if house_service.update_types_of_heating(new_toh):
            print("Database update succeeded")
            messagebox.showinfo(title="Uploading data succeeded", 
                                message="Database upload successful.")
        else:
            print("Database update failed")
            messagebox.showerror(title="Uploading data failed",
                                 message="Database update failed")

    def _create_new_admin(self):
        username_entry = self.new_admin_username.get()
        password_entry = self.new_admin_password .get()

        print(f"Attempt at registering an admin for: {username_entry}")
        admin = house_service.create_new_admin(username_entry, password_entry)
        if admin:
            messagebox.showinfo(title="Success", 
                                message="New admin created.")
        else:
            messagebox.showerror(title="Registration failed",
                                 message="Username taken")

    def _handle_logout_click(self):
        self._handle_login()
