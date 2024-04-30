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

        self.lbl_house_age = tk.Label(
            self._frame, bg="#000080", fg="#ffffff", padx=5, pady=5, text="House Age parameters (influence of the year of construction on the energy consumption and pollution)")

        self.lbl_types_of_heating = tk.Label(
            self._frame, bg="#000080", fg="#ffffff", padx=5, pady=5, text="Types of heating parameters (influence of heating a house has on the the energy consumption and pollution)")

        #self.txt_edit = tk.Text(self._frame, width=40, height=5)

        #self.txt_edit.insert(tk.END, "5+5")

        #update_button = tk.Button(
        #    master=self._frame,
        #    text="Update",
        #    command=lambda: self._update_click(),
        #    bg="#808000", fg="#ffffff"
        #)

        logout_button = tk.Button(
            master=self._frame,
            text="Logout",
            command=lambda: self._handle_logout_click(),
            bg="#ff8c00", fg="#ffffff"
        )

        send_types_of_heating_button = tk.Button(
            master=self._frame,
            text="Send",
            command=lambda: self._send_types_of_heating()
        )

        send_house_age_button = tk.Button(
            master=self._frame,
            text="Send",
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

        #label = tk.Label(self._frame, text="Types of:")
        #label.grid(row=8, column=0, pady=5, sticky='ew')

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

        #label = tk.Label(self._frame, text="Types of:")
        #label.grid(row=8, column=0, pady=5, sticky='ew')

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


        #    constants.E, constants.W), padx=5, pady=5)

        send_types_of_heating_button.grid(row=10, column=0, columnspan=5, sticky=(
            constants.E, constants.W), padx=5, pady=5)
        #self.txt_edit.grid(row=3, column=0, columnspan=2, sticky="ew")

        #update_button.grid(row=4, column=0, columnspan=2, sticky=(
        #    constants.E, constants.W), padx=5, pady=5)
        logout_button.grid(row=11, column=0, columnspan=5, sticky=(
            constants.E, constants.W), padx=5, pady=5)


        # Adjust column configuration for root widget
        self._root.grid_columnconfigure(0, weight=1)

    #def _update_click(self):
    #    text = self.txt_edit.get("1.0", tk.END)
    #    print(text)
    #
    #    if house_service.check_equation(text):
    #        print("equation checked, works")
    #    print("equation checked, doesnt work")
    #    try:
    #        print(eval(text))
    #        messagebox.showinfo(title="Update successfull",
    #                            message="You have successfully updated the model")
    #    except:
    #        print("Failed to evalute")
    #        messagebox.showerror(title="Update failed",
    #                             message="Failed to parse your input")

    def _send_house_age(self):
        min_year = self.min_year_entry.get()
        max_year=self.max_year_entry.get()
        ha_energy_consumption = self.ha_energy_consumption_entry.get()
        ha_pollution = self.ha_pollution_entry.get()
        SUCCESS = 1
        if min_year == "":
            SUCCESS = 0
        if max_year == "":
            SUCCESS = 0
        if ha_energy_consumption  == "":
            SUCCESS = 0
        if ha_pollution  == "":
            SUCCESS = 0
        if SUCCESS == 0:
            messagebox.showerror(title="Uploading data failed",
                                 message="One of the fields was empty")
            return 
        house_age = {}
        house_age["min_year"]=min_year
        house_age["max_year"]=max_year
        house_age["ha_energy_consumption"]=ha_energy_consumption
        house_age["ha_pollution"]=ha_pollution
        if house_service.update_model(house_age):
            print("database updated succeeeded")
            messagebox.showinfo(title="Uploading data succeeded", 
                                message="Database upload successful.")
        else:
            print("database update failed")
            messagebox.showerror(title="Uploading data failed",
                                 message="Database update failed")


    def _send_types_of_heating(self):
        type_of_heating = self.type_entry.get()
        name = self.name_entry.get()
        energy_consumption = self.toh_energy_consumption_entry.get()
        pollution = self.toh_pollution_entry.get()
        SUCCESS = 1
        if type_of_heating == "":
            SUCCESS = 0
        if name == "":
            SUCCESS = 0
        if energy_consumption == "":
            SUCCESS = 0
        if pollution == "":
            SUCCESS = 0
        if SUCCESS == 0:
            messagebox.showerror(title="Uploading data failed",
                                 message="One of the fields was empty")
            return 
        types_of_heating = {}
        types_of_heating["type_of_heating"] = type_of_heating
        types_of_heating["name"] = name
        types_of_heating["energy_consumption"] = energy_consumption
        types_of_heating["pollution"] = pollution
        if house_service.update_model(types_of_heating):
            print("Database update succeeded")
            messagebox.showinfo(title="Uploading data succeeded", 
                                message="Database upload successful.")
        else:
            print("Database update failed")
            messagebox.showerror(title="Uploading data failed",
                                 message="Database update failed")

    def _handle_logout_click(self):
        self._handle_login()

