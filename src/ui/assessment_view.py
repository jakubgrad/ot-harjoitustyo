from tkinter import ttk, constants
import tkinter as tk
from services.house_service import house_service


class AssessmentView:
    """Class representing the view for filling out a basic assessment about the user's home.

    Args:
        root (tk.Tk): The root Tkinter window.
        handle_login (function): Function to handle the logout action
        handle_house (function): Function to handle switching to house view.
        user (User): The user object associated with the view.
    """

    def __init__(self, root, handle_login, handle_house, user):
        self._root = root
        self._handle_login = handle_login
        self._handle_house = handle_house
        self._frame = None
        self._house_age_entry = None
        self._type_of_heating_entry = None
        self._user_id = user._id
        self._user = user

        self._initialize()

    def destroy(self):
        """Destroys the AssessmentView frame."""
        self._frame.destroy()

    def _initialize(self):
        self._frame = ttk.Frame(master=self._root)
        # Grid the frame within the root widget
        self._frame.grid(row=0, column=0)

        heading_label = ttk.Label(
            master=self._frame, text="Fill out a basic assessment about your home!")

        house_age_label = ttk.Label(master=self._frame, text="House age / construction year")
        self._house_age_entry = ttk.Entry(master=self._frame)


        type_of_heating_label = ttk.Label(
            master=self._frame, 
            text="Types of heating 1-8:")

        heating_types_label = ttk.Label(
            master=self._frame, 
            text="1. Gas boiler\n"
                 "2. Electric heater\n"
                 "3. Wood stove\n"
                 "4. Solar panels\n"
                 "5. District heating\n"
                 "6. Gil boiler\n"
                 "7. Pellet stove\n"
                 "8. Geothermal heating"
        )


        self._type_of_heating_entry = ttk.Entry(master=self._frame)

        update_button = tk.Button(
            master=self._frame,
            text="Update",
            command=lambda: self._update_click()
        )
        logout_button = tk.Button(
            master=self._frame,
            text="Logout",
            command=lambda: self._handle_logout_click()
        )

        heading_label.grid(row=0, column=0, columnspan=2,
                           sticky=constants.W, padx=5, pady=5)
        house_age_label.grid(row=1, column=0, padx=5, pady=5)
        self._house_age_entry.grid(row=1, column=1, sticky=(
            constants.E, constants.W), padx=5, pady=5)
        type_of_heating_label.grid(row=2, column=0, padx=5, pady=5)
        self._type_of_heating_entry  .grid(row=2, column=1, sticky=(
            constants.E, constants.W), padx=5, pady=5)
        heating_types_label.grid(row=3, column=0, columnspan=2, padx=5, pady=5) 
        update_button.grid(row=4, column=0, columnspan=2, sticky=(
            constants.E, constants.W), padx=5, pady=5)
        logout_button.grid(row=5, column=0, columnspan=2, sticky=(
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
        print(f"_user._id:{self._user._id}")
        # house_id = house_service.get_users_house_id(self._user._id)
        # print(f"house_id found in UI:{house_id}")
        house_service.update_house(self._user._id, new_parameters)

        self._handle_house(self._user)

        # self, root, handle_login, handle_assessment, user._id):
