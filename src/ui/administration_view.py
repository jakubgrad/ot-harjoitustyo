from tkinter import ttk, constants
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

        heading_label = ttk.Label(
            master=self._frame, text="Set the parameters of the model")

        administrators_label = ttk.Label(master=self._frame, text="House age")
        self._administrators_entry = ttk.Entry(master=self._frame)

        type_of_heating_label = ttk.Label(
            master=self._frame, text="Type of heating 1-9")
        self._type_of_heating_entry = ttk.Entry(master=self._frame)

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

        heading_label.grid(row=0, column=0, columnspan=2,
                           sticky=constants.W, padx=5, pady=5)
        house_age_label.grid(row=1, column=0, padx=5, pady=5)
        self._house_age_entry.grid(row=1, column=1, sticky=(
            constants.E, constants.W), padx=5, pady=5)
        type_of_heating_label.grid(row=2, column=0, padx=5, pady=5)
        self._type_of_heating_entry  .grid(row=2, column=1, sticky=(
            constants.E, constants.W), padx=5, pady=5)
        update_button.grid(row=3, column=0, columnspan=2, sticky=(
            constants.E, constants.W), padx=5, pady=5)
        logout_button.grid(row=4, column=0, columnspan=2, sticky=(
            constants.E, constants.W), padx=5, pady=5)

        # Adjust column configuration for root widget
        self._root.grid_columnconfigure(0, weight=1)

    def _handle_logout_click(self):
        self._handle_login()

    def _update_click(self):
        house_age = self._house_age_entry.get()
        type_of_heating_entry = self._type_of_heating_entry.get()
        new_parameters = house_age + "," + type_of_heating_entry
        print(f"new_parameters {new_parameters }")

        print(f"house age:{house_age}")
        print(f"type of heating:{type_of_heating_entry}")
        print(f"_administrator._id:{self._administrator._id}")
        house_service.update_house(self._administrator._id, new_parameters)

        self._handle_house(self._administrator)

        # self, root, handle_login, handle_assessment, user._id):
